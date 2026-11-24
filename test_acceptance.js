const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
const inlineScripts = html.match(/<script(?![^>]*src=)[^>]*>([\s\S]*?)<\/script>/gi) || [];
console.log('Inline scripts found:', inlineScripts.length);
const seedTag = inlineScripts.find(s => s.includes('const SEED_DATA ='));
const mainTag = inlineScripts.find(s => s.includes('let MuleNetState ='));
if (!seedTag || !mainTag) {
  throw new Error('Could not locate SEED_DATA or MuleNetState inline scripts in index.html');
}
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
      appendChild: function(ch) {},
      setAttribute: function(k, v) { this[k] = v; }
    };
  }
  return elements[id];
}

const mockWindow = {
  addEventListener: () => {},
  localStorage: {
    getItem: () => null,
    setItem: () => {},
    removeItem: () => {},
    clear: () => {}
  },
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

try {
  vm.runInContext(seedDataScript, context);
  vm.runInContext(mainScript, context);
  // Call loadInitialData
  vm.runInContext('loadInitialData()', context);
  const state = vm.runInContext('MuleNetState', context);
  console.log('MuleNet initialized successfully:');
  console.log('- Active Case:', state.currentCaseId);
  console.log('- Total Accounts:', state.accounts.length);
  console.log('- Total Transactions:', state.transactions.length);
  console.log('- Total Evidence Files:', state.evidenceFiles.length);

  // Run all self tests
  vm.runInContext('runAllSelfTests()', context);
  const summaryEl = getEl('selfTestsSummaryLabel');
  console.log('\nAcceptance Test Summary:', summaryEl.innerText);

  const containerEl = getEl('selfTestResultsContainer');
  console.log('Results rendered length:', containerEl.innerHTML.length);

  const failedMatches = containerEl.innerHTML.match(/FAILED/g);
  const passedMatches = containerEl.innerHTML.match(/PASSED/g);
  console.log(`Passed tests: ${passedMatches ? passedMatches.length : 0}, Failed tests: ${failedMatches ? failedMatches.length : 0}`);

  if (failedMatches && failedMatches.length > 0) {
    console.error('Some tests failed!');
    process.exit(1);
  } else {
    console.log('ALL ACCEPTANCE TESTS VERIFIED AND PASSED 100%!');
  }
} catch (e) {
  console.error('Execution error:', e);
  process.exit(1);
}

