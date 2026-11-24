const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
const inlineScripts = html.match(/<script(?![^>]*src=)[^>]*>([\s\S]*?)<\/script>/gi);
const seedDataScript = inlineScripts[1].replace(/<\/?script[^>]*>/gi, '');
const mainScript = inlineScripts[2].replace(/<\/?script[^>]*>/gi, '');

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
      appendChild: function(ch) {},
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
  getElementById: getEl,
  querySelectorAll: () => [],
  querySelector: () => null,
  createElement: (tag) => getEl('mock_' + Math.random())
};

const vm = require('vm');
const context = vm.createContext({
  window: mockWindow,
  document: mockDocument,
  localStorage: mockWindow.localStorage,
  console: console,
  setTimeout: setTimeout,
  clearTimeout: clearTimeout,
  navigator: { clipboard: { writeText: () => Promise.resolve() } },
  cytoscape: () => ({ on: () => {}, fit: () => {}, elements: () => ({ remove: () => {} }), add: () => {}, layout: () => ({ run: () => {} }) }),
  jspdf: { jsPDF: function() { return { setFont: () => {}, text: () => {}, save: () => {} }; } },
  XLSX: { utils: { book_new: () => ({}), json_to_sheet: () => ({}), book_append_sheet: () => {} }, writeFile: () => {} }
});
context.window = context;

vm.runInContext(seedDataScript, context);
vm.runInContext(mainScript, context);
vm.runInContext('loadInitialData()', context);

console.log('====================================================');
console.log('MULENET COMPREHENSIVE FORENSIC ENGINE VERIFICATION');
console.log('====================================================\n');

// 1. Bank Statement Parser Test on Real Files
console.log('--- 1. Testing CSV Statement Parsing & Normalization ---');
const kotakCSV = fs.readFileSync('sample_data/kotak_account_A_statement.csv', 'utf8');
const sbiCSV = fs.readFileSync('sample_data/sbi_account_C_statement_inconsistent.csv', 'utf8');

const parsedKotakTxns = vm.runInContext(`parseCSVStatement(${JSON.stringify(kotakCSV)}, 'kotak_account_A_statement.csv')`, context);
console.log(`Parsed Kotak CSV: ${parsedKotakTxns.length} txns extracted.`);
if (parsedKotakTxns.length !== 5) throw new Error('Expected 5 Kotak txns, got ' + parsedKotakTxns.length);

const kotakRecon = vm.runInContext(`verifyStatementReconciliation(parseCSVStatement(${JSON.stringify(kotakCSV)}, 'kotak_account_A_statement.csv'), 40000, 24500)`, context);
console.log(`Kotak Statement Reconciled? ${kotakRecon.isReconciled} | Calculated Closing: ₹${kotakRecon.calculatedClosing}`);
if (!kotakRecon.isReconciled) throw new Error('Kotak statement should reconcile perfectly!');

const parsedSbiTxns = vm.runInContext(`parseCSVStatement(${JSON.stringify(sbiCSV)}, 'sbi_account_C_statement_inconsistent.csv')`, context);
const sbiRecon = vm.runInContext(`verifyStatementReconciliation(parseCSVStatement(${JSON.stringify(sbiCSV)}, 'sbi_account_C_statement_inconsistent.csv'), 5000, 48000)`, context);
console.log(`SBI Inconsistent CSV: ${parsedSbiTxns.length} txns extracted. Reconciled? ${sbiRecon.isReconciled} (Expected: false)`);
if (sbiRecon.isReconciled) throw new Error('SBI inconsistent statement should fail reconciliation due to discrepancy!');
console.log('Statement Inconsistency correctly detected: ' + sbiRecon.error);

// 2. Dynamic Money Trail Analysis (FIFO vs Proportional)
console.log('\n--- 2. Testing Dynamic Money-Trail Graph & Fund Conservation ---');
const fifoTrace = vm.runInContext(`traceMoneyTrailFromVictim('UTR-2024-RJ-894102', 'FIFO')`, context);
console.log(`FIFO Trace: Victim Inflow = ₹${fifoTrace.victimAmount}, Total Residuals = ₹${fifoTrace.totalResidual}, Total Transferred = ₹${fifoTrace.totalTransferred}, Balanced? ${fifoTrace.isBalanced}`);
if (!fifoTrace.isBalanced || fifoTrace.victimAmount !== 100000) throw new Error('FIFO Money conservation violated!');

const propTrace = vm.runInContext(`traceMoneyTrailFromVictim('UTR-2024-RJ-894102', 'PROPORTIONAL')`, context);
console.log(`PROPORTIONAL Trace: Victim Inflow = ₹${propTrace.victimAmount}, Total Residuals = ₹${propTrace.totalResidual}, Balanced? ${propTrace.isBalanced}`);
if (!propTrace.isBalanced) throw new Error('PROPORTIONAL Money conservation violated!');

// 3. Invalid UTR Rejection
console.log('\n--- 3. Testing Nonexistent / Invalid UTR Rejection ---');
const invalidTrace = vm.runInContext(`traceMoneyTrailFromVictim('UTR-BOGUS-999999')`, context);
console.log(`Bogus UTR rejection: Error message = "${invalidTrace.error}", Balanced = ${invalidTrace.isBalanced}`);
if (!invalidTrace.error) throw new Error('Invalid UTR should produce an error!');

// 4. Cross-Case Correlation Engine
console.log('\n--- 4. Testing Multi-Case Cross-Correlation Engine ---');
vm.runInContext(`renderCrossCaseTable()`, context);
const crossCaseTbody = getEl('crossCaseTbody');
console.log(`Cross-case table populated with dynamic rows: ${crossCaseTbody.innerHTML.length > 0}`);
if (crossCaseTbody.innerHTML.length === 0) throw new Error('Expected cross-case table to be populated!');

// 5. Freeze-Priority Dynamic Ranking
console.log('\n--- 5. Testing Dynamic Freeze Priority Calculation ---');
context.fifoTrace = fifoTrace;
const freezeTargets = vm.runInContext(`calculateDynamicFreezePriority(fifoTrace)`, context);
console.log(`Freeze Targets Identified: ${freezeTargets.length}`);
freezeTargets.forEach((t, idx) => {
  console.log(` [Priority ${idx+1}] Acc: ${t.accountNumber} (${t.bank}) | Residual: ₹${t.residual.toLocaleString()} | Risk: ${t.riskScore}/100 | Level: ${t.priorityLevel}`);
});
if (freezeTargets.length === 0) throw new Error('No freeze targets found!');
if (freezeTargets[0].residual < 0) {
  throw new Error('Freeze targets should have valid non-negative residual amounts!');
}

// 6. SHA-256 Pure JS Cryptographic Seal
console.log('\n--- 6. Testing Cryptographic SHA-256 Verification ---');
const testString = "TechTonicX-Rajasthan-Police-Hackathon-2026";
const hash = vm.runInContext(`sha256PureJS(${JSON.stringify(testString)})`, context);
console.log(`SHA-256("${testString}") = ${hash}`);
const crypto = require('crypto');
const expectedHash = crypto.createHash('sha256').update(testString).digest('hex');
console.log(`Node.js crypto SHA-256 matches? ${hash === expectedHash ? 'PERFECT 100% MATCH' : 'MISMATCH'}`);
if (hash !== expectedHash) throw new Error('Pure JS SHA-256 hash mismatch!');

console.log('\n====================================================');
console.log('ALL FORENSIC AUDIT CHECKS PASSED WITH ZERO ERRORS!');
console.log('====================================================');
