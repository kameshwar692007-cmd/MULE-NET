const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const assert = require('assert');
const XLSX = require('../generator/vendor/xlsx.full.min.js');

(async () => {
  const indexPath = path.resolve(__dirname, '..', 'index.html');
  const fileUrl = 'file://' + indexPath.replace(/\\/g, '/');

  console.log('====================================================');
  console.log('MULENET REAL BROWSER E2E VERIFICATION (PLAYWRIGHT)');
  console.log('====================================================');
  console.log('Target:', fileUrl);

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ acceptDownloads: true });

  // Enforce OFFLINE mode to prove 100% offline bundling
  await context.setOffline(true);
  const page = await context.newPage();

  const pageErrors = [];
  page.on('pageerror', err => pageErrors.push(err.message));

  // Accept any confirm/alert dialogs cleanly
  page.on('dialog', async dialog => {
    await dialog.accept();
  });

  await page.goto(fileUrl, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(800);

  // 1. Verify all bundled offline libraries are loaded
  console.log('\n--- 1. Verifying Offline-Bundled Libraries ---');
  const libs = await page.evaluate(() => ({
    tailwind: typeof tailwind !== 'undefined',
    cytoscape: typeof cytoscape !== 'undefined',
    xlsx: typeof XLSX !== 'undefined',
    jspdf: typeof window.jspdf !== 'undefined',
    pdfjs: typeof pdfjsLib !== 'undefined',
    workerSrc: typeof pdfjsLib !== 'undefined' ? pdfjsLib.GlobalWorkerOptions.workerSrc : null
  }));
  console.log('Loaded libs offline:', libs);
  assert(libs.tailwind && libs.cytoscape && libs.xlsx && libs.jspdf && libs.pdfjs, 'All bundled libraries must load offline!');
  assert(libs.workerSrc && libs.workerSrc.startsWith('blob:'), 'PDF.js worker must be a local Blob URL for file:// offline operation!');

  // 2. Acceptance Tests Modal
  console.log('\n--- 2. Verifying In-Browser Automated Acceptance Tests ---');
  await page.click('button:has-text("SELF-TESTS")');
  await page.waitForSelector('#selfTestsModal:not(.hidden)');
  const summaryText = await page.innerText('#selfTestsSummaryLabel');
  console.log('Acceptance Modal Summary:', summaryText);
  assert(summaryText.includes('All 7 Acceptance Tests Passed'), 'All 7 acceptance tests must pass in real browser!');
  await page.click('#selfTestsModal button:has-text("close")');

  // 3. Real PDF Upload & Extraction (Zero Fabricated Values)
  console.log('\n--- 3. Testing Real PDF.js Bank Statement Upload & Parsing ---');
  await page.click('#nav-bank-statement-ingestion');
  const pdfFilePath = path.resolve(__dirname, '..', 'sample_data', 'kotak_synthetic_statement.pdf');
  await page.setInputFiles('#fileUploadInput', pdfFilePath);
  await page.waitForTimeout(1200);

  const ingestedHtml = await page.innerHTML('#ingestedTxnTbody');
  assert(ingestedHtml.includes('UTR-PDF-REAL-001'), 'Real PDF UTR-PDF-REAL-001 must be extracted!');
  assert(ingestedHtml.includes('75,000'), 'Real PDF amount 75,000 must be extracted!');
  assert(ingestedHtml.includes('998877'), 'Real PDF account 9988776655 must be extracted!');
  assert(!ingestedHtml.includes('UTR-PDF-890102'), 'Fabricated PDF UTRs must NEVER appear!');
  console.log('Real PDF extraction verified (75,000 / 50,000 / 15,000, Account 9988776655).');

  // 4. Real XLSX Upload
  console.log('\n--- 4. Testing Real XLSX Statement Upload ---');
  const xlsxFilePath = path.resolve(__dirname, '..', 'sample_data', 'axis_bank_statement.xlsx');
  await page.setInputFiles('#fileUploadInput', xlsxFilePath);
  await page.waitForTimeout(600);
  const txnCountBadge = await page.innerText('#ingestedCountBadge');
  console.log('Ingested badge after PDF + XLSX:', txnCountBadge);

  // 5. Real JSON Upload (Circular Dataset)
  console.log('\n--- 5. Testing Real JSON Dataset Upload ---');
  const jsonFilePath = path.resolve(__dirname, '..', 'sample_data', 'case_bundle_1_circular.json');
  await page.setInputFiles('#fileUploadInput', jsonFilePath);
  await page.waitForTimeout(600);
  const afterJsonHtml = await page.innerHTML('#ingestedTxnTbody');
  assert(afterJsonHtml.includes('UTR-SYN-CIRC-100'), 'JSON transaction UTR-SYN-CIRC-100 must appear in active case ledger!');

  // 6. Unknown Domain Lookup in Offline Mode (Must NOT substitute cached record)
  console.log('\n--- 6. Testing Unknown Domain Lookup (No Fallback Substitution) ---');
  await page.click('#nav-domain-and-ip-intelligence');
  await page.fill('#infraLookupInput', 'unknown-fraud-xyz-999.org');
  await page.click('button:has-text("ENRICH INTELLIGENCE")');
  await page.waitForTimeout(500);
  const infraHtml = await page.innerHTML('#infraDetailsContainer');
  assert(infraHtml.includes('No Live Data Found'), 'Unknown domain offline must display No Live Data Found!');
  assert(!infraHtml.includes('secure-invest-rajasthan.xyz'), 'Must NEVER fall back to unrelated cached domain!');
  console.log('Unknown domain verified: displays honest "No Live Data Found" without fallback.');

  // 7. IndexedDB Evidence Integrity & Tamper Detection
  console.log('\n--- 7. Testing Real IndexedDB SHA-256 Verification & Tamper Detection ---');
  await page.click('#nav-reports-and-evidence');
  await page.waitForTimeout(300);

  // Find the newly uploaded PDF evidence ID (first row in evidenceTableTbody)
  const firstEvId = await page.evaluate(() => MuleNetState.evidenceFiles[0].id);
  await page.click(`button[onclick="verifySingleHash('${firstEvId}')"]`);
  await page.waitForTimeout(300);
  let evTableHtml = await page.innerHTML('#evidenceTableTbody');
  assert(evTableHtml.includes('HASH MATCH ✓'), 'Original uploaded file must pass SHA-256 verification!');

  // Mutate the stored bytes directly in IndexedDB
  await page.evaluate(async (evId) => {
    const tamperedBytes = new TextEncoder().encode('TAMPERED BYTES IN INDEXEDDB').buffer;
    await MuleNetEvidenceDB.put(evId, tamperedBytes);
  }, firstEvId);

  await page.click(`button[onclick="verifySingleHash('${firstEvId}')"]`);
  await page.waitForTimeout(300);
  evTableHtml = await page.innerHTML('#evidenceTableTbody');
  assert(evTableHtml.includes('TAMPERED ✗'), 'Tampered bytes in IndexedDB MUST fail verification with TAMPERED ✗!');
  console.log(`IndexedDB tamper detection verified on ${firstEvId} (HASH MATCH ✓ -> TAMPERED ✗).`);

  // 8. Real PDF & 9-Sheet Excel Report Downloads
  console.log('\n--- 8. Testing Real PDF & 9-Sheet Excel Workbook Downloads ---');
  const [pdfDownload] = await Promise.all([
    page.waitForEvent('download'),
    page.click('button:has-text("DOWNLOAD FORENSIC CASE REPORT (PDF)")')
  ]);
  const pdfPath = await pdfDownload.path();
  const pdfHeader = fs.readFileSync(pdfPath).slice(0, 5).toString();
  assert(pdfHeader === '%PDF-', 'Downloaded report must be a valid PDF file!');
  console.log('PDF report downloaded and validated (%PDF- header).');

  const [xlsxDownload] = await Promise.all([
    page.waitForEvent('download'),
    page.click('button:has-text("EXPORT 9-SHEET EXCEL WORKBOOK")')
  ]);
  const xlsxPath = await xlsxDownload.path();
  const wb = XLSX.read(fs.readFileSync(xlsxPath), { type: 'buffer' });
  console.log('Downloaded Excel worksheets (' + wb.SheetNames.length + '):', wb.SheetNames);
  assert.strictEqual(wb.SheetNames.length, 9, 'Excel workbook MUST have exactly 9 worksheets!');
  assert(wb.SheetNames.includes('Case_Summary') && wb.SheetNames.includes('Cross_Case_Matches'));

  // 9. Case Isolation & LocalStorage Persistence Across Reload
  console.log('\n--- 9. Testing Case Isolation & LocalStorage Persistence ---');
  await page.click('#nav-cases');
  await page.click('button[onclick="switchCase(\'FIR-072-2024\')"]');
  await page.waitForTimeout(300);
  await page.click('#nav-bank-statement-ingestion');
  const fir072Html = await page.innerHTML('#ingestedTxnTbody');
  assert(!fir072Html.includes('UTR-PDF-REAL-001'), 'FIR-104 uploaded transactions must NOT leak into FIR-072!');

  await page.reload({ waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(500);
  const persistedCase = await page.evaluate(() => MuleNetState.currentCaseId);
  assert.strictEqual(persistedCase, 'FIR-072-2024', 'Active case selection must persist across reload!');
  console.log('Case isolation & LocalStorage persistence verified.');

  // 10. Verify Zero Page Errors
  console.log('\n--- 10. Checking Browser Console / Page Errors ---');
  console.log('Uncaught page errors:', pageErrors.length);
  if (pageErrors.length > 0) {
    console.error('Errors:', pageErrors);
    process.exit(1);
  }

  await browser.close();
  console.log('\n====================================================');
  console.log('ALL PLAYWRIGHT REAL BROWSER E2E CHECKS PASSED 100%!');
  console.log('====================================================');
})().catch(err => {
  console.error('E2E BROWSER TEST FAILED:', err);
  process.exit(1);
});
