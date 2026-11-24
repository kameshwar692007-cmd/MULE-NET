const fs = require('fs');
const crypto = require('crypto');
const html = fs.readFileSync('index.html', 'utf8');
const inlineScripts = html.match(/<script(?![^>]*src=)[^>]*>([\s\S]*?)<\/script>/gi) || [];
const seedTag = inlineScripts.find(s => s.includes('const SEED_DATA ='));
const mainTag = inlineScripts.find(s => s.includes('let MuleNetState ='));
if (!seedTag || !mainTag) throw new Error('Missing inline scripts in index.html');

const seedDataScript = seedTag.replace(/<\/?script[^>]*>/gi, '');
const mainScript = mainTag.replace(/<\/?script[^>]*>/gi, '');

const elements = {};
function getEl(id) {
  if (!elements[id]) {
    elements[id] = {
      id: id,
      innerHTML: '',
      innerText: '',
      className: '',
      value: '',
      classList: {
        add: function(c) { this[c] = true; },
        remove: function(c) { delete this[c]; },
        toggle: function(c) { this[c] = !this[c]; }
      },
      style: {},
      appendChild: function() {},
      remove: function() {},
      setAttribute: function(k, v) { this[k] = v; }
    };
  }
  return elements[id];
}

const mockWindow = {
  addEventListener: () => {},
  localStorage: { getItem: () => null, setItem: () => {}, removeItem: () => {}, clear: () => {} },
  location: { reload: () => {} },
  setTimeout: setTimeout,
  clearTimeout: clearTimeout,
  crypto: { subtle: null }
};

const mockDocument = {
  addEventListener: () => {},
  body: { appendChild: () => {} },
  getElementById: getEl,
  querySelectorAll: () => [],
  querySelector: () => null,
  createElement: () => getEl('mock_' + Math.random())
};

const vm = require('vm');
const context = vm.createContext({
  window: mockWindow,
  document: mockDocument,
  localStorage: mockWindow.localStorage,
  console: console,
  setTimeout: setTimeout,
  clearTimeout: clearTimeout,
  TextEncoder: TextEncoder,
  TextDecoder: TextDecoder,
  navigator: { clipboard: { writeText: () => Promise.resolve() } },
  cytoscape: () => ({ on: () => {}, fit: () => {}, elements: () => ({ remove: () => {} }), add: () => {}, layout: () => ({ run: () => {} }) }),
  jspdf: { jsPDF: function() { return { setFont: () => {}, text: () => {}, save: () => {} }; } },
  XLSX: { utils: { book_new: () => ({}), json_to_sheet: () => ({}), book_append_sheet: () => {} }, writeFile: () => {} }
});
context.window = context;

vm.runInContext(seedDataScript, context);
vm.runInContext(mainScript, context);
vm.runInContext('loadInitialData()', context);

(async function runAll() {
  console.log('====================================================');
  console.log('MULENET COMPREHENSIVE FORENSIC ENGINE VERIFICATION');
  console.log('====================================================\n');

  // 1. Bank Statement Parser Test on Real Files + Strict Validation
  console.log('--- 1. Testing CSV Statement Parsing, Strict Validation & Rejected Rows ---');
  const kotakCSV = fs.readFileSync('sample_data/kotak_account_A_statement.csv', 'utf8');
  const sbiCSV = fs.readFileSync('sample_data/sbi_account_C_statement_inconsistent.csv', 'utf8');

  const parsedKotak = vm.runInContext(`parseCSVStatement(${JSON.stringify(kotakCSV)}, 'kotak_account_A_statement.csv', { targetAccount: '9182736450' })`, context);
  console.log(`Parsed Kotak CSV: ${parsedKotak.transactions.length} valid, ${parsedKotak.rejectedRows.length} rejected.`);
  if (parsedKotak.transactions.length !== 5 || parsedKotak.rejectedRows.length !== 0) {
    throw new Error('Expected 5 valid Kotak txns and 0 rejected');
  }

  context.parsedKotakTxns = parsedKotak.transactions;
  const kotakRecon = vm.runInContext(`verifyStatementReconciliation(parsedKotakTxns, 40000, 24500)`, context);
  console.log(`Kotak Statement Reconciled? ${kotakRecon.isReconciled} | Calculated Closing: ₹${kotakRecon.calculatedClosing}`);
  if (!kotakRecon.isReconciled) throw new Error('Kotak statement should reconcile perfectly!');

  const parsedSbi = vm.runInContext(`parseCSVStatement(${JSON.stringify(sbiCSV)}, 'sbi_account_C_statement_inconsistent.csv', { targetAccount: '5519283746' })`, context);
  context.parsedSbiTxns = parsedSbi.transactions;
  const sbiRecon = vm.runInContext(`verifyStatementReconciliation(parsedSbiTxns, 5000, 48000)`, context);
  console.log(`SBI Inconsistent CSV: ${parsedSbi.transactions.length} txns. Reconciled? ${sbiRecon.isReconciled} (Expected: false)`);
  if (sbiRecon.isReconciled) throw new Error('SBI inconsistent statement should fail reconciliation!');

  // Malformed CSV row rejection test (no fabricated defaults)
  const badCSV = "Date,Debit,Credit,Balance,Account,UTR\nNOT-A-DATE,1000,0,500,9182736450,UTR1\n2024-10-18,INVALID_AMT,0,500,9182736450,UTR2\n2024-10-18,500,0,500,,UTR3";
  const parsedBad = vm.runInContext(`parseCSVStatement(${JSON.stringify(badCSV)}, 'malformed.csv')`, context);
  console.log(`Malformed CSV rejected rows: ${parsedBad.rejectedRows.length} (Expected: 3), valid: ${parsedBad.transactions.length}`);
  if (parsedBad.rejectedRows.length !== 3 || parsedBad.transactions.length !== 0) {
    throw new Error('Malformed CSV rows must be rejected, not fabricated!');
  }

  // 2. Dynamic Money Trail Analysis (FIFO vs Proportional + Conservation)
  console.log('\n--- 2. Testing Dynamic Chronological Money-Trail & Fund Conservation ---');
  const fifoTrace = vm.runInContext(`traceMoneyTrailFromVictim('UTR-2024-RJ-894102', 'FIFO')`, context);
  console.log(`FIFO Trace: Victim Inflow = ₹${fifoTrace.victimAmount}, Total Residuals = ₹${fifoTrace.totalResidual}, External = ₹${fifoTrace.externalOutflow}, Balanced? ${fifoTrace.isBalanced}`);
  if (!fifoTrace.isBalanced || fifoTrace.victimAmount !== 100000) throw new Error('FIFO Money conservation violated!');

  const propTrace = vm.runInContext(`traceMoneyTrailFromVictim('UTR-2024-RJ-894102', 'PROPORTIONAL')`, context);
  console.log(`PROPORTIONAL Trace: Victim Inflow = ₹${propTrace.victimAmount}, Total Residuals = ₹${propTrace.totalResidual.toFixed(2)}, External = ₹${propTrace.externalOutflow.toFixed(2)}, Balanced? ${propTrace.isBalanced}`);
  if (!propTrace.isBalanced) throw new Error('PROPORTIONAL Money conservation violated!');

  // 3. Circular Transfer & Repeated Account Visit Test (A -> B -> A -> C)
  console.log('\n--- 3. Testing Circular Fund Flow (A -> B -> A -> C) & Uncovered Destination ---');
  vm.runInContext(`
    MuleNetState.cases.push({ caseId: 'FIR-CIRC-2024', firNo: 'FIR CIRC/2024', victimUTR: 'UTR-CIRC-001', victimFraudAmount: 50000 });
    MuleNetState.transactions.push(
      { id: 'C1', caseId: 'FIR-CIRC-2024', timestamp: '2024-11-01T10:00:00+05:30', account: 'ACC_A', direction: 'CREDIT', credit: 50000, debit: 0, amount: 50000, balance: 50000, utr: 'UTR-CIRC-001', counterpartyAccount: 'VICTIM_X' },
      { id: 'C2', caseId: 'FIR-CIRC-2024', timestamp: '2024-11-01T10:10:00+05:30', account: 'ACC_A', direction: 'DEBIT', credit: 0, debit: 50000, amount: 50000, balance: 0, utr: 'UTR-CIRC-002', counterpartyAccount: 'ACC_B' },
      { id: 'C3', caseId: 'FIR-CIRC-2024', timestamp: '2024-11-01T10:20:00+05:30', account: 'ACC_B', direction: 'CREDIT', credit: 50000, debit: 0, amount: 50000, balance: 50000, utr: 'UTR-CIRC-002', counterpartyAccount: 'ACC_A' },
      { id: 'C4', caseId: 'FIR-CIRC-2024', timestamp: '2024-11-01T10:30:00+05:30', account: 'ACC_B', direction: 'DEBIT', credit: 0, debit: 30000, amount: 30000, balance: 20000, utr: 'UTR-CIRC-003', counterpartyAccount: 'ACC_A' },
      { id: 'C5', caseId: 'FIR-CIRC-2024', timestamp: '2024-11-01T10:40:00+05:30', account: 'ACC_A', direction: 'CREDIT', credit: 30000, debit: 0, amount: 30000, balance: 30000, utr: 'UTR-CIRC-003', counterpartyAccount: 'ACC_B' },
      { id: 'C6', caseId: 'FIR-CIRC-2024', timestamp: '2024-11-01T10:50:00+05:30', account: 'ACC_A', direction: 'DEBIT', credit: 0, debit: 20000, amount: 20000, balance: 10000, utr: 'UTR-CIRC-004', counterpartyAccount: 'ACC_C_NO_STMT' }
    );
    MuleNetState.currentCaseId = 'FIR-CIRC-2024';
  `, context);
  const circTrace = vm.runInContext(`traceMoneyTrailFromVictim('UTR-CIRC-001', 'FIFO')`, context);
  console.log(`Circular Trace: Balanced=${circTrace.isBalanced}, ACC_A retained=₹${circTrace.nodes['ACC_A'].retained}, ACC_B retained=₹${circTrace.nodes['ACC_B'].retained}, ACC_C_NO_STMT=${circTrace.nodes['ACC_C_NO_STMT'].retained} (covered=${circTrace.nodes['ACC_C_NO_STMT'].covered})`);
  if (!circTrace.isBalanced || circTrace.nodes['ACC_A'].retained !== 10000 || circTrace.nodes['ACC_B'].retained !== 20000 || circTrace.nodes['ACC_C_NO_STMT'].covered !== false) {
    throw new Error('Circular trace or uncovered destination attribution failed!');
  }
  vm.runInContext(`MuleNetState.currentCaseId = 'FIR-104-2024';`, context);

  // 4. Invalid UTR Rejection
  console.log('\n--- 4. Testing Nonexistent / Invalid UTR Rejection ---');
  const invalidTrace = vm.runInContext(`traceMoneyTrailFromVictim('UTR-BOGUS-999999')`, context);
  console.log(`Bogus UTR rejection: "${invalidTrace.error}"`);
  if (!invalidTrace.error) throw new Error('Invalid UTR should produce an error!');

  // 5. Cross-Case Correlation Engine
  console.log('\n--- 5. Testing Dynamic Cross-Case Correlation & Review Workflow ---');
  const crossMatches = vm.runInContext(`computeDynamicCrossCaseMatches()`, context);
  console.log(`Dynamic cross-case matches found: ${crossMatches.length}`);
  if (crossMatches.length === 0 || crossMatches.some(m => m.status !== 'PENDING_REVIEW')) {
    throw new Error('Cross-case matches must start as PENDING_REVIEW, never auto-verified!');
  }

  // 6. Freeze-Priority Dynamic Ranking
  console.log('\n--- 6. Testing Dynamic Freeze Priority Calculation ---');
  context.fifoTrace = fifoTrace;
  const freezeTargets = vm.runInContext(`calculateDynamicFreezePriority(fifoTrace)`, context);
  console.log(`Freeze Targets Identified: ${freezeTargets.length}`);
  freezeTargets.forEach((t, idx) => {
    console.log(` [Priority ${idx+1}] Acc: ${t.accountNumber} (${t.bank}) | Residual: ₹${t.residual.toLocaleString()} | Risk: ${t.riskScore}/100 | Level: ${t.priorityLevel}`);
  });
  if (freezeTargets.length === 0) throw new Error('No freeze targets found!');

  // 7. SHA-256 Pure JS + Tamper Detection Verification
  console.log('\n--- 7. Testing Cryptographic SHA-256 & Evidence Tamper Detection ---');
  const testString = "TechTonicX-Rajasthan-Police-Hackathon-2026";
  const hash = vm.runInContext(`sha256PureJS(${JSON.stringify(testString)})`, context);
  const expectedHash = crypto.createHash('sha256').update(testString).digest('hex');
  if (hash !== expectedHash) throw new Error('Pure JS SHA-256 hash mismatch!');
  console.log(`SHA-256 exact match verified: ${hash}`);

  // Simulate storing raw bytes in MuleNetEvidenceDB, verifying, then tampering bytes
  await vm.runInContext(`(async () => {
    const orig = new TextEncoder().encode("Original Statement Bytes").buffer;
    const origHash = await computeRealSHA256(orig);
    MuleNetState.evidenceFiles.push({ id: 'EV-TEST', filename: 'test.csv', sha256: origHash, caseId: 'FIR-104-2024', status: 'RECONCILED' });
    await MuleNetEvidenceDB.put('EV-TEST', orig);
    const okRes = await verifySingleHash('EV-TEST');
    if (!okRes.ok) throw new Error('Expected valid bytes to pass verification!');
    const tampered = new TextEncoder().encode("Tampered Statement Bytes").buffer;
    await MuleNetEvidenceDB.put('EV-TEST', tampered);
    const failRes = await verifySingleHash('EV-TEST');
    if (failRes.ok || failRes.reason !== 'HASH_MISMATCH') throw new Error('Expected tampered bytes to FAIL SHA-256 verification!');
    console.log('Tamper detection verified: modified bytes triggered HASH_MISMATCH!');
  })()`, context);

  console.log('\n====================================================');
  console.log('ALL FORENSIC AUDIT CHECKS PASSED WITH ZERO ERRORS!');
  console.log('====================================================');
})().catch(e => {
  console.error('AUDIT TEST FAILED:', e);
  process.exit(1);
});
