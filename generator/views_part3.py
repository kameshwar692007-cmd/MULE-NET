# generator/views_part3.py
# HTML for Freeze Priority, Cyber Intel, Unified Graph, Cross-Case, Timeline, Reports, Lawful Notices, Audit, Settings, Modals

VIEW_FREEZE_PRIORITY = """
<section id="view-freeze-priority-engine" class="view-panel hidden">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 pb-2 mb-3 border-b border-outline-variant">
    <div>
      <div class="flex items-center gap-1.5">
        <span class="px-2 py-0.5 rounded bg-error/10 text-error font-label-code-sm text-[11px] font-bold">OPERATIONAL ENFORCEMENT</span>
        <span class="text-secondary font-label-code-sm text-[11px] font-bold">• DYNAMIC RESIDUAL SCORING</span>
      </div>
      <h1 class="font-headline-lg text-[18px] font-bold text-on-surface tracking-tight mt-0.5">Freeze-Priority Intelligence & Action Engine</h1>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="bulkDraftFreezeNotices()" class="flex items-center gap-1.5 px-3 py-1.5 bg-error text-white rounded font-label-caps text-[11px] font-bold tracking-wider hover:bg-red-700 shadow-sm transition-opacity">
        <span class="material-symbols-outlined text-[15px]">gavel</span>
        <span>BULK DRAFT FREEZE DIRECTIVES (6)</span>
      </button>
      <button onclick="exportPriorityListExcel()" class="flex items-center gap-1.5 px-3 py-1.5 bg-surface-container-low hover:bg-surface-container text-on-surface rounded font-label-caps text-[11px] tracking-wider border border-outline-variant">
        <span class="material-symbols-outlined text-[15px]">download</span>
        <span>EXPORT PRIORITY LIST</span>
      </button>
    </div>
  </div>

  <!-- Statutory Disclaimer Notice -->
  <div class="p-2.5 bg-amber-500/10 border-l-4 border-amber-500 text-amber-900 rounded-r text-[11px] mb-3 flex items-start gap-2">
    <span class="material-symbols-outlined text-[18px] text-amber-600 mt-0.5 shrink-0">policy</span>
    <div>
      <strong class="font-semibold">STATUTORY INVESTIGATIVE RECOMMENDATION ONLY:</strong>
      Residual exposure is mathematically estimated from uploaded core banking statements and chronological trace paths. It does not constitute a real-time live CBS balance inquiry. Any debit freeze instruction requires an authorized warrant / Section 91 CrPC notice signed by an Investigating Officer.
    </div>
  </div>

  <!-- Freeze Priority Table -->
  <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant">
    <div class="flex items-center justify-between pb-2 border-b border-outline-variant mb-2">
      <div class="flex items-center gap-2">
        <span class="font-headline-sm text-[14px] font-bold text-on-surface">Account Priority Hierarchy (Ranked by Residual Exposure & Risk)</span>
        <span class="px-1.5 py-0.2 bg-error/10 text-error font-mono text-[10px] font-bold rounded">₹1,00,000 TOTAL ACTIONABLE</span>
      </div>
      <div class="flex items-center gap-2 text-[11px]">
        <label class="text-on-surface-variant">Sort by:</label>
        <select onchange="sortPriorityTable(this.value)" class="h-6 px-1.5 bg-surface-container border border-outline-variant rounded font-mono text-[10px]">
          <option value="residual">Residual Exposure (High to Low)</option>
          <option value="risk">Mule Risk Score (High to Low)</option>
          <option value="velocity">Velocity Factor</option>
        </select>
      </div>
    </div>
    <div class="overflow-x-auto">
      <table class="w-full text-left text-[11px]">
        <thead class="bg-surface-container text-on-surface-variant font-label-caps text-[9px]">
          <tr>
            <th class="py-1.5 px-2">Rank</th>
            <th class="py-1.5 px-2">Account Number</th>
            <th class="py-1.5 px-2">Bank & Branch</th>
            <th class="py-1.5 px-2">Account Holder</th>
            <th class="py-1.5 px-2 text-center">Priority</th>
            <th class="py-1.5 px-2 text-right">Traced Inflow (₹)</th>
            <th class="py-1.5 px-2 text-right">Traced Outflow (₹)</th>
            <th class="py-1.5 px-2 text-right font-bold text-error">Residual Exposure (₹)</th>
            <th class="py-1.5 px-2 text-center">Risk Score</th>
            <th class="py-1.5 px-2">Cross-Case Status</th>
            <th class="py-1.5 px-2 text-center">Action</th>
          </tr>
        </thead>
        <tbody id="priorityTableTbody" class="divide-y divide-outline-variant/60 font-mono">
          <!-- Rendered dynamically -->
        </tbody>
      </table>
    </div>
  </div>
</section>
"""

VIEW_CYBER_INTEL = """
<section id="view-domain-and-ip-intelligence" class="view-panel hidden">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 pb-2 mb-3 border-b border-outline-variant">
    <div>
      <div class="flex items-center gap-1.5">
        <span class="px-2 py-0.5 rounded bg-primary-container text-surface-container-high font-label-code-sm text-[11px]">CYBER OSINT ENGINE</span>
        <span class="text-secondary font-label-code-sm text-[11px] font-bold">• PASSIVE RECONNAISSANCE ONLY</span>
      </div>
      <h1 class="font-headline-lg text-[18px] font-bold text-on-surface tracking-tight mt-0.5">Domain, DNS & IP Infrastructure Intelligence</h1>
    </div>
    <div class="flex items-center gap-2">
      <span class="px-2 py-1 bg-surface-container-low rounded border border-outline-variant font-mono text-[10px] text-on-surface-variant">
        NO ACTIVE SCANNING • STRICT LEGAL COMPLIANCE
      </span>
    </div>
  </div>

  <!-- Search Ribbon: Domain or IP Lookup -->
  <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant mb-3 flex flex-col md:flex-row items-center gap-2">
    <div class="flex-1 flex items-center gap-2 w-full">
      <div class="relative flex-1">
        <span class="material-symbols-outlined absolute left-2 top-2 text-outline text-[16px]">language</span>
        <input id="infraLookupInput" type="text" placeholder="Enter Domain or IPv4 (e.g. secure-invest-rajasthan.xyz or 185.220.101.45)..." value="secure-invest-rajasthan.xyz" class="w-full h-8 pl-8 pr-2.5 bg-surface-container-low border border-outline-variant rounded font-mono text-[11px]"/>
      </div>
      <button onclick="performInfraLookup()" class="h-8 px-4 bg-secondary hover:bg-blue-700 text-white rounded font-label-caps text-[11px] font-bold tracking-wider transition-colors">
        ENRICH INTELLIGENCE
      </button>
    </div>
    <div class="flex items-center gap-1 text-[10px] text-on-surface-variant font-mono">
      <span>Quick demo:</span>
      <button onclick="lookupInfraDemo('secure-invest-rajasthan.xyz')" class="text-secondary underline">secure-invest-rajasthan.xyz</button>
      <span>•</span>
      <button onclick="lookupInfraDemo('kyc-verify-portal.net')" class="text-secondary underline">kyc-verify-portal.net</button>
      <span>•</span>
      <button onclick="lookupInfraDemo('185.220.101.45')" class="text-secondary underline">185.220.101.45</button>
    </div>
  </div>

  <!-- Infrastructure Enrichment Display -->
  <div class="grid grid-cols-1 lg:grid-cols-12 gap-3 mb-3">
    <!-- Left: Infrastructure Entity Details -->
    <div class="lg:col-span-7 flex flex-col gap-3">
      <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant" id="infraDetailsContainer">
        <!-- Rendered dynamically -->
      </div>
    </div>

    <!-- Right: Visual Network Hierarchy Diagram (Domain -> DNS -> IP -> ASN -> Hosting) -->
    <div class="lg:col-span-5 flex flex-col gap-3">
      <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant">
        <div class="flex items-center justify-between pb-1.5 border-b border-outline-variant mb-2">
          <span class="font-headline-sm text-[13px] font-bold text-on-surface">Digital Infrastructure Chain</span>
          <span class="font-mono text-[9px] text-secondary">STRUCTURAL MAPPING</span>
        </div>
        <div id="infraChainVisual" class="space-y-2 font-mono text-[11px]">
          <!-- Rendered dynamically -->
        </div>
      </div>
    </div>
  </div>
</section>
"""

VIEW_RELATIONSHIP_GRAPH = """
<section id="view-relationship-graph" class="view-panel hidden">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 pb-2 mb-3 border-b border-outline-variant">
    <div>
      <div class="flex items-center gap-1.5">
        <span class="px-2 py-0.5 rounded bg-primary-container text-surface-container-high font-label-code-sm text-[11px]">CROSS-DOMAIN FUSION</span>
        <span class="text-secondary font-label-code-sm text-[11px] font-bold">• FINANCIAL & DIGITAL GRAPH</span>
      </div>
      <h1 class="font-headline-lg text-[18px] font-bold text-on-surface tracking-tight mt-0.5">Unified Financial & Digital Relationship Graph</h1>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="resetRelationshipGraphLayout()" class="flex items-center gap-1 px-3 py-1.5 bg-surface-container-low hover:bg-surface-container text-on-surface rounded font-label-caps text-[11px] tracking-wider border border-outline-variant">
        <span class="material-symbols-outlined text-[15px]">refresh</span>
        <span>RESET GRAPH LAYOUT</span>
      </button>
      <button onclick="exportRelationshipGraphImage()" class="flex items-center gap-1 px-3 py-1.5 bg-secondary text-white rounded font-label-caps text-[11px] font-bold tracking-wider hover:bg-blue-700">
        <span class="material-symbols-outlined text-[15px]">image</span>
        <span>EXPORT PNG</span>
      </button>
    </div>
  </div>

  <div class="bg-surface-container-lowest rounded-lg shadow-sm border border-outline-variant overflow-hidden relative mb-3">
    <div class="absolute top-3 left-3 z-10 flex flex-wrap items-center gap-2 bg-white/95 backdrop-blur border border-outline-variant px-2.5 py-1 rounded shadow-sm text-[10px] font-mono">
      <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span> Case FIR</span>
      <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-emerald-600"></span> Victim</span>
      <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-amber-500"></span> Bank Account</span>
      <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-purple-600"></span> Domain</span>
      <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-red-600"></span> IP / ASN</span>
    </div>
    <div id="cyRelationshipGraph" class="w-full h-[580px] bg-slate-50 cursor-grab active:cursor-grabbing"></div>
  </div>
</section>
"""

VIEW_CROSS_CASE = """
<section id="view-cross-case-linking" class="view-panel hidden">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 pb-2 mb-3 border-b border-outline-variant">
    <div>
      <div class="flex items-center gap-1.5">
        <span class="px-2 py-0.5 rounded bg-primary-container text-surface-container-high font-label-code-sm text-[11px]">CROSS-JURISDICTION SYNDICATE DISCOVERY</span>
        <span class="text-secondary font-label-code-sm text-[11px] font-bold">• 3 ACTIVE STATE FIRS</span>
      </div>
      <h1 class="font-headline-lg text-[18px] font-bold text-on-surface tracking-tight mt-0.5">Cross-Case Intelligence & Entity Correlator</h1>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="runCrossCaseCorrelationScan()" class="flex items-center gap-1.5 px-3 py-1.5 bg-amber-500 hover:bg-amber-600 text-slate-900 rounded font-label-caps text-[11px] font-bold tracking-wider shadow-sm transition-all">
        <span class="material-symbols-outlined text-[15px]">refresh</span>
        <span>RUN RE-CORRELATION SCAN</span>
      </button>
    </div>
  </div>

  <!-- Heat List of Multi-Case Syndicate Entities -->
  <div class="grid grid-cols-1 md:grid-cols-3 gap-3 mb-3">
    <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant border-l-4 border-error">
      <div class="font-label-caps text-[10px] text-error font-bold">SHARED BANK ACCOUNT (STRONG MATCH)</div>
      <div class="font-mono text-[14px] font-bold text-on-surface mt-1">Axis Bank: 1192837465</div>
      <div class="text-[11px] text-on-surface-variant">Suresh Traders • Shared across <strong class="text-on-surface">FIR 104 & FIR 072</strong></div>
      <div class="mt-2 text-[10px] font-mono text-secondary">Combined Defrauded Pool: ₹4,50,000</div>
    </div>
    <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant border-l-4 border-amber-500">
      <div class="font-label-caps text-[10px] text-amber-600 font-bold">SHARED PHISHING PORTAL (DIRECT MATCH)</div>
      <div class="font-mono text-[14px] font-bold text-on-surface mt-1">kyc-verify-portal.net</div>
      <div class="text-[11px] text-on-surface-variant">Used in Telegram Scam & Jodhpur Job Phishing</div>
      <div class="mt-2 text-[10px] font-mono text-secondary">Cloudflare Proxy Origin</div>
    </div>
    <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant border-l-4 border-purple-500">
      <div class="font-label-caps text-[10px] text-purple-600 font-bold">SHARED BULLETPROOF IP (CONTEXTUAL)</div>
      <div class="font-mono text-[14px] font-bold text-on-surface mt-1">185.220.101.45 (AS9009)</div>
      <div class="text-[11px] text-on-surface-variant">Hosts Trading Portal & Kota Loan Harassment APK</div>
      <div class="mt-2 text-[10px] font-mono text-secondary">Tor Exit Node Infrastructure</div>
    </div>
  </div>

  <!-- Cross-Case Table -->
  <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant">
    <div class="flex items-center justify-between pb-2 border-b border-outline-variant mb-2">
      <span class="font-headline-sm text-[14px] font-bold text-on-surface">Correlated Entity Matches Across Rajasthan Police FIRs</span>
      <span class="font-mono text-[11px] text-secondary">Automated Hash & Identifier Equivalence</span>
    </div>
    <div class="overflow-x-auto">
      <table class="w-full text-left text-[11px]">
        <thead class="bg-surface-container text-on-surface-variant font-label-caps text-[9px]">
          <tr>
            <th class="py-1.5 px-2">Entity Type</th>
            <th class="py-1.5 px-2">Identifier / Value</th>
            <th class="py-1.5 px-2">Cases Involved</th>
            <th class="py-1.5 px-2 text-center">Match Strength</th>
            <th class="py-1.5 px-2">Evidence Corroboration</th>
            <th class="py-1.5 px-2 text-center">Officer Verification</th>
          </tr>
        </thead>
        <tbody id="crossCaseTbody" class="divide-y divide-outline-variant/60 font-mono">
          <!-- Rendered dynamically -->
        </tbody>
      </table>
    </div>
  </div>
</section>
"""

VIEW_TIMELINE = """
<section id="view-investigation-timeline" class="view-panel hidden">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 pb-2 mb-3 border-b border-outline-variant">
    <div>
      <div class="flex items-center gap-1.5">
        <span class="px-2 py-0.5 rounded bg-primary-container text-surface-container-high font-label-code-sm text-[11px]">TEMPORAL RECONSTRUCTION</span>
        <span class="text-secondary font-label-code-sm text-[11px] font-bold">• NORMALIZED TO IST</span>
      </div>
      <h1 class="font-headline-lg text-[18px] font-bold text-on-surface tracking-tight mt-0.5">Chronological Multi-Domain Incident Timeline</h1>
    </div>
    <div class="flex items-center gap-2">
      <select id="timelineFilterSelect" onchange="filterTimelineEvents(this.value)" class="h-8 px-2 bg-surface-container border border-outline-variant rounded font-mono text-[11px]">
        <option value="ALL">All Events (Financial, Cyber, Case)</option>
        <option value="FINANCIAL">Financial Transfers Only</option>
        <option value="CYBER">Digital Infrastructure Only</option>
        <option value="MILESTONE">Police Milestones Only</option>
      </select>
    </div>
  </div>

  <div class="bg-surface-container-lowest rounded-lg p-4 shadow-sm border border-outline-variant">
    <div class="relative pl-6 space-y-6 before:absolute before:left-2 before:top-2 before:bottom-2 before:w-0.5 before:bg-outline-variant" id="timelineEventsContainer">
      <!-- Rendered dynamically -->
    </div>
  </div>
</section>
"""

VIEW_REPORTS_EVIDENCE = """
<section id="view-reports-and-evidence" class="view-panel hidden">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 pb-2 mb-3 border-b border-outline-variant">
    <div>
      <div class="flex items-center gap-1.5">
        <span class="px-2 py-0.5 rounded bg-primary-container text-surface-container-high font-label-code-sm text-[11px]">EVIDENTIARY REPOSITORY</span>
        <span class="text-secondary font-label-code-sm text-[11px] font-bold">• SEC 65B INDIAN EVIDENCE ACT / BSA</span>
      </div>
      <h1 class="font-headline-lg text-[18px] font-bold text-on-surface tracking-tight mt-0.5">Investigation Evidence Vault & Court-Ready Report Generation</h1>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="generateOfficialPDFReport()" class="flex items-center gap-1.5 px-3 py-1.5 bg-error text-white rounded font-label-caps text-[11px] font-bold tracking-wider hover:bg-red-700 shadow-sm transition-opacity">
        <span class="material-symbols-outlined text-[15px]">picture_as_pdf</span>
        <span>DOWNLOAD FORENSIC CASE REPORT (PDF)</span>
      </button>
      <button onclick="generateComprehensiveExcelWorkbook()" class="flex items-center gap-1.5 px-3 py-1.5 bg-secondary text-white rounded font-label-caps text-[11px] font-bold tracking-wider hover:bg-blue-700 shadow-sm transition-opacity">
        <span class="material-symbols-outlined text-[15px]">table_view</span>
        <span>EXPORT 9-SHEET EXCEL WORKBOOK</span>
      </button>
    </div>
  </div>

  <!-- Evidence Files Vault Table -->
  <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant mb-3">
    <div class="flex items-center justify-between pb-2 border-b border-outline-variant mb-2">
      <div class="flex items-center gap-1.5">
        <span class="material-symbols-outlined text-secondary text-[18px]">folder_special</span>
        <span class="font-headline-sm text-[14px] font-bold text-on-surface">Evidence Files & Cryptographic SHA-256 Chain</span>
      </div>
      <button onclick="verifyAllHashes()" class="px-2 py-1 bg-surface-container hover:bg-surface-container-high border border-outline-variant rounded font-mono text-[10px] text-secondary">
        RE-VERIFY ALL HASHES
      </button>
    </div>
    <div class="overflow-x-auto">
      <table class="w-full text-left text-[11px]">
        <thead class="bg-surface-container text-on-surface-variant font-label-caps text-[9px]">
          <tr>
            <th class="py-1.5 px-2">Evidence ID</th>
            <th class="py-1.5 px-2">Original Filename</th>
            <th class="py-1.5 px-2">Type</th>
            <th class="py-1.5 px-2">Ingestion Time</th>
            <th class="py-1.5 px-2 font-mono">SHA-256 Checksum</th>
            <th class="py-1.5 px-2 text-center">Status</th>
            <th class="py-1.5 px-2 text-center">Action</th>
          </tr>
        </thead>
        <tbody id="evidenceTableTbody" class="divide-y divide-outline-variant/60 font-mono">
          <!-- Rendered dynamically -->
        </tbody>
      </table>
    </div>
  </div>

  <!-- Report Generator Preview Box -->
  <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant">
    <div class="flex items-center justify-between pb-2 border-b border-outline-variant mb-2">
      <span class="font-headline-sm text-[14px] font-bold text-on-surface">Court Report Narrative Preview</span>
      <span class="font-label-caps text-[10px] px-1.5 py-0.2 rounded bg-amber-100 text-amber-900 border border-amber-300">DRAFT — FOR OFFICER VERIFICATION</span>
    </div>
    <div class="p-3 bg-surface-container-low rounded border border-outline-variant font-mono text-[11px] text-slate-800 space-y-2 leading-relaxed" id="reportPreviewContainer">
      <!-- Rendered dynamically -->
    </div>
  </div>
</section>
"""

VIEW_LAWFUL_REQUESTS = """
<section id="view-lawful-requests" class="view-panel hidden">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 pb-2 mb-3 border-b border-outline-variant">
    <div>
      <div class="flex items-center gap-1.5">
        <span class="px-2 py-0.5 rounded bg-error/10 text-error font-label-code-sm text-[11px] font-bold">STATUTORY LEGAL DIRECTIVES</span>
        <span class="text-secondary font-label-code-sm text-[11px] font-bold">• SEC 91 CrPC / SEC 94 BNSS</span>
      </div>
      <h1 class="font-headline-lg text-[18px] font-bold text-on-surface tracking-tight mt-0.5">Lawful Information Request & Freeze Notice Generator</h1>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="copyNoticeToClipboard()" class="flex items-center gap-1 px-3 py-1.5 bg-secondary text-white rounded font-label-caps text-[11px] font-bold tracking-wider hover:bg-blue-700 transition-colors">
        <span class="material-symbols-outlined text-[15px]">content_copy</span>
        <span>COPY NOTICE TEXT</span>
      </button>
      <button onclick="downloadNoticePDF()" class="flex items-center gap-1 px-3 py-1.5 bg-error text-white rounded font-label-caps text-[11px] font-bold tracking-wider hover:bg-red-700 transition-colors">
        <span class="material-symbols-outlined text-[15px]">picture_as_pdf</span>
        <span>DOWNLOAD SIGNED NOTICE (PDF)</span>
      </button>
    </div>
  </div>

  <!-- Form & Interactive Draft Container -->
  <div class="grid grid-cols-1 lg:grid-cols-12 gap-3 mb-3">
    <!-- Left: Recipient & Account Configuration -->
    <div class="lg:col-span-4 flex flex-col gap-3">
      <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant">
        <div class="font-headline-sm text-[13px] font-bold text-on-surface mb-2">Notice Parameters</div>
        <div class="space-y-2 text-[11px]">
          <div>
            <label class="font-label-caps text-[9px] text-on-surface-variant uppercase">Target Entity Type</label>
            <select id="noticeRecipientType" onchange="updateNoticeTemplate()" class="w-full h-7 px-2 bg-surface-container-low border border-outline-variant rounded">
              <option value="BANK_FREEZE">Core Banking System (Nodal Officer - Immediate Debit Freeze)</option>
              <option value="GATEWAY_UPI">Payment Aggregator / NPCI (UPI VPA Log Records)</option>
              <option value="REGISTRAR">Domain Registrar (Namecheap / PDR - WHOIS & Server IP)</option>
              <option value="HOSTING_VPN">Offshore Cloud Host / ISP (Access & IPDR Logs)</option>
            </select>
          </div>
          <div>
            <label class="font-label-caps text-[9px] text-on-surface-variant uppercase">Select Target Account / Entity</label>
            <select id="noticeTargetEntitySelect" onchange="updateNoticeTemplate()" class="w-full h-7 px-2 bg-surface-container-low border border-outline-variant rounded font-mono">
              <option value="1192837465">Axis Bank: 1192837465 (Suresh Traders - ₹50,000)</option>
              <option value="8829103948">HDFC Bank: 8829103948 (Vikash Cloud - ₹15,000)</option>
              <option value="7738291045">Yes Bank: 7738291045 (Royal Ent - ₹15,000)</option>
              <option value="9182736450">Kotak Bank: 9182736450 (Ashok Verma - ₹10,000)</option>
            </select>
          </div>
          <div>
            <label class="font-label-caps text-[9px] text-on-surface-variant uppercase">Investigating Officer Name & Rank</label>
            <input id="noticeOfficerInput" type="text" value="Insp. Rajesh K. Shekhawat, State Cyber PS Jaipur" class="w-full h-7 px-2 bg-surface-container-low border border-outline-variant rounded text-[11px]"/>
          </div>
        </div>
      </div>
    </div>

    <!-- Right: Rich Notice Document Preview -->
    <div class="lg:col-span-8 flex flex-col gap-3">
      <div class="bg-surface-container-lowest rounded-lg p-4 shadow-sm border border-outline-variant">
        <div class="flex items-center justify-between pb-2 border-b border-outline-variant mb-2">
          <span class="font-headline-sm text-[13px] font-bold text-on-surface">Official Statutory Directive Draft</span>
          <span class="px-1.5 py-0.2 rounded bg-amber-100 text-amber-900 border border-amber-300 font-mono text-[9px]">DRAFT — SUBJECT TO SIGNATURE</span>
        </div>
        <textarea id="noticeDraftTextarea" rows="16" class="w-full p-3 bg-surface-container-low border border-outline-variant rounded font-mono text-[11px] text-slate-800 focus:outline-none focus:bg-white leading-relaxed resize-y"></textarea>
      </div>
    </div>
  </div>
</section>
"""

VIEW_AUDIT_LOG = """
<section id="view-audit-log" class="view-panel hidden">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 pb-2 mb-3 border-b border-outline-variant">
    <div>
      <div class="flex items-center gap-1.5">
        <span class="px-2 py-0.5 rounded bg-primary-container text-surface-container-high font-label-code-sm text-[11px]">AUDIT INTEGRITY CHAIN</span>
        <span class="text-secondary font-label-code-sm text-[11px] font-bold">• FORENSIC TRACEABILITY</span>
      </div>
      <h1 class="font-headline-lg text-[18px] font-bold text-on-surface tracking-tight mt-0.5">Platform Forensic Audit Log</h1>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="exportAuditLogCSV()" class="flex items-center gap-1 px-3 py-1.5 bg-surface-container-low hover:bg-surface-container text-on-surface rounded font-label-caps text-[11px] tracking-wider border border-outline-variant">
        <span class="material-symbols-outlined text-[15px]">download</span>
        <span>EXPORT AUDIT CSV</span>
      </button>
    </div>
  </div>

  <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant">
    <div class="overflow-x-auto">
      <table class="w-full text-left text-[11px]">
        <thead class="bg-surface-container text-on-surface-variant font-label-caps text-[9px]">
          <tr>
            <th class="py-1.5 px-2">Log ID</th>
            <th class="py-1.5 px-2">Timestamp (IST)</th>
            <th class="py-1.5 px-2">Officer Identity</th>
            <th class="py-1.5 px-2">Action / Command</th>
            <th class="py-1.5 px-2">Case Reference</th>
            <th class="py-1.5 px-2">Forensic Details</th>
            <th class="py-1.5 px-2 font-mono">Chain Hash</th>
          </tr>
        </thead>
        <tbody id="auditLogTbody" class="divide-y divide-outline-variant/60 font-mono">
          <!-- Rendered dynamically -->
        </tbody>
      </table>
    </div>
  </div>
</section>
"""

VIEW_SETTINGS = """
<section id="view-settings" class="view-panel hidden">
  <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 pb-2 mb-3 border-b border-outline-variant">
    <div>
      <div class="flex items-center gap-1.5">
        <span class="px-2 py-0.5 rounded bg-primary-container text-surface-container-high font-label-code-sm text-[11px]">CONFIGURATION</span>
        <span class="text-secondary font-label-code-sm text-[11px] font-bold">• HEURISTIC WEIGHTS & THRESHOLDS</span>
      </div>
      <h1 class="font-headline-lg text-[18px] font-bold text-on-surface tracking-tight mt-0.5">MuleNet Intelligence Rules & System Configuration</h1>
    </div>
    <div class="flex items-center gap-2">
      <button onclick="resetSettingsToDefaults()" class="px-3 py-1.5 bg-surface-container hover:bg-surface-container-high border border-outline-variant rounded font-label-caps text-[11px] text-on-surface transition-colors">
        RESET TO DEFAULTS
      </button>
      <button onclick="saveSettingsConfiguration()" class="px-3 py-1.5 bg-secondary text-white rounded font-label-caps text-[11px] font-bold hover:bg-blue-700 transition-colors">
        SAVE & RECALCULATE ALL
      </button>
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-3 mb-3">
    <!-- Rule Weights Configuration -->
    <div class="bg-surface-container-lowest rounded-lg p-3.5 shadow-sm border border-outline-variant">
      <div class="font-headline-sm text-[13px] font-bold text-on-surface mb-2">Detection Rule Scoring Weights (0 - 100 Composite)</div>
      <div class="space-y-2 text-[11px]">
        <div class="flex items-center justify-between">
          <span>Rapid In-Out Transfer Weight:</span>
          <input id="cfgWeightRapid" type="number" value="20" min="0" max="50" class="w-16 h-6 px-1.5 bg-surface-container-low border border-outline-variant rounded text-right font-mono"/>
        </div>
        <div class="flex items-center justify-between">
          <span>Many-to-One Credits Weight:</span>
          <input id="cfgWeightMany" type="number" value="15" min="0" max="50" class="w-16 h-6 px-1.5 bg-surface-container-low border border-outline-variant rounded text-right font-mono"/>
        </div>
        <div class="flex items-center justify-between">
          <span>Round-Figure Layering Weight:</span>
          <input id="cfgWeightRound" type="number" value="10" min="0" max="50" class="w-16 h-6 px-1.5 bg-surface-container-low border border-outline-variant rounded text-right font-mono"/>
        </div>
        <div class="flex items-center justify-between">
          <span>Dormant-to-Active Jump Weight:</span>
          <input id="cfgWeightDormant" type="number" value="15" min="0" max="50" class="w-16 h-6 px-1.5 bg-surface-container-low border border-outline-variant rounded text-right font-mono"/>
        </div>
        <div class="flex items-center justify-between">
          <span>Repeated Counterparties Weight:</span>
          <input id="cfgWeightRepeated" type="number" value="10" min="0" max="50" class="w-16 h-6 px-1.5 bg-surface-container-low border border-outline-variant rounded text-right font-mono"/>
        </div>
        <div class="flex items-center justify-between">
          <span>High Transaction Velocity Weight:</span>
          <input id="cfgWeightVelocity" type="number" value="10" min="0" max="50" class="w-16 h-6 px-1.5 bg-surface-container-low border border-outline-variant rounded text-right font-mono"/>
        </div>
        <div class="flex items-center justify-between">
          <span>Pass-Through Ratio Weight:</span>
          <input id="cfgWeightPass" type="number" value="10" min="0" max="50" class="w-16 h-6 px-1.5 bg-surface-container-low border border-outline-variant rounded text-right font-mono"/>
        </div>
        <div class="flex items-center justify-between">
          <span>Cross-Case Match Weight:</span>
          <input id="cfgWeightCross" type="number" value="10" min="0" max="50" class="w-16 h-6 px-1.5 bg-surface-container-low border border-outline-variant rounded text-right font-mono"/>
        </div>
      </div>
    </div>

    <!-- Thresholds & Hackathon Reset -->
    <div class="bg-surface-container-lowest rounded-lg p-3.5 shadow-sm border border-outline-variant flex flex-col justify-between">
      <div>
        <div class="font-headline-sm text-[13px] font-bold text-on-surface mb-2">Thresholds & Algorithm Parameters</div>
        <div class="space-y-2 text-[11px]">
          <div class="flex items-center justify-between">
            <span>High Risk Threshold:</span>
            <input id="cfgThreshHigh" type="number" value="70" min="50" max="90" class="w-16 h-6 px-1.5 bg-surface-container-low border border-outline-variant rounded text-right font-mono"/>
          </div>
          <div class="flex items-center justify-between">
            <span>Medium Risk Threshold:</span>
            <input id="cfgThreshMed" type="number" value="40" min="20" max="60" class="w-16 h-6 px-1.5 bg-surface-container-low border border-outline-variant rounded text-right font-mono"/>
          </div>
          <div class="flex items-center justify-between">
            <span>Rapid In-Out Dwell Limit (Hours):</span>
            <input id="cfgRapidHours" type="number" value="2" min="1" max="24" class="w-16 h-6 px-1.5 bg-surface-container-low border border-outline-variant rounded text-right font-mono"/>
          </div>
          <div class="flex items-center justify-between">
            <span>Dormancy Inactivity Period (Days):</span>
            <input id="cfgDormantDays" type="number" value="30" min="15" max="180" class="w-16 h-6 px-1.5 bg-surface-container-low border border-outline-variant rounded text-right font-mono"/>
          </div>
        </div>
      </div>

      <div class="mt-4 pt-3 border-t border-outline-variant">
        <div class="font-label-caps text-[10px] text-error font-bold mb-1">HAZARDOUS RESET ZONE:</div>
        <button onclick="resetEntireDemoPristine()" class="w-full py-1.5 bg-error/10 hover:bg-error/20 text-error border border-error/30 rounded font-label-caps text-[10px] font-bold tracking-wider transition-colors flex items-center justify-center gap-1">
          <span class="material-symbols-outlined text-[14px]">restart_alt</span>
          <span>RESTORE ENTIRE PLATFORM TO PRISTINE DEMO STATE</span>
        </button>
      </div>
    </div>
  </div>
</section>
"""

# Modals and Floating Panels
MODALS_HTML = """
<!-- Create Case Modal -->
<div id="createCaseModal" class="hidden fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-3">
  <div class="bg-surface-container-lowest rounded-lg border border-outline-variant max-w-lg w-full p-4 shadow-xl">
    <div class="flex items-center justify-between pb-2 border-b border-outline-variant mb-3">
      <div class="font-headline-sm text-[14px] font-bold text-on-surface">Register New Cyber Crime Case FIR</div>
      <button onclick="closeCreateCaseModal()" class="text-on-surface-variant hover:text-on-surface">
        <span class="material-symbols-outlined text-[18px]">close</span>
      </button>
    </div>
    <div class="space-y-2 text-[11px]">
      <div>
        <label class="font-label-caps text-[9px] text-on-surface-variant uppercase">FIR Number</label>
        <input id="newCaseFirNo" type="text" placeholder="e.g. FIR No. 201/2024" class="w-full h-7 px-2 bg-surface-container-low border border-outline-variant rounded"/>
      </div>
      <div>
        <label class="font-label-caps text-[9px] text-on-surface-variant uppercase">Case Title / Syndicate</label>
        <input id="newCaseTitle" type="text" placeholder="e.g. Fictitious Crypto Staking Scheme" class="w-full h-7 px-2 bg-surface-container-low border border-outline-variant rounded"/>
      </div>
      <div>
        <label class="font-label-caps text-[9px] text-on-surface-variant uppercase">Police Station Jurisdiction</label>
        <input id="newCaseStation" type="text" value="Cyber Police Station, Jaipur South" class="w-full h-7 px-2 bg-surface-container-low border border-outline-variant rounded"/>
      </div>
      <div class="grid grid-cols-2 gap-2">
        <div>
          <label class="font-label-caps text-[9px] text-on-surface-variant uppercase">Victim Name</label>
          <input id="newCaseVictim" type="text" placeholder="Victim Name" class="w-full h-7 px-2 bg-surface-container-low border border-outline-variant rounded"/>
        </div>
        <div>
          <label class="font-label-caps text-[9px] text-on-surface-variant uppercase">Reported Amount (₹)</label>
          <input id="newCaseAmount" type="number" placeholder="100000" class="w-full h-7 px-2 bg-surface-container-low border border-outline-variant rounded font-mono"/>
        </div>
      </div>
      <div>
        <label class="font-label-caps text-[9px] text-on-surface-variant uppercase">Victim Primary UTR</label>
        <input id="newCaseUTR" type="text" placeholder="e.g. UTR-2024-RJ-XXXX" class="w-full h-7 px-2 bg-surface-container-low border border-outline-variant rounded font-mono"/>
      </div>
    </div>
    <div class="flex items-center justify-end gap-2 mt-4 pt-2 border-t border-outline-variant">
      <button onclick="closeCreateCaseModal()" class="px-3 py-1 text-on-surface-variant hover:text-on-surface font-label-caps text-[10px]">CANCEL</button>
      <button onclick="saveNewCase()" class="px-4 py-1.5 bg-secondary text-white rounded font-label-caps text-[10px] font-bold hover:bg-blue-700">CREATE FIR RECORD</button>
    </div>
  </div>
</div>

<!-- Automated Self-Tests Modal -->
<div id="selfTestsModal" class="hidden fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-3">
  <div class="bg-surface-container-lowest rounded-lg border border-outline-variant max-w-xl w-full p-4 shadow-xl">
    <div class="flex items-center justify-between pb-2 border-b border-outline-variant mb-2">
      <div class="flex items-center gap-1.5">
        <span class="material-symbols-outlined text-secondary text-[20px]">verified</span>
        <div class="font-headline-sm text-[14px] font-bold text-on-surface">MuleNet Automated Acceptance Tests</div>
      </div>
      <button onclick="closeSelfTestsModal()" class="text-on-surface-variant hover:text-on-surface">
        <span class="material-symbols-outlined text-[18px]">close</span>
      </button>
    </div>
    <div class="text-[11px] text-on-surface-variant mb-3">
      Live mathematical verification of core forensic invariants: fund conservation, reconciliation formulas, chronological precedence, and cross-case detection.
    </div>
    <div id="selfTestResultsContainer" class="space-y-2 text-[11px] font-mono">
      <!-- Injected dynamically -->
    </div>
    <div class="flex items-center justify-between mt-4 pt-2 border-t border-outline-variant">
      <span class="font-mono text-[10px] text-secondary" id="selfTestsSummaryLabel">All 6 Tests Passed</span>
      <button onclick="runAllSelfTests()" class="px-3 py-1.5 bg-secondary text-white rounded font-label-caps text-[10px] font-bold hover:bg-blue-700">
        RE-EXECUTE TESTS
      </button>
    </div>
  </div>
</div>

<!-- Floating Guided Demo Banner Controller -->
<div id="guidedDemoBanner" class="hidden fixed bottom-4 left-72 right-6 z-40 bg-slate-900 text-white rounded-lg p-3 shadow-2xl border border-amber-500/50 flex flex-col md:flex-row items-center justify-between gap-3 animate-bounce-subtle">
  <div class="flex items-center gap-2">
    <span class="w-8 h-8 rounded-full bg-amber-500 text-slate-900 flex items-center justify-center font-bold font-mono text-[13px] shrink-0" id="demoStepPill">1</span>
    <div>
      <div class="flex items-center gap-2">
        <span class="font-bold text-amber-400 text-[12px] uppercase tracking-wide" id="demoStepTitle">Step 1: Open Victim Complaint</span>
        <span class="text-[10px] text-slate-400 font-mono">(Step <span id="demoStepNum">1</span> of 11)</span>
      </div>
      <div class="text-[11px] text-slate-200 mt-0.5" id="demoStepDesc">
        Review FIR No. 104/2024 registered at Cyber PS Jaipur South.
      </div>
    </div>
  </div>
  <div class="flex items-center gap-2 shrink-0">
    <button onclick="demoStepPrev()" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded text-[10px] font-mono">‹ PREV</button>
    <button onclick="demoStepNext()" class="px-3 py-1 bg-amber-500 hover:bg-amber-400 text-slate-900 font-bold rounded text-[10px] font-mono">NEXT STEP ›</button>
    <button onclick="stopGuidedDemo()" class="text-slate-400 hover:text-white p-1">
      <span class="material-symbols-outlined text-[16px]">close</span>
    </button>
  </div>
</div>
"""

print("Views part 3 loaded.")
