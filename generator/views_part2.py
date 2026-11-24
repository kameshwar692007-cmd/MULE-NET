# generator/views_part2.py
# HTML for Cases, Statement Ingestion, Transaction Explorer, Mule Detection, and Money Trail Analysis

VIEW_CASES = """
<section id="view-cases" class="view-panel hidden">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 pb-2 mb-3 border-b border-outline-variant">
    <div>
      <div class="flex items-center gap-1.5">
        <span class="px-2 py-0.5 rounded bg-primary-container text-surface-container-high font-label-code-sm text-[11px]">CASE REGISTRY // SEC 65B READY</span>
        <span class="text-secondary font-label-code-sm text-[11px] font-bold">• 3 SYNTHETIC INVESTIGATIONS ACTIVE</span>
      </div>
      <h1 class="font-headline-lg text-[18px] font-bold text-on-surface tracking-tight mt-0.5">Police Case Management & Incident Registry</h1>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="openCreateCaseModal()" class="flex items-center gap-1.5 px-3 py-1.5 bg-secondary text-white rounded font-label-caps text-[11px] font-bold tracking-wider hover:bg-blue-700 shadow-sm transition-colors">
        <span class="material-symbols-outlined text-[15px]">add_box</span>
        <span>REGISTER NEW CYBER FIR</span>
      </button>
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-3 gap-3 mb-3" id="casesCardsContainer">
    <!-- Rendered dynamically -->
  </div>

  <!-- Active Case Deep Forensic Context Card -->
  <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant" id="activeCaseDetailContainer">
    <!-- Rendered dynamically -->
  </div>
</section>
"""

VIEW_INGESTION = """
<section id="view-bank-statement-ingestion" class="view-panel hidden">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 pb-2 mb-3 border-b border-outline-variant">
    <div>
      <div class="flex items-center gap-1.5">
        <span class="px-2 py-0.5 rounded bg-primary-container text-surface-container-high font-label-code-sm text-[11px]">INGESTION ENGINE // V4.2-STABLE</span>
        <span class="flex items-center gap-1 text-secondary font-label-code-sm text-[11px]"><span class="w-1.5 h-1.5 rounded-full bg-secondary"></span>45 CBS ADAPTERS READY</span>
      </div>
      <h1 class="font-headline-lg text-[18px] font-bold text-on-surface tracking-tight mt-0.5">Multi-Bank Statement Parsing & Reconciliation Normalisation</h1>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="loadSampleStatementsDemo()" class="flex items-center gap-1.5 px-3 py-1.5 bg-amber-500 hover:bg-amber-600 text-slate-900 rounded font-label-caps text-[11px] font-bold tracking-wider shadow-sm transition-all">
        <span class="material-symbols-outlined text-[15px]">download</span>
        <span>1-CLICK LOAD DEMO STATEMENTS</span>
      </button>
      <button onclick="document.getElementById('fileUploadInput').click()" class="flex items-center gap-1.5 px-3 py-1.5 bg-secondary text-white rounded font-label-caps text-[11px] font-bold tracking-wider hover:bg-blue-700 shadow-sm transition-opacity">
        <span class="material-symbols-outlined text-[15px]">file_upload</span>
        <span>UPLOAD STATEMENT</span>
      </button>
    </div>
  </div>

  <!-- Ingestion Workspace Grid -->
  <div class="grid grid-cols-1 lg:grid-cols-12 gap-3 mb-3">
    <!-- Left Column: Upload Dropzone & Parameters -->
    <div class="lg:col-span-8 flex flex-col gap-3">
      <div class="bg-surface-container-lowest rounded-lg p-3.5 shadow-sm border border-outline-variant flex flex-col">
        <div class="flex items-center justify-between mb-2">
          <div class="flex items-center gap-1.5">
            <span class="material-symbols-outlined text-secondary text-[20px]">file_upload</span>
            <span class="font-headline-sm text-[14px] font-bold text-on-surface">Digital & Physical Statement Ingestion Box</span>
          </div>
          <span class="font-label-code-sm text-[10px] text-on-surface-variant bg-surface-container-low px-2 py-0.5 rounded">PDF, XLSX, XLS, CSV, NPCI/IMPS RAW</span>
        </div>

        <!-- Drag & Drop Zone -->
        <div id="dropZone" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)" ondrop="handleFileDrop(event)" class="border-2 border-dashed border-outline-variant hover:border-secondary transition-colors rounded-lg p-6 flex flex-col items-center justify-center bg-surface-container-low/40 cursor-pointer text-center relative">
          <input class="absolute inset-0 opacity-0 cursor-pointer w-full h-full" id="fileUploadInput" onchange="handleFileUpload(event)" type="file" multiple accept=".csv,.xlsx,.xls,.pdf,.json"/>
          <div class="w-10 h-10 rounded-full bg-surface-container flex items-center justify-center text-secondary mb-2">
            <span class="material-symbols-outlined text-[24px]">cloud_upload</span>
          </div>
          <div class="font-headline-sm text-[13px] font-bold text-on-surface">Drag & Drop Bank Statements (PDF, CSV, Excel) or <span class="text-secondary underline">Browse Files</span></div>
          <p class="font-body-sm text-[11px] text-on-surface-variant max-w-md mt-1">Core Banking Engines: SBI, HDFC, ICICI, Kotak, Axis, PNB, Canara, BoB, Yes Bank, Paytm PB.</p>
          <div class="flex flex-wrap items-center justify-center gap-1.5 font-label-code-sm text-[10px] text-on-surface-variant mt-2">
            <span class="px-2 py-0.5 bg-surface-container-lowest rounded border border-outline-variant">Auto-detect Header Mapping</span>
            <span class="px-2 py-0.5 bg-surface-container-lowest rounded border border-outline-variant">Split Multiline Ledger Lines</span>
            <span class="px-2 py-0.5 bg-surface-container-lowest rounded border border-outline-variant">UPI VPA Parser Included</span>
          </div>
        </div>

        <!-- Controls: Decryption Password & Normalisation Trigger -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mt-3 pt-3 border-t border-outline-variant">
          <div>
            <label class="font-label-caps text-[10px] text-on-surface flex items-center gap-1 mb-1" for="pdfPasswordInput">
              <span class="material-symbols-outlined text-[13px] text-on-surface-variant">lock</span>
              <span>STATEMENT PASSWORD / DECRYPTION KEY (IF ENCRYPTED)</span>
            </label>
            <input class="w-full h-8 px-2.5 bg-surface-container-low border border-outline-variant rounded font-label-code-sm text-[11px] text-on-surface focus:outline-none focus:border-secondary" id="pdfPasswordInput" placeholder="e.g. PAN + DOB (HDFC/SBI standard format)" type="password" value="PANJAIPUR9088"/>
          </div>
          <div class="flex flex-col justify-end">
            <button onclick="processIngestionBatch()" class="w-full h-8 bg-primary hover:bg-slate-800 text-white rounded font-label-caps text-[11px] tracking-wider flex items-center justify-center gap-1.5 transition-colors shadow-sm">
              <span class="material-symbols-outlined text-[15px] text-amber-400">psychology</span>
              <span>PROCESS & FORENSICALLY NORMALISE</span>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Right Column: Reconciliation Engine Status & Synthetic Demo Helpers -->
    <div class="lg:col-span-4 flex flex-col gap-3">
      <!-- Reconciliation Health Meter -->
      <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant">
        <div class="flex items-center justify-between pb-1.5 border-b border-outline-variant mb-2">
          <div class="flex items-center gap-1">
            <span class="material-symbols-outlined text-secondary text-[16px]">tune</span>
            <span class="font-label-caps text-[11px] font-bold text-on-surface">RECONCILIATION AUDIT</span>
          </div>
          <span id="reconciliationHealthBadge" class="font-label-code-sm text-[10px] px-1.5 py-0.2 rounded bg-emerald-100 text-emerald-800 font-bold">1 DISCREPANCY</span>
        </div>
        <div class="p-2 bg-surface-container-low rounded font-label-code-sm text-[11px] space-y-1">
          <div class="text-[10px] font-bold text-slate-700">MATHEMATICAL BALANCE EQUATION:</div>
          <div class="p-1 bg-surface-container-lowest rounded border border-outline-variant text-slate-800 text-[10px]">
            <code>Opening Bal + Total Credits - Total Debits = Closing Bal</code>
          </div>
          <div id="reconciliationStatusText" class="text-[11px] text-slate-700 pt-1">
            • Kotak (Acc A): <span class="text-emerald-700 font-bold">RECONCILED ✓</span><br>
            • ICICI (Acc B): <span class="text-emerald-700 font-bold">RECONCILED ✓</span><br>
            • SBI (Acc C): <span class="text-red-700 font-bold">MISMATCH DETECTED (Row 4) ⚠</span>
          </div>
        </div>
      </div>

      <!-- Sample Statements Ready for Download/Testing -->
      <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant">
        <div class="font-label-caps text-[10px] font-bold text-on-surface uppercase mb-1.5">Download Synthetic Hackathon Statements</div>
        <div class="space-y-1.5 text-[11px]">
          <a href="sample_data/kotak_account_A_statement.csv" download class="p-1.5 bg-surface-container hover:bg-surface-container-high rounded border border-outline-variant flex items-center justify-between text-secondary">
            <span class="font-mono">kotak_account_A_statement.csv</span>
            <span class="material-symbols-outlined text-[15px]">download</span>
          </a>
          <a href="sample_data/icici_account_B_statement.csv" download class="p-1.5 bg-surface-container hover:bg-surface-container-high rounded border border-outline-variant flex items-center justify-between text-secondary">
            <span class="font-mono">icici_account_B_statement.csv</span>
            <span class="material-symbols-outlined text-[15px]">download</span>
          </a>
          <a href="sample_data/sbi_account_C_statement_inconsistent.csv" download class="p-1.5 bg-surface-container hover:bg-surface-container-high rounded border border-outline-variant flex items-center justify-between text-error font-medium">
            <span class="font-mono">sbi_inconsistent_statement.csv</span>
            <span class="material-symbols-outlined text-[15px]">download</span>
          </a>
        </div>
      </div>
    </div>
  </div>

  <!-- Reconciled Statement Ingestion Table -->
  <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant">
    <div class="flex items-center justify-between pb-2 border-b border-outline-variant mb-2">
      <div class="flex items-center gap-2">
        <span class="font-headline-sm text-[14px] font-bold text-on-surface">Normalized Transaction Ledger (Batch Review)</span>
        <span class="px-1.5 py-0.2 bg-surface-container text-on-surface-variant font-label-code-sm text-[10px] rounded" id="ingestedCountBadge">13 TRANSACTIONS</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="text-[11px] text-on-surface-variant">Reconciliation:</span>
        <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-amber-100 text-amber-900 border border-amber-300">1 Line Discrepancy Flagged</span>
      </div>
    </div>
    <div class="overflow-x-auto">
      <table class="w-full text-left text-[11px]">
        <thead class="bg-surface-container text-on-surface-variant font-label-caps text-[9px]">
          <tr>
            <th class="py-1.5 px-2">TXN ID / Date</th>
            <th class="py-1.5 px-2">Bank / Account</th>
            <th class="py-1.5 px-2">Counterparty</th>
            <th class="py-1.5 px-2">UTR Reference</th>
            <th class="py-1.5 px-2 text-right">Debit (₹)</th>
            <th class="py-1.5 px-2 text-right">Credit (₹)</th>
            <th class="py-1.5 px-2 text-right">Running Bal (₹)</th>
            <th class="py-1.5 px-2 text-center">Status / Hash</th>
          </tr>
        </thead>
        <tbody id="ingestedTxnTbody" class="divide-y divide-outline-variant/60 font-mono">
          <!-- Rendered dynamically -->
        </tbody>
      </table>
    </div>
  </div>
</section>
"""

VIEW_TRANSACTIONS = """
<section id="view-transaction-explorer" class="view-panel hidden">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 pb-2 mb-3 border-b border-outline-variant">
    <div>
      <div class="flex items-center gap-1.5">
        <span class="px-2 py-0.5 rounded bg-primary-container text-surface-container-high font-label-code-sm text-[11px]">EVIDENCE LEDGER</span>
        <span class="text-secondary font-label-code-sm text-[11px] font-bold">• 100% AUDITABLE</span>
      </div>
      <h1 class="font-headline-lg text-[18px] font-bold text-on-surface tracking-tight mt-0.5">Forensic Transaction Explorer</h1>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="exportTransactionsCSV()" class="flex items-center gap-1 px-3 py-1.5 bg-surface-container-low hover:bg-surface-container text-on-surface rounded font-label-caps text-[11px] tracking-wider transition-colors border border-outline-variant">
        <span class="material-symbols-outlined text-[15px]">file_download</span>
        <span>EXPORT CSV</span>
      </button>
      <button onclick="navigateTo('money-trail-analysis')" class="flex items-center gap-1 px-3 py-1.5 bg-secondary text-white rounded font-label-caps text-[11px] font-bold tracking-wider hover:bg-blue-700 transition-colors">
        <span class="material-symbols-outlined text-[15px]">hub</span>
        <span>VIEW IN MONEY TRAIL</span>
      </button>
    </div>
  </div>

  <!-- Filter Ribbon -->
  <div class="bg-surface-container-lowest rounded-lg p-2.5 shadow-sm border border-outline-variant mb-3 grid grid-cols-1 md:grid-cols-5 gap-2 text-[12px]">
    <div>
      <label class="font-label-caps text-[9px] text-on-surface-variant uppercase">Search Filter</label>
      <input id="txnSearchFilter" onkeyup="filterTransactionsTable()" type="text" placeholder="Filter UTR / Account / Narration..." class="w-full h-7 px-2 bg-surface-container-low border border-outline-variant rounded font-mono text-[11px]"/>
    </div>
    <div>
      <label class="font-label-caps text-[9px] text-on-surface-variant uppercase">Bank Filter</label>
      <select id="txnBankFilter" onchange="filterTransactionsTable()" class="w-full h-7 px-2 bg-surface-container-low border border-outline-variant rounded text-[11px]">
        <option value="ALL">All Banks (45)</option>
        <option value="Kotak">Kotak Mahindra</option>
        <option value="ICICI">ICICI Bank</option>
        <option value="SBI">State Bank of India</option>
        <option value="Axis">Axis Bank</option>
        <option value="HDFC">HDFC Bank</option>
        <option value="Yes">Yes Bank</option>
      </select>
    </div>
    <div>
      <label class="font-label-caps text-[9px] text-on-surface-variant uppercase">Direction</label>
      <select id="txnDirectionFilter" onchange="filterTransactionsTable()" class="w-full h-7 px-2 bg-surface-container-low border border-outline-variant rounded text-[11px]">
        <option value="ALL">Debits & Credits</option>
        <option value="CREDIT">Credits Only</option>
        <option value="DEBIT">Debits Only</option>
      </select>
    </div>
    <div>
      <label class="font-label-caps text-[9px] text-on-surface-variant uppercase">Risk Classification</label>
      <select id="txnRiskFilter" onchange="filterTransactionsTable()" class="w-full h-7 px-2 bg-surface-container-low border border-outline-variant rounded text-[11px]">
        <option value="ALL">All Classifications</option>
        <option value="VICTIM">Victim Deposit</option>
        <option value="MULE">Mule Layering</option>
        <option value="TERMINAL">Terminal Residual</option>
        <option value="EXCLUDED">Pre-Fund Excluded</option>
      </select>
    </div>
    <div class="flex items-end">
      <button onclick="resetTxnFilters()" class="w-full h-7 bg-surface-container hover:bg-surface-container-high rounded text-on-surface font-label-caps text-[10px] tracking-wider uppercase transition-colors">
        RESET FILTERS
      </button>
    </div>
  </div>

  <!-- Transactions Table -->
  <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant">
    <div class="overflow-x-auto">
      <table class="w-full text-left text-[11px]">
        <thead class="bg-surface-container text-on-surface-variant font-label-caps text-[9px]">
          <tr>
            <th class="py-1.5 px-2">TXN ID</th>
            <th class="py-1.5 px-2">Timestamp (IST)</th>
            <th class="py-1.5 px-2">Bank & A/C</th>
            <th class="py-1.5 px-2">Direction</th>
            <th class="py-1.5 px-2 text-right">Amount (₹)</th>
            <th class="py-1.5 px-2">Counterparty</th>
            <th class="py-1.5 px-2">UTR Reference</th>
            <th class="py-1.5 px-2">Classification</th>
            <th class="py-1.5 px-2 text-center">Inspect</th>
          </tr>
        </thead>
        <tbody id="fullTxnTbody" class="divide-y divide-outline-variant/60 font-mono">
          <!-- Rendered dynamically -->
        </tbody>
      </table>
    </div>
  </div>
</section>
"""

VIEW_MULE_DETECTION = """
<section id="view-mule-account-detection" class="view-panel hidden">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 pb-2 mb-3 border-b border-outline-variant">
    <div>
      <div class="flex items-center gap-1.5">
        <span class="px-2 py-0.5 rounded bg-primary-container text-surface-container-high font-label-code-sm text-[11px]">BHARAT-FINCYBER ML ENGINE</span>
        <span class="text-secondary font-label-code-sm text-[11px] font-bold">• 8 EXPLAINABLE RULES ACTIVE</span>
      </div>
      <h1 class="font-headline-lg text-[18px] font-bold text-on-surface tracking-tight mt-0.5">Mule Account Intelligence & Explainable Detection Engine</h1>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="navigateTo('freeze-priority-engine')" class="flex items-center gap-1.5 px-3 py-1.5 bg-error text-white rounded font-label-caps text-[11px] font-bold tracking-wider hover:bg-red-700 shadow-sm transition-colors">
        <span class="material-symbols-outlined text-[15px]">lock_clock</span>
        <span>FORWARD TO FREEZE ENGINE</span>
      </button>
    </div>
  </div>

  <!-- KPI Pillars Ribbon -->
  <div class="grid grid-cols-1 md:grid-cols-5 gap-2.5 mb-3">
    <div class="bg-surface-container-lowest p-2.5 rounded shadow-sm border border-outline-variant">
      <div class="font-label-caps text-[10px] text-on-surface-variant">TOTAL ACCOUNTS SCANNED</div>
      <div class="font-headline-lg text-[20px] font-bold text-on-surface mt-1">15 <span class="text-[11px] font-normal text-on-surface-variant">Nodes</span></div>
      <div class="font-label-code-sm text-[10px] text-secondary">100% Ingested Coverage</div>
    </div>
    <div class="bg-surface-container-lowest p-2.5 rounded shadow-sm border-l-4 border-error border border-outline-variant">
      <div class="font-label-caps text-[10px] text-error font-bold">HIGH RISK MULES (>70)</div>
      <div class="font-headline-lg text-[20px] font-bold text-error mt-1">6 <span class="text-[11px] font-normal text-error">Identified</span></div>
      <div class="font-label-code-sm text-[10px] text-error">Actionable for Freeze</div>
    </div>
    <div class="bg-surface-container-lowest p-2.5 rounded shadow-sm border border-outline-variant">
      <div class="font-label-caps text-[10px] text-on-surface-variant">RAPID IN-OUT TRANSFERS</div>
      <div class="font-headline-lg text-[20px] font-bold text-on-surface mt-1">4 <span class="text-[11px] font-normal text-on-surface-variant">Accounts</span></div>
      <div class="font-label-code-sm text-[10px] text-amber-600">Dwell time < 45 mins</div>
    </div>
    <div class="bg-surface-container-lowest p-2.5 rounded shadow-sm border border-outline-variant">
      <div class="font-label-caps text-[10px] text-on-surface-variant">CROSS-CASE ENTITIES</div>
      <div class="font-headline-lg text-[20px] font-bold text-on-surface mt-1">2 <span class="text-[11px] font-normal text-on-surface-variant">Matches</span></div>
      <div class="font-label-code-sm text-[10px] text-secondary">Linked to FIR 072 & 119</div>
    </div>
    <div class="bg-surface-container-lowest p-2.5 rounded shadow-sm border border-outline-variant">
      <div class="font-label-caps text-[10px] text-on-surface-variant">AVG TRANSIT DWELL TIME</div>
      <div class="font-headline-lg text-[20px] font-bold text-on-surface mt-1">28.4 <span class="text-[11px] font-normal text-on-surface-variant">MINS</span></div>
      <div class="font-label-code-sm text-[10px] text-secondary font-medium">Layering Funnel Detected</div>
    </div>
  </div>

  <!-- Mule Table & Explainability Preview Split View -->
  <div class="grid grid-cols-1 lg:grid-cols-12 gap-3">
    <!-- Left: Flagged Mules Directory -->
    <div class="lg:col-span-8 flex flex-col gap-2">
      <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant">
        <div class="flex items-center justify-between pb-2 border-b border-outline-variant mb-2">
          <div class="flex items-center gap-1.5">
            <span class="material-symbols-outlined text-secondary text-[18px]">account_tree</span>
            <span class="font-headline-sm text-[14px] font-bold text-on-surface">Flagged Mule Account Registry</span>
          </div>
          <span class="text-[11px] text-on-surface-variant font-mono">Click any row to open Deep Explainability Drawer</span>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full text-left text-[11px]">
            <thead class="bg-surface-container text-on-surface-variant font-label-caps text-[9px]">
              <tr>
                <th class="py-1.5 px-2">Account No</th>
                <th class="py-1.5 px-2">Bank & Branch</th>
                <th class="py-1.5 px-2">Holder / Entity</th>
                <th class="py-1.5 px-2 text-center">Composite Score</th>
                <th class="py-1.5 px-2">Triggered Rules</th>
                <th class="py-1.5 px-2 text-right">Parked Residual</th>
                <th class="py-1.5 px-2 text-center">Inspect</th>
              </tr>
            </thead>
            <tbody id="mulesListTbody" class="divide-y divide-outline-variant/60 font-mono">
              <!-- Rendered dynamically -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Right: Sticky Explainability Forensics Panel -->
    <div class="lg:col-span-4 flex flex-col gap-2">
      <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant sticky top-20" id="muleExplainabilityContainer">
        <div class="flex items-center justify-between pb-2 border-b border-outline-variant mb-2">
          <div class="flex items-center gap-1">
            <span class="material-symbols-outlined text-amber-500 text-[18px]">psychology</span>
            <span class="font-headline-sm text-[13px] font-bold text-on-surface">Rule-Level Explainability</span>
          </div>
          <span class="px-1.5 py-0.2 bg-surface-container text-secondary text-[9px] font-bold font-mono rounded">100% EXPLAINABLE</span>
        </div>
        <div id="muleExplainabilityBody" class="space-y-2 text-[12px]">
          <div class="p-3 text-center text-on-surface-variant font-mono text-[11px]">
            Select an account from the table to inspect its exact rule weights, mathematical contributions, and cited transaction rows.
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

VIEW_MONEY_TRAIL = """
<section id="view-money-trail-analysis" class="view-panel hidden">
  <!-- Top Hero Header & Algorithm Controls -->
  <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant mb-3">
    <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-2 pb-2 border-b border-outline-variant mb-2">
      <div class="flex items-center gap-2">
        <div class="w-8 h-8 rounded bg-amber-500/10 text-amber-500 flex items-center justify-center font-bold">
          <span class="material-symbols-outlined text-[20px]">hub</span>
        </div>
        <div>
          <div class="flex items-center gap-1.5">
            <span class="font-headline-sm text-[15px] font-bold text-on-surface">Chronological Money-Trail Tracing Engine</span>
            <span class="px-1.5 py-0.2 bg-amber-500 text-slate-900 font-label-caps text-[9px] font-bold rounded">HERO FEATURE</span>
          </div>
          <div class="font-body-sm text-[11px] text-on-surface-variant">
            Reconstructing fund journeys • Strict temporal ordering • Anti-double counting conservation
          </div>
        </div>
      </div>

      <!-- Controls: UTR Input, FIFO/Proportional Toggle, Hop Filter -->
      <div class="flex flex-wrap items-center gap-2 text-[11px]">
        <div class="flex items-center gap-1 bg-surface-container px-2 py-1 rounded border border-outline-variant font-mono">
          <span class="text-on-surface-variant text-[10px]">VICTIM UTR:</span>
          <input id="traceUtrInput" type="text" value="UTR-2024-RJ-894102" class="bg-transparent font-bold text-secondary focus:outline-none w-36 uppercase"/>
          <button onclick="executeMoneyTrailTrace()" class="px-1.5 py-0.5 bg-secondary text-white rounded text-[10px] font-sans font-bold hover:bg-blue-700">TRACE</button>
        </div>

        <!-- Attribution Algorithm Switcher -->
        <div class="flex items-center gap-1 bg-surface-container-low px-2 py-1 rounded border border-outline-variant">
          <span class="text-on-surface-variant text-[10px] font-label-caps">ATTRIBUTION:</span>
          <button id="btnFifoMode" onclick="setAttributionMode('FIFO')" class="px-2 py-0.5 rounded text-[10px] font-bold bg-secondary text-white">FIFO</button>
          <button id="btnPropMode" onclick="setAttributionMode('PROPORTIONAL')" class="px-2 py-0.5 rounded text-[10px] font-bold text-on-surface-variant hover:bg-surface-container">PROPORTIONAL</button>
        </div>

        <!-- Layer Hop Filter -->
        <select id="trailHopFilter" onchange="filterTrailHops(this.value)" class="h-7 px-2 bg-surface-container border border-outline-variant rounded font-label-code-sm text-[10px]">
          <option value="ALL">All Layers (1 to 3)</option>
          <option value="1">Layer 1 Only (Collector)</option>
          <option value="2">Layer 2 Only (Layering)</option>
          <option value="3">Layer 3 Only (Sinks/Parked)</option>
        </select>

        <button onclick="exportGraphImage()" class="px-2 py-1 bg-surface-container hover:bg-surface-container-high border border-outline-variant rounded font-label-caps text-[10px] tracking-wider transition-colors flex items-center gap-1">
          <span class="material-symbols-outlined text-[13px]">image</span>
          <span>EXPORT GRAPH</span>
        </button>
      </div>
    </div>

    <!-- Conservation Audit & Fund Balance Bar -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-2 pt-1 font-mono text-[11px] bg-surface-container-low p-2 rounded border border-outline-variant">
      <div>
        <span class="text-on-surface-variant text-[10px]">VICTIM INFLOW:</span>
        <div class="text-[13px] font-bold text-on-surface" id="trailVictimInflow">₹1,00,000</div>
      </div>
      <div>
        <span class="text-on-surface-variant text-[10px]">ESTIMATED RESIDUAL EXPOSURE:</span>
        <div class="text-[13px] font-bold text-error" id="trailResidualExposure">₹1,00,000 (100%)</div>
      </div>
      <div>
        <span class="text-on-surface-variant text-[10px]">EXTERNAL UNTRACKED OUTFLOW:</span>
        <div class="text-[13px] font-bold text-slate-700" id="trailUntrackedOutflow">₹0 (0%)</div>
      </div>
      <div>
        <span class="text-on-surface-variant text-[10px]">CONSERVATION CHECK:</span>
        <div class="text-[12px] font-bold text-emerald-700" id="trailConservationStatus">BALANCED ✓ (₹0 Discrepancy)</div>
      </div>
    </div>
  </div>

  <!-- Interactive Network Graph Canvas + Node Details Inspector -->
  <div class="grid grid-cols-1 lg:grid-cols-12 gap-3 mb-3">
    <!-- Graph Canvas Container (Col 9) -->
    <div class="lg:col-span-9 flex flex-col gap-2">
      <div class="bg-surface-container-lowest rounded-lg shadow-sm border border-outline-variant overflow-hidden relative">
        <!-- Floating Canvas Toolbar -->
        <div class="absolute top-3 left-3 z-10 flex items-center gap-1.5 bg-white/95 backdrop-blur border border-outline-variant px-2.5 py-1 rounded shadow-sm text-[11px] font-mono">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          <span class="font-bold text-slate-800">CYTOSCAPE.JS NETWORK GRAPH</span>
          <span class="text-slate-400">|</span>
          <button onclick="resetGraphLayout()" class="text-secondary hover:underline flex items-center gap-0.5">
            <span class="material-symbols-outlined text-[13px]">refresh</span> Reset Layout
          </button>
          <span class="text-slate-400">|</span>
          <button onclick="zoomGraphIn()" class="text-slate-700 hover:text-black font-bold px-1">+</button>
          <button onclick="zoomGraphOut()" class="text-slate-700 hover:text-black font-bold px-1">-</button>
        </div>

        <!-- Legend Overlay -->
        <div class="absolute bottom-3 left-3 z-10 flex flex-wrap items-center gap-2 bg-white/95 backdrop-blur border border-outline-variant px-2 py-1 rounded shadow-sm text-[10px] font-mono">
          <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span> Victim</span>
          <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-amber-500"></span> Layer 1</span>
          <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-purple-600"></span> Layer 2</span>
          <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-red-600"></span> Layer 3 Freeze Target</span>
        </div>

        <!-- Cytoscape Graph Element -->
        <div id="cyMoneyTrail" class="w-full h-[540px] bg-slate-50 cursor-grab active:cursor-grabbing"></div>
      </div>

      <!-- Timeline Playback Slider -->
      <div class="bg-surface-container-lowest rounded-lg p-2.5 shadow-sm border border-outline-variant flex items-center justify-between gap-3 text-[11px]">
        <div class="flex items-center gap-2">
          <button id="trailPlayBtn" onclick="toggleTimelinePlayback()" class="w-7 h-7 rounded bg-secondary hover:bg-blue-700 text-white flex items-center justify-center">
            <span class="material-symbols-outlined text-[16px]">play_arrow</span>
          </button>
          <span class="font-label-caps text-[10px] text-on-surface-variant font-bold">TIMELINE PLAYBACK:</span>
        </div>
        <input id="timelinePlaybackSlider" oninput="handleTimelineSlider(this.value)" type="range" min="0" max="6" value="6" class="flex-1 cursor-pointer accent-secondary"/>
        <div class="font-mono text-[10px] text-on-surface" id="timelineStepLabel">Step 6/6: Complete Multi-Hop Trail</div>
      </div>
    </div>

    <!-- Node Inspector Drawer (Col 3) -->
    <div class="lg:col-span-3 flex flex-col gap-2">
      <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant sticky top-20" id="trailNodeInspector">
        <div class="flex items-center justify-between pb-2 border-b border-outline-variant mb-2">
          <div class="flex items-center gap-1">
            <span class="material-symbols-outlined text-secondary text-[16px]">info</span>
            <span class="font-headline-sm text-[13px] font-bold text-on-surface">Node Inspector</span>
          </div>
          <span class="font-label-code-sm text-[9px] text-on-surface-variant bg-surface-container px-1 rounded">LIVE SELECTION</span>
        </div>
        <div id="trailNodeInspectorBody" class="space-y-2 text-[11px]">
          <div class="p-4 text-center text-on-surface-variant font-mono">
            Click on any account or victim node in the graph above to inspect its balance, residual exposure, counterparty records, and Section 91 freeze priority.
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

print("Views part 2 loaded.")
