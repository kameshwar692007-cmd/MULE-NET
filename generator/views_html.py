# generator/views_html.py
# HTML for all 15 views, headers, sidebars, modals and forensic side drawers

HEADER_HTML = """
<header class="fixed top-0 left-0 right-0 h-16 bg-surface-container-lowest border-b border-outline-variant z-40 flex items-center justify-between px-2 sm:px-3 md:px-4">
  <div class="flex items-center gap-2 sm:gap-3 flex-shrink-0">
    <!-- Mobile Hamburger Toggle -->
    <button onclick="toggleMobileSidebar()" class="lg:hidden p-1.5 rounded-md text-on-surface hover:bg-surface-container border border-outline-variant flex items-center justify-center focus:outline-none cursor-pointer" aria-label="Toggle Navigation">
      <span class="material-symbols-outlined text-[20px]">menu</span>
    </button>
    <div class="flex items-center gap-2">
      <div class="w-8 h-8 sm:w-9 sm:h-9 rounded bg-primary-container border border-outline-variant flex items-center justify-center text-amber-500 font-bold shadow-sm flex-shrink-0">
        <span class="material-symbols-outlined text-[20px] sm:text-[22px]">shield</span>
      </div>
      <div class="flex flex-col border-l border-outline-variant pl-2">
        <div class="flex items-center gap-1 sm:gap-1.5">
          <span class="font-headline-sm text-[13px] sm:text-[15px] font-bold tracking-tight text-on-surface">MULENET</span>
          <span class="px-1.5 py-0.2 bg-surface-container text-secondary text-[9px] sm:text-[10px] font-label-code-sm font-bold rounded">POLICE INTEL v4.2</span>
        </div>
        <span class="font-label-caps text-[8px] sm:text-[9px] text-on-surface-variant uppercase tracking-wider hidden sm:inline">STATE CYBER POLICE HQ, JAIPUR</span>
      </div>
    </div>
  </div>

  <!-- Global Search Bar -->
  <div class="flex-1 max-w-xs sm:max-w-sm md:max-w-md lg:max-w-lg mx-2 sm:mx-3 min-w-0">
    <div class="relative flex items-center w-full">
      <span class="material-symbols-outlined absolute left-2.5 text-on-surface-variant text-[16px] sm:text-[18px]">search</span>
      <input id="globalSearchInput" onkeyup="handleGlobalSearch(event)" class="w-full h-8 pl-8 sm:pl-9 pr-6 sm:pr-8 bg-surface-container-low border border-outline-variant rounded font-label-code-sm text-[11px] sm:text-[12px] text-on-surface focus:outline-none focus:border-secondary focus:bg-surface-container-lowest placeholder:text-outline truncate" placeholder="Global Search: UTR / Account..." type="text"/>
      <span class="absolute right-2 text-[10px] text-outline font-label-code-sm border border-outline-variant px-1 rounded hidden sm:inline">↵</span>
    </div>
    <!-- Search Results Dropdown -->
    <div id="globalSearchResults" class="hidden absolute top-12 max-w-lg w-full bg-surface-container-lowest border border-outline-variant rounded shadow-lg z-50 p-2 space-y-1"></div>
  </div>

  <!-- Case Quick Switcher & Officer Profile -->
  <div class="flex items-center gap-1 sm:gap-2 flex-shrink-0">
    <!-- Active Case Selector -->
    <div class="hidden xl:flex items-center gap-1.5 px-2 py-1 bg-surface-container border border-outline-variant rounded">
      <span class="w-2 h-2 rounded-full bg-error animate-pulse"></span>
      <div class="flex flex-col">
        <div class="flex items-center gap-1">
          <select id="caseSwitcherSelect" onchange="switchCase(this.value)" class="bg-transparent font-label-code-sm text-[11px] font-bold text-on-surface focus:outline-none cursor-pointer">
            <option value="FIR-104-2024">FIR 104/2024 (Jaipur South - Trading)</option>
            <option value="FIR-072-2024">FIR 072/2024 (Jodhpur - Job Phishing)</option>
            <option value="FIR-119-2024">FIR 119/2024 (Kota - Loan Extortion)</option>
          </select>
        </div>
        <span class="font-body-sm text-[10px] text-on-surface-variant leading-tight">₹1.00 L Traced | <span class="text-error font-semibold">ACTIVE</span></span>
      </div>
    </div>

    <!-- Guided Demo Tour Button -->
    <button onclick="startGuidedDemo()" class="flex items-center gap-1 px-2 sm:px-2.5 py-1 bg-amber-500 hover:bg-amber-600 text-slate-900 rounded font-label-caps text-[10px] sm:text-[11px] font-bold tracking-wider shadow-sm transition-all" title="Guided Tour">
      <span class="material-symbols-outlined text-[15px]">play_circle</span>
      <span class="hidden md:inline">GUIDED DEMO</span>
    </button>

    <!-- Automated Self Tests Button -->
    <button onclick="openSelfTestsModal()" class="flex items-center gap-1 px-2 py-1 bg-surface-container hover:bg-surface-container-high border border-outline-variant text-on-surface rounded font-label-caps text-[10px] font-semibold tracking-wider transition-colors" title="Self-Tests">
      <span class="material-symbols-outlined text-[14px] text-secondary">verified</span>
      <span class="hidden md:inline">SELF-TESTS</span>
    </button>

    <!-- Evaluator / User Manual Button -->
    <button onclick="openEvaluatorManual()" class="flex items-center gap-1 px-2 py-1 bg-blue-600 hover:bg-blue-700 text-white rounded font-label-caps text-[10px] font-bold tracking-wider transition-colors shadow-sm" title="User Manual">
      <span class="material-symbols-outlined text-[14px]">menu_book</span>
      <span class="hidden sm:inline">USER MANUAL</span>
    </button>

    <!-- Officer Badge -->
    <div class="hidden 2xl:flex items-center gap-1.5 px-2 py-1 bg-surface-container-low rounded border border-outline-variant">
      <span class="material-symbols-outlined text-[16px] text-secondary">badge</span>
      <div class="flex flex-col text-right">
        <span class="font-label-caps text-[10px] text-on-surface font-semibold leading-tight">Insp. Rajesh K.</span>
        <span class="font-label-code-sm text-[9px] text-on-surface-variant leading-tight">RJ-CY-8402</span>
      </div>
    </div>

    <!-- Sec 65B Hash Seal -->
    <div class="hidden sm:flex items-center gap-1 px-1.5 py-1 rounded bg-surface-container font-label-code-sm text-[10px] text-on-surface-variant border border-outline-variant" title="Cryptographic SHA-256 Chain Active">
      <span class="material-symbols-outlined text-[13px] text-secondary">lock</span>
      <span>SHA-256</span>
    </div>
  </div>
</header>
"""

SIDEBAR_HTML = """
<!-- Mobile Sidebar Backdrop -->
<div id="sidebarBackdrop" onclick="toggleMobileSidebar()" class="fixed inset-0 top-16 bg-slate-950/70 backdrop-blur-sm z-45 hidden lg:hidden transition-opacity"></div>

<aside id="mainSidebar" class="fixed left-0 top-16 bottom-0 w-64 bg-primary-container text-on-primary-container z-50 flex flex-col justify-between border-r border-outline-variant overflow-y-auto transform -translate-x-full lg:translate-x-0 transition-transform duration-200 ease-in-out shadow-2xl lg:shadow-none">
  <div class="py-3">
    <!-- Operations Group -->
    <div class="px-4 mb-1 font-label-caps text-[10px] text-outline-variant uppercase tracking-wider flex items-center justify-between">
      <span>Command & Operations</span>
      <button onclick="toggleMobileSidebar()" class="lg:hidden text-slate-400 hover:text-white p-0.5" title="Close Menu">
        <span class="material-symbols-outlined text-[16px]">close</span>
      </button>
    </div>
    <nav class="space-y-0.5 px-2 mb-3">
      <a href="javascript:void(0)" onclick="navigateTo('investigation-dashboard')" id="nav-investigation-dashboard" class="nav-item active flex items-center gap-2.5 px-3 py-1.5 rounded transition-colors text-slate-300 hover:bg-slate-800 hover:text-white font-body-sm text-[13px]">
        <span class="material-symbols-outlined text-[18px]">dashboard</span>
        <span>Investigation Overview</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateTo('cases')" id="nav-cases" class="nav-item flex items-center gap-2.5 px-3 py-1.5 rounded text-slate-300 hover:bg-slate-800 hover:text-white transition-colors font-body-sm text-[13px]">
        <span class="material-symbols-outlined text-[18px]">folder_shared</span>
        <span>Case Management</span>
      </a>
    </nav>

    <!-- Financial Forensics Group -->
    <div class="px-4 mb-1 font-label-caps text-[10px] text-outline-variant uppercase tracking-wider">Financial Forensics</div>
    <nav class="space-y-0.5 px-2 mb-3">
      <a href="javascript:void(0)" onclick="navigateTo('bank-statement-ingestion')" id="nav-bank-statement-ingestion" class="nav-item flex items-center gap-2.5 px-3 py-1.5 rounded text-slate-300 hover:bg-slate-800 hover:text-white transition-colors font-body-sm text-[13px]">
        <span class="material-symbols-outlined text-[18px]">upload_file</span>
        <span>Bank Statement Ingestion</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateTo('transaction-explorer')" id="nav-transaction-explorer" class="nav-item flex items-center gap-2.5 px-3 py-1.5 rounded text-slate-300 hover:bg-slate-800 hover:text-white transition-colors font-body-sm text-[13px]">
        <span class="material-symbols-outlined text-[18px]">receipt_long</span>
        <span>Transaction Explorer</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateTo('mule-account-detection')" id="nav-mule-account-detection" class="nav-item flex items-center gap-2.5 px-3 py-1.5 rounded text-slate-300 hover:bg-slate-800 hover:text-white transition-colors font-body-sm text-[13px]">
        <span class="material-symbols-outlined text-[18px]">account_tree</span>
        <span>Mule Account Detection</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateTo('money-trail-analysis')" id="nav-money-trail-analysis" class="nav-item flex items-center gap-2.5 px-3 py-1.5 rounded text-slate-300 hover:bg-slate-800 hover:text-white transition-colors font-body-sm text-[13px]">
        <span class="material-symbols-outlined text-[18px] text-amber-400">hub</span>
        <span class="font-semibold text-white">Money Trail Analysis</span>
        <span class="ml-auto px-1 py-0.2 bg-amber-500/20 text-amber-400 text-[9px] font-bold rounded">HERO</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateTo('freeze-priority-engine')" id="nav-freeze-priority-engine" class="nav-item flex items-center gap-2.5 px-3 py-1.5 rounded text-slate-300 hover:bg-slate-800 hover:text-white transition-colors font-body-sm text-[13px]">
        <span class="material-symbols-outlined text-[18px]">lock_clock</span>
        <span>Freeze-Priority Engine</span>
      </a>
    </nav>

    <!-- Cyber & Infrastructure Group -->
    <div class="px-4 mb-1 font-label-caps text-[10px] text-outline-variant uppercase tracking-wider">Cyber & Infrastructure</div>
    <nav class="space-y-0.5 px-2 mb-3">
      <a href="javascript:void(0)" onclick="navigateTo('domain-and-ip-intelligence')" id="nav-domain-and-ip-intelligence" class="nav-item flex items-center gap-2.5 px-3 py-1.5 rounded text-slate-300 hover:bg-slate-800 hover:text-white transition-colors font-body-sm text-[13px]">
        <span class="material-symbols-outlined text-[18px]">dns</span>
        <span>Domain & IP Intelligence</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateTo('relationship-graph')" id="nav-relationship-graph" class="nav-item flex items-center gap-2.5 px-3 py-1.5 rounded text-slate-300 hover:bg-slate-800 hover:text-white transition-colors font-body-sm text-[13px]">
        <span class="material-symbols-outlined text-[18px]">bubble_chart</span>
        <span>Relationship Graph</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateTo('cross-case-linking')" id="nav-cross-case-linking" class="nav-item flex items-center gap-2.5 px-3 py-1.5 rounded text-slate-300 hover:bg-slate-800 hover:text-white transition-colors font-body-sm text-[13px]">
        <span class="material-symbols-outlined text-[18px]">share</span>
        <span>Cross-Case Intelligence</span>
      </a>
    </nav>

    <!-- Evidence & Compliance Group -->
    <div class="px-4 mb-1 font-label-caps text-[10px] text-outline-variant uppercase tracking-wider">Evidence & Legal Compliance</div>
    <nav class="space-y-0.5 px-2 mb-3">
      <a href="javascript:void(0)" onclick="navigateTo('investigation-timeline')" id="nav-investigation-timeline" class="nav-item flex items-center gap-2.5 px-3 py-1.5 rounded text-slate-300 hover:bg-slate-800 hover:text-white transition-colors font-body-sm text-[13px]">
        <span class="material-symbols-outlined text-[18px]">timeline</span>
        <span>Investigation Timeline</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateTo('reports-and-evidence')" id="nav-reports-and-evidence" class="nav-item flex items-center gap-2.5 px-3 py-1.5 rounded text-slate-300 hover:bg-slate-800 hover:text-white transition-colors font-body-sm text-[13px]">
        <span class="material-symbols-outlined text-[18px]">gavel</span>
        <span>Reports & Evidence</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateTo('lawful-requests')" id="nav-lawful-requests" class="nav-item flex items-center gap-2.5 px-3 py-1.5 rounded text-slate-300 hover:bg-slate-800 hover:text-white transition-colors font-body-sm text-[13px]">
        <span class="material-symbols-outlined text-[18px]">assignment_late</span>
        <span>Sec 91 CrPC Requests</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateTo('audit-log')" id="nav-audit-log" class="nav-item flex items-center gap-2.5 px-3 py-1.5 rounded text-slate-300 hover:bg-slate-800 hover:text-white transition-colors font-body-sm text-[13px]">
        <span class="material-symbols-outlined text-[18px]">history</span>
        <span>Audit Log</span>
      </a>
      <a href="javascript:void(0)" onclick="navigateTo('settings')" id="nav-settings" class="nav-item flex items-center gap-2.5 px-3 py-1.5 rounded text-slate-300 hover:bg-slate-800 hover:text-white transition-colors font-body-sm text-[13px]">
        <span class="material-symbols-outlined text-[18px]">settings</span>
        <span>Settings & Help</span>
      </a>
    </nav>
  </div>

  <!-- Sidebar Footer / Doctrine -->
  <div class="p-3 border-t border-outline/30 bg-primary-container">
    <div class="p-2 bg-surface-container-low/10 rounded border border-outline-variant/30 mb-2">
      <div class="font-label-caps text-[9px] text-amber-400 font-bold tracking-wider uppercase mb-0.5 flex items-center gap-1">
        <span class="material-symbols-outlined text-[13px]">verified_user</span>
        <span>Team TechTonicX</span>
      </div>
      <p class="font-body-sm text-[11px] text-surface-container-high leading-snug italic">"Follow the Money. Find the Infrastructure. Prioritise Action."</p>
      <div class="mt-1 pt-1 border-t border-outline/30 flex items-center justify-between font-label-code-sm text-[9px] text-outline-variant">
        <span>RAJASTHAN POLICE HACKATHON</span>
        <span class="text-secondary-fixed">OFFLINE READY</span>
      </div>
    </div>
    <button onclick="navigateTo('lawful-requests')" class="flex items-center justify-center gap-1.5 w-full py-1.5 bg-secondary hover:bg-blue-700 text-white rounded font-label-caps text-[11px] font-bold tracking-wider transition-colors shadow-sm">
      <span class="material-symbols-outlined text-[14px]">bolt</span>
      <span>EMERGENCY FREEZE NOTICE</span>
    </button>
  </div>
</aside>
"""

# Now write the 15 view containers
VIEW_OVERVIEW = """
<section id="view-investigation-dashboard" class="view-panel">
  <!-- Case Command Ribbon -->
  <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm mb-3 border border-outline-variant">
    <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-2 pb-2">
      <div class="flex flex-wrap items-center gap-2">
        <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded bg-error/10 text-error font-label-code-sm text-[11px] font-bold">
          <span class="w-1.5 h-1.5 rounded-full bg-error animate-pulse"></span>
          CRITICAL INVESTIGATION
        </span>
        <span id="dashCaseFir" class="font-label-code-md text-[13px] text-on-surface font-semibold">FIR No. 104/2024</span>
        <span class="text-on-surface-variant">|</span>
        <span id="dashCasePS" class="font-body-sm text-[13px] text-on-surface-variant">Cyber Police Station, Jaipur South</span>
        <span class="text-on-surface-variant">|</span>
        <span class="font-body-sm text-[12px] text-on-surface-variant">Sec 66D IT Act • Sec 318(4), 319(2), 61(2) BNS</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="font-label-caps text-[10px] text-on-surface-variant uppercase">EVIDENTIARY HASH:</span>
        <span class="font-label-code-sm text-[11px] bg-surface-container px-2 py-0.5 rounded text-on-surface font-mono">SHA256: 8f4a...9b12e</span>
        <button onclick="navigateTo('reports-and-evidence')" class="inline-flex items-center gap-1 px-2.5 py-1 bg-surface-container-high hover:bg-surface-container-highest text-on-surface rounded font-label-caps text-[10px] uppercase transition-colors">
          <span class="material-symbols-outlined text-[13px]">history</span>
          <span>Integrity Chain</span>
        </button>
      </div>
    </div>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-2 pt-2 bg-surface-container-low rounded p-2 text-[12px]">
      <div>
        <div class="font-label-caps text-[10px] text-on-surface-variant uppercase">Case Nomenclature</div>
        <div id="dashCaseTitle" class="font-headline-sm text-[13px] font-semibold text-on-surface truncate">Trading Investment Syndicate</div>
      </div>
      <div>
        <div class="font-label-caps text-[10px] text-on-surface-variant uppercase">Lead Investigating Officer</div>
        <div class="font-body-md text-[13px] text-on-surface flex items-center gap-1">
          <span class="material-symbols-outlined text-[14px] text-secondary">badge</span>
          <span>Insp. Rajesh K. Shekhawat</span>
        </div>
      </div>
      <div>
        <div class="font-label-caps text-[10px] text-on-surface-variant uppercase">Victim Primary UTR</div>
        <div id="dashVictimUTR" class="font-label-code-md text-[12px] text-secondary font-mono font-bold">UTR-2024-RJ-894102</div>
      </div>
      <div>
        <div class="font-label-caps text-[10px] text-on-surface-variant uppercase">Initial Victim Outflow</div>
        <div id="dashVictimAmount" class="font-label-code-md text-[13px] text-error font-bold">₹1,00,000 <span class="font-body-sm text-[10px] text-on-surface-variant font-normal">(1 Deposit)</span></div>
      </div>
    </div>
  </div>

  <!-- Row 1: Calculated Forensic KPIs -->
  <div class="grid grid-cols-1 md:grid-cols-5 gap-2.5 mb-3">
    <!-- Total Defrauded -->
    <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant flex flex-col justify-between">
      <div class="flex items-center justify-between text-on-surface-variant mb-1">
        <span class="font-label-caps text-[10px] uppercase">Reported Fraud</span>
        <span class="material-symbols-outlined text-[16px] text-error">trending_down</span>
      </div>
      <div>
        <div id="kpiTotalDefrauded" class="font-headline-xl text-[22px] font-bold text-on-surface">₹1,00,000</div>
        <div class="font-label-code-sm text-[11px] text-on-surface-variant">Source: <span class="font-semibold text-on-surface">HDFC (Acc ****8231)</span></div>
      </div>
      <div class="mt-2 pt-1 flex items-center justify-between text-[10px] font-label-code-sm text-on-surface-variant bg-surface-container-low px-1.5 py-0.5 rounded">
        <span>NCRP TICKET</span>
        <span class="text-secondary font-semibold">#NCRP-RJ-9821</span>
      </div>
    </div>

    <!-- Traced Outflow -->
    <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant flex flex-col justify-between">
      <div class="flex items-center justify-between text-on-surface-variant mb-1">
        <span class="font-label-caps text-[10px] uppercase">Traced Movement</span>
        <span class="material-symbols-outlined text-[16px] text-secondary">account_tree</span>
      </div>
      <div>
        <div id="kpiTracedAmount" class="font-headline-xl text-[22px] font-bold text-on-surface">₹1,00,000</div>
        <div class="mt-0.5 flex items-center gap-1.5">
          <span class="px-1 py-0.2 rounded bg-surface-container text-secondary font-label-code-sm text-[10px] font-bold">100% Traced</span>
          <span class="font-body-sm text-[10px] text-on-surface-variant">3 Discrete Layers</span>
        </div>
      </div>
      <div class="mt-2 pt-1">
        <div class="w-full bg-surface-container rounded-full h-1.5 overflow-hidden">
          <div class="bg-secondary h-1.5 rounded-full" style="width: 100%"></div>
        </div>
      </div>
    </div>

    <!-- Active Mule Accounts -->
    <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant flex flex-col justify-between">
      <div class="flex items-center justify-between text-on-surface-variant mb-1">
        <span class="font-label-caps text-[10px] uppercase">Identified Mule Nodes</span>
        <span class="material-symbols-outlined text-[16px] text-amber-500">hub</span>
      </div>
      <div>
        <div id="kpiMuleNodes" class="font-headline-xl text-[22px] font-bold text-on-surface">6 <span class="font-headline-sm text-[13px] text-on-surface-variant font-normal">Accounts</span></div>
        <div class="font-body-sm text-[10px] text-on-surface-variant">1 Collector • 2 Layer • 3 Terminal</div>
      </div>
      <div class="mt-2 pt-1 flex items-center gap-1 font-label-code-sm text-[9px]">
        <span class="px-1 rounded bg-error/10 text-error font-semibold">1 L-1</span>
        <span class="px-1 rounded bg-amber-500/10 text-amber-600 font-semibold">2 L-2</span>
        <span class="px-1 rounded bg-surface-container text-on-surface-variant font-semibold">3 L-3</span>
      </div>
    </div>

    <!-- Actionable Residual Exposure -->
    <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border-2 border-error/40 flex flex-col justify-between">
      <div class="flex items-center justify-between text-on-surface-variant mb-1">
        <span class="font-label-caps text-[10px] uppercase text-error font-bold">Actionable Residual</span>
        <span class="material-symbols-outlined text-[16px] text-error">lock_clock</span>
      </div>
      <div>
        <div id="kpiResidualAmount" class="font-headline-xl text-[22px] font-bold text-error">₹1,00,000</div>
        <div class="font-body-sm text-[10px] text-on-surface-variant">Parked across <span class="font-semibold text-on-surface">6 freeze targets</span></div>
      </div>
      <div class="mt-2 pt-1">
        <button onclick="navigateTo('freeze-priority-engine')" class="w-full py-0.5 bg-error hover:bg-error/90 text-white rounded font-label-caps text-[10px] tracking-wider uppercase transition-opacity flex items-center justify-center gap-1">
          <span class="material-symbols-outlined text-[12px]">gavel</span>
          <span>Draft Freeze Orders</span>
        </button>
      </div>
    </div>

    <!-- Cyber Infrastructure Footprint -->
    <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant flex flex-col justify-between">
      <div class="flex items-center justify-between text-on-surface-variant mb-1">
        <span class="font-label-caps text-[10px] uppercase">Infra Footprint</span>
        <span class="material-symbols-outlined text-[16px] text-secondary">lan</span>
      </div>
      <div>
        <div id="kpiInfraSummary" class="font-headline-xl text-[22px] font-bold text-on-surface">3 <span class="font-headline-sm text-[13px] text-on-surface-variant font-normal">Domains</span></div>
        <div class="font-label-code-sm text-[10px] text-on-surface-variant">1 Tor Node • 2 Cloudflare • 2 Cross-Links</div>
      </div>
      <div class="mt-2 pt-1 flex items-center justify-between font-label-code-sm text-[10px] text-on-surface-variant">
        <span>SYNDICATE LINKS</span>
        <span class="text-secondary font-bold">2 FIRs MATCHED</span>
      </div>
    </div>
  </div>

  <!-- Operational Two-Column Dashboard (7 / 5 Grid) -->
  <div class="grid grid-cols-1 lg:grid-cols-12 gap-3">
    <!-- Left Column: Money Trail Snapshot & Actionable Queue -->
    <div class="lg:col-span-7 flex flex-col gap-3">
      <!-- Quick Traced Fund Distribution Panel -->
      <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant">
        <div class="flex items-center justify-between pb-2 border-b border-outline-variant mb-2">
          <div class="flex items-center gap-1.5">
            <span class="material-symbols-outlined text-secondary text-[18px]">account_tree</span>
            <span class="font-headline-sm text-[14px] font-bold text-on-surface">Chronological Money Trail Snapshot</span>
          </div>
          <button onclick="navigateTo('money-trail-analysis')" class="text-secondary text-[11px] font-label-code-sm hover:underline flex items-center gap-0.5">
            <span>Open Interactive Graph</span>
            <span class="material-symbols-outlined text-[13px]">arrow_forward</span>
          </button>
        </div>

        <!-- Money Trail Flow Breadcrumb -->
        <div class="p-2.5 bg-surface-container-low rounded border border-outline-variant text-[11px] font-mono space-y-2">
          <div class="flex items-center justify-between">
            <span class="px-2 py-0.5 bg-blue-100 text-blue-900 font-bold rounded">Victim Deposit</span>
            <span class="text-on-surface font-bold">₹1,00,000 (10:00:15 IST)</span>
            <span class="text-secondary font-mono">UTR-2024-RJ-894102</span>
          </div>
          <div class="pl-4 border-l-2 border-secondary space-y-1.5">
            <div class="flex items-center justify-between">
              <span>↳ <strong>Acc A</strong> (Kotak 9182736450 - Ashok Verma)</span>
              <span class="text-error font-semibold">- ₹90,000 routed</span>
              <span class="text-emerald-700 font-bold">Retains ₹10,000</span>
            </div>
            <div class="pl-4 border-l-2 border-slate-300 space-y-1">
              <div class="flex items-center justify-between">
                <span>↳ <strong>Acc B</strong> (ICICI 4091823719 - Devendra Singh)</span>
                <span class="text-error">- ₹65,000 routed</span>
                <span class="text-emerald-700 font-bold">Retains ₹5,000</span>
              </div>
              <div class="pl-4 border-l-2 border-amber-300 space-y-0.5 text-[10px]">
                <div class="flex items-center justify-between">
                  <span>↳ <strong>Acc D</strong> (Axis 1192837465 - Suresh Traders)</span>
                  <span class="text-error font-bold">PARKED ₹50,000</span>
                  <span class="px-1 bg-red-100 text-red-800 rounded font-bold">TOP FREEZE PRIORITY</span>
                </div>
                <div class="flex items-center justify-between">
                  <span>↳ <strong>Acc E</strong> (HDFC 8829103948 - Vikash Cloud)</span>
                  <span class="text-error font-bold">PARKED ₹15,000</span>
                  <span class="px-1 bg-amber-100 text-amber-800 rounded">SHARED WITH FIR 119</span>
                </div>
              </div>
              <div class="flex items-center justify-between mt-1">
                <span>↳ <strong>Acc C</strong> (SBI 5519283746 - Manoj Meena)</span>
                <span class="text-error">- ₹15,000 routed</span>
                <span class="text-emerald-700 font-bold">Retains ₹5,000</span>
              </div>
              <div class="pl-4 border-l-2 border-amber-300 text-[10px]">
                <div class="flex items-center justify-between">
                  <span>↳ <strong>Acc F</strong> (Yes Bank 7738291045 - Royal Ent)</span>
                  <span class="text-error font-bold">PARKED ₹15,000</span>
                  <span class="px-1 bg-red-100 text-red-800 rounded">LAYER 3 SINK</span>
                </div>
              </div>
            </div>
          </div>
          <div class="pt-1.5 border-t border-outline-variant flex items-center justify-between text-[11px] font-bold text-slate-800">
            <span>CONSERVATION AUDIT: ₹10k + ₹5k + ₹50k + ₹15k + ₹5k + ₹15k</span>
            <span class="text-emerald-700">₹1,00,000 (100% Accounted / ₹0 Loss)</span>
          </div>
        </div>
      </div>

      <!-- Actionable Freeze Priority Table -->
      <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant">
        <div class="flex items-center justify-between pb-2 border-b border-outline-variant mb-2">
          <div class="flex items-center gap-1.5">
            <span class="material-symbols-outlined text-error text-[18px]">lock_clock</span>
            <span class="font-headline-sm text-[14px] font-bold text-on-surface">Immediate Freeze Directives Queue</span>
          </div>
          <button onclick="navigateTo('freeze-priority-engine')" class="text-secondary text-[11px] font-label-code-sm hover:underline">View All Accounts</button>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full text-left text-[12px]">
            <thead class="bg-surface-container text-on-surface-variant font-label-caps text-[10px]">
              <tr>
                <th class="py-1.5 px-2">Account No</th>
                <th class="py-1.5 px-2">Bank</th>
                <th class="py-1.5 px-2">Holder / Entity</th>
                <th class="py-1.5 px-2 text-right">Residual Exposure</th>
                <th class="py-1.5 px-2 text-center">Risk</th>
                <th class="py-1.5 px-2 text-center">Action</th>
              </tr>
            </thead>
            <tbody id="dashFreezeQueueTbody" class="divide-y divide-outline-variant/60">
              <!-- Rendered dynamically -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Right Column: Infrastructure Intelligence & Cross-Case Correlator -->
    <div class="lg:col-span-5 flex flex-col gap-3">
      <!-- Digital Infrastructure Footprint -->
      <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant">
        <div class="flex items-center justify-between pb-2 border-b border-outline-variant mb-2">
          <div class="flex items-center gap-1.5">
            <span class="material-symbols-outlined text-secondary text-[18px]">dns</span>
            <span class="font-headline-sm text-[14px] font-bold text-on-surface">Syndicate Digital Infrastructure</span>
          </div>
          <button onclick="navigateTo('domain-and-ip-intelligence')" class="text-secondary text-[11px] font-label-code-sm hover:underline">Deep Lookup</button>
        </div>
        <div class="space-y-2">
          <div class="p-2 bg-surface-container-low rounded border border-outline-variant">
            <div class="flex items-center justify-between">
              <span class="font-mono text-[12px] font-bold text-on-surface">secure-invest-rajasthan.xyz</span>
              <span class="px-1.5 py-0.2 bg-red-100 text-red-800 text-[9px] font-mono font-bold rounded">TOR NODE</span>
            </div>
            <div class="text-[11px] text-on-surface-variant mt-1 flex items-center justify-between">
              <span>IP: <strong class="text-on-surface font-mono">185.220.101.45</strong> (AS9009 M247 Ltd)</span>
              <span>Offshore Proxy</span>
            </div>
          </div>
          <div class="p-2 bg-surface-container-low rounded border border-outline-variant">
            <div class="flex items-center justify-between">
              <span class="font-mono text-[12px] font-bold text-on-surface">kyc-verify-portal.net</span>
              <span class="px-1.5 py-0.2 bg-amber-100 text-amber-800 text-[9px] font-mono font-bold rounded">CROSS-CASE LINK</span>
            </div>
            <div class="text-[11px] text-on-surface-variant mt-1 flex items-center justify-between">
              <span>IP: <strong class="text-on-surface font-mono">104.21.48.192</strong> (Cloudflare)</span>
              <span>FIR 072 Match</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Cross-Case Intelligence Matrix -->
      <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant">
        <div class="flex items-center justify-between pb-2 border-b border-outline-variant mb-2">
          <div class="flex items-center gap-1.5">
            <span class="material-symbols-outlined text-amber-500 text-[18px]">share</span>
            <span class="font-headline-sm text-[14px] font-bold text-on-surface">Cross-Case Correlations</span>
          </div>
          <span class="px-1.5 py-0.2 bg-amber-500/20 text-amber-600 font-label-code-sm text-[10px] font-bold rounded">2 LINKED FIRS</span>
        </div>
        <div class="space-y-2 text-[12px]">
          <div class="p-2 bg-amber-50/50 rounded border border-amber-200">
            <div class="flex items-center justify-between">
              <span class="font-bold text-amber-900">FIR No. 072/2024 (Jodhpur)</span>
              <span class="px-1 bg-red-600 text-white text-[9px] font-bold rounded">EXACT ACCOUNT MATCH</span>
            </div>
            <div class="mt-1 text-[11px] text-slate-700">
              Shared Mule: <strong class="font-mono">1192837465</strong> (Suresh Traders, Axis Bank)
            </div>
          </div>
          <div class="p-2 bg-blue-50/50 rounded border border-blue-200">
            <div class="flex items-center justify-between">
              <span class="font-bold text-blue-900">FIR No. 119/2024 (Kota)</span>
              <span class="px-1 bg-amber-600 text-white text-[9px] font-bold rounded">INFRASTRUCTURE MATCH</span>
            </div>
            <div class="mt-1 text-[11px] text-slate-700">
              Shared Mule: <strong class="font-mono">8829103948</strong> + Shared Proxy IP <strong class="font-mono">185.220.101.45</strong>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Investigation Actions -->
      <div class="bg-surface-container-lowest rounded-lg p-3 shadow-sm border border-outline-variant">
        <div class="font-headline-sm text-[14px] font-bold text-on-surface mb-2">Rapid Forensic Actions</div>
        <div class="grid grid-cols-2 gap-2 text-[11px]">
          <button onclick="navigateTo('bank-statement-ingestion')" class="p-2 bg-surface-container hover:bg-surface-container-high rounded border border-outline-variant flex items-center gap-1.5 font-medium transition-colors">
            <span class="material-symbols-outlined text-[16px] text-secondary">upload_file</span>
            <span>Ingest Bank PDF/XLSX</span>
          </button>
          <button onclick="navigateTo('money-trail-analysis')" class="p-2 bg-surface-container hover:bg-surface-container-high rounded border border-outline-variant flex items-center gap-1.5 font-medium transition-colors">
            <span class="material-symbols-outlined text-[16px] text-amber-500">search</span>
            <span>Trace Victim UTR</span>
          </button>
          <button onclick="navigateTo('lawful-requests')" class="p-2 bg-surface-container hover:bg-surface-container-high rounded border border-outline-variant flex items-center gap-1.5 font-medium transition-colors">
            <span class="material-symbols-outlined text-[16px] text-error">assignment_late</span>
            <span>Issue Sec 91 Notice</span>
          </button>
          <button onclick="navigateTo('reports-and-evidence')" class="p-2 bg-surface-container hover:bg-surface-container-high rounded border border-outline-variant flex items-center gap-1.5 font-medium transition-colors">
            <span class="material-symbols-outlined text-[16px] text-slate-700">download</span>
            <span>Export Case PDF/Excel</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</section>
"""

print("Views HTML part 1 loaded.")
