# MULENET — Evaluator & User Manual
### Financial Crime Intelligence & Money-Trail Analysis Platform
**Developed for the Rajasthan Police Hackathon by Team TechTonicX**  
**Team Leader:** Kameshwar | **Team Members:** Balaji S, Dharani T, A Daria, Kameshwar  
**Platform Version:** 4.2-Forensic  
**Core Doctrine:** *"Follow the Money. Find the Infrastructure. Prioritise Action."*  
**Application Entry Point:** [`index.html`](index.html) (Single-file offline-ready executable)

---

## 1. Executive Summary for Evaluators

**MuleNet** is an end-to-end financial cybercrime intelligence platform designed specifically for the **Rajasthan Police Cyber Crime Investigation Division**. It bridges the gap between fragmented bank statements, digital communication traces, and urgent field actions.

Rather than presenting static dashboards or mockups, MuleNet provides **mathematically functional analytical engines** directly in the browser:
1. **Multi-Bank Statement Normalization & Reconciliation Engine:** Mathematically proves $\text{Opening Balance} + \sum \text{Credits} - \sum \text{Debits} = \text{Closing Balance}$ and flags discrepancies at the row level.
2. **Chronological Money-Trail Tracing Engine:** Enforces temporal precedence (pre-fund debits are excluded), conserves funds with $0\%$ leakage, and reconstructs multi-hop layering up to Layer 3 sinks via an interactive **Cytoscape.js** network graph.
3. **Explainable Mule Detection Engine:** Evaluates accounts against 8 configurable heuristic rules with transparent score breakdowns.
4. **Freeze-Priority Engine:** Calculates immediate actionable residual exposure to prevent funds from being cashed out.
5. **Cross-Case Syndicate Correlator:** Automatically detects shared mule accounts, phishing domains, and bulletproof Tor exit nodes across multiple FIRs.
6. **Court-Ready Evidentiary Outputs:** Generates official **Section 91 CrPC freeze notices**, downloadable **Forensic PDF case reports** with Rajasthan Police letterheads, and **9-sheet Excel workbooks**.

---

## 2. Quick Start Guide (Zero Installation)

1. **No Backend Required:** MuleNet runs entirely in client-side modern JavaScript.
2. **Launch:** Double-click [`index.html`](index.html) or open it in any modern browser (**Google Chrome**, **Microsoft Edge**, **Mozilla Firefox**, or **Brave**).
3. **Offline Operation:** All core tracing algorithms, synthetic datasets, PDF generators, Excel exporters, and cryptographic hash routines operate **100% offline**.

---

## 3. Evaluator 3-Minute Quick Tour

For hackathon judges with limited time, follow these three high-impact interactions:

### ⚡ Action 1: Run the 11-Step Interactive Guided Demo
- Click the amber **`GUIDED DEMO`** button in the top navigation bar.
- A floating controller will appear at the bottom of the screen.
- Click **`NEXT STEP ›`** to walk through the entire investigative workflow:
  * *Step 1:* Review Victim Complaint (FIR No. 104/2024, ₹1,00,000 fraud).
  * *Step 2 & 3:* Ingest statements and detect a deliberate reconciliation error in Row 4 of the SBI statement.
  * *Step 4:* Inspect 8 explainable heuristic rules on flagged mule accounts.
  * *Step 5 & 6:* Trace victim UTR `UTR-2024-RJ-894102` through multi-hop branches using the interactive Cytoscape network graph and playback slider.
  * *Step 7:* Rank accounts by residual balance (Axis Bank Account D holds ₹50,000).
  * *Step 8 & 9:* Perform passive domain/IP OSINT and uncover cross-case links to Jodhpur and Kota FIRs.
  * *Step 10 & 11:* Generate an official forensic PDF report and draft a Section 91 CrPC freeze directive.

### 🧪 Action 2: Inspect Live Automated Self-Tests
- Click the **`SELF-TESTS`** button in the header.
- MuleNet will run 6 live unit tests verifying:
  1. *Reconciliation Balance Equation*
  2. *Chronological Attribution Constraint* (Pre-fund exclusion)
  3. *Fund Conservation Law* ($\text{Victim} = \text{Residual} + \text{Outflow}$)
  4. *Rule Scoring Normalization* ($0 \le \text{Score} \le 100$)
  5. *Cross-Case Syndicate Identifier Matching*
  6. *Evidence SHA-256 Cryptographic Consistency*

### 📥 Action 3: Download Forensic Outputs
- Navigate to **Reports & Evidence** in the left sidebar:
  * Click **`DOWNLOAD FORENSIC CASE REPORT (PDF)`** to get the official police report.
  * Click **`EXPORT 9-SHEET EXCEL WORKBOOK`** to inspect the full structured dataset.
- Navigate to **Sec 91 CrPC Requests**:
  * Click **`DOWNLOAD SIGNED NOTICE (PDF)`** to review the ready-to-issue legal freeze order.

---

## 4. Detailed Feature Guide

### 4.1 Global Header & Operational Controls
- **Case Selector:** Switch between three loaded synthetic cases:
  - `FIR 104/2024` (Jaipur South — Telegram Ponzi Scam)
  - `FIR 072/2024` (Jodhpur — Work-from-Home Job Phishing)
  - `FIR 119/2024` (Kota — Instant Loan App Harassment)
- **Global Search:** Type any keyword (e.g., `1192837465`, `secure-invest`, `894102`, `185.220`) into the search bar to jump directly to the relevant account, transaction, or infrastructure record.
- **Evidentiary Hash Seal:** Displays the current case cryptographic integrity hash calculated under Section 65B of the Indian Evidence Act / Bharatiya Sakshya Adhiniyam (BSA).

---

### 4.2 Bank Statement Ingestion & Reconciliation Engine
*Location: Left Sidebar → Bank Statement Ingestion*
- **Drag-and-Drop Dropzone:** Accepts `.csv`, `.xlsx`, `.xls`, `.pdf`, and `.json` statement files.
- **1-Click Load:** Click **`1-CLICK LOAD DEMO STATEMENTS`** to instantly populate normalized transactions from Kotak, ICICI, and SBI.
- **Reconciliation Audit Panel:** Evaluates:
  $$\text{Opening Balance} + \sum \text{Credits} - \sum \text{Debits} = \text{Closing Balance}$$
  - **Kotak Bank (Account A):** Balanced and reconciled ($\checkmark$).
  - **ICICI Bank (Account B):** Balanced and reconciled ($\checkmark$).
  - **SBI Bank (Account C):** **MISMATCH FLAGGED ($\triangle$)** on Row 4 where an unverified balance jump of ₹20,000 was deliberately planted in synthetic data to demonstrate anomaly detection.
- **Sample Files:** Evaluators can download the raw sample CSV files from the right-hand panel or [`sample_data/`](sample_data) directory and drag them back into the dropzone.

---

### 4.3 Mule Account Detection & Explainability
*Location: Left Sidebar → Mule Account Detection*
- **Detection Algorithm:** 8 explainable heuristic rules:
  | Rule | Default Weight | Condition |
  | :--- | :---: | :--- |
  | **Rapid In-Out Transfer** | 20 | Inflow moved outward within 2 hours (>70% of value) |
  | **Many-to-One Credits** | 15 | 3+ distinct counterparties crediting within 24 hours |
  | **Round-Figure Layering** | 10 | Repeated transfers in round multiples of ₹1,000 / ₹5,000 |
  | **Dormant-to-Active Spike**| 15 | High velocity after >30 days inactivity |
  | **Repeated Counterparties**| 10 | Recurring counterparties across accounts or FIRs |
  | **High Velocity** | 10 | $\ge 4$ transactions in a 3.5-hour window |
  | **Pass-Through Ratio** | 10 | Outflow/Inflow ratio between 70% and 105% |
  | **Cross-Case Match** | 10 | Entity detected in more than one police case FIR |
- **Explainability Drawer:** Click on any row in the **Flagged Mule Account Registry** (e.g., `9182736450` or `1192837465`) to open the right-hand inspection drawer. It details:
  - Exact composite score ($0 - 100$).
  - Specific rule points contributing to the score.
  - Cited supporting transaction rows and timestamps.
  - Recommended statutory next steps.

---

### 4.4 Money-Trail Tracing Engine (Hero Feature)
*Location: Left Sidebar → Money Trail Analysis*
- **Strict Chronological Precedence Test:**
  - Notice transaction `TXN-001` (ATM Cash Withdrawal of ₹25,000 from Account A at 08:15:00 IST).
  - The victim funds arrived at 10:00:15 IST (`TXN-002`).
  - **The engine correctly excludes `TXN-001` from the victim trail** because funds cannot be attributed to events that occurred before arrival.
- **Conservation of Funds:**
  - Victim deposits ₹1,00,000 into **Account A** (Kotak `9182736450`, Ashok Verma).
  - Account A routes:
    - ₹70,000 to **Account B** (ICICI `4091823719`, Devendra Singh)
    - ₹20,000 to **Account C** (SBI `5519283746`, Manoj Meena)
    - **Retains ₹10,000 residual.**
  - Account B routes:
    - ₹50,000 to **Account D** (Axis `1192837465`, Suresh Traders)
    - ₹15,000 to **Account E** (HDFC `8829103948`, Vikash Cloud)
    - **Retains ₹5,000 residual.**
  - Account C routes:
    - ₹15,000 to **Account F** (Yes Bank `7738291045`, Royal Enterprises)
    - **Retains ₹5,000 residual.**
  - **Attributable Residual Sum:** ₹10k + ₹5k + ₹5k + ₹50k + ₹15k + ₹15k = **₹1,00,000** (Zero leakage, 100% accounted).
- **Interactive Graph Features:**
  - **Zoom & Pan:** Use mouse wheel or top-left `+` / `-` controls.
  - **Reset Layout:** Returns nodes to standard hierarchy.
  - **Attribution Toggle:** Switch between **FIFO** and **Proportional** modes.
  - **Hop Filter:** Filter view by *Layer 1 (Collector)*, *Layer 2 (Layering)*, or *Layer 3 (Sinks)*.
  - **Timeline Playback Slider:** Drag the slider from Step 0 to Step 6 to watch the funds travel step-by-step across Jaipur, Jodhpur, and Bhiwadi.
  - **Export Graph:** Downloads a high-resolution PNG snapshot of the money trail.

---

### 4.5 Freeze-Priority Intelligence Engine
*Location: Left Sidebar → Freeze-Priority Engine*
- Ranks accounts by urgency of statutory debit freeze based on remaining residual balance:
  1. **Rank #1 (Immediate):** Axis Bank `1192837465` (Suresh Traders) — **₹50,000 residual parked**
  2. **Rank #2 (Immediate):** HDFC Bank `8829103948` (Vikash Cloud) — **₹15,000 residual parked**
  3. **Rank #3 (Immediate):** Yes Bank `7738291045` (Royal Enterprises) — **₹15,000 residual parked**
  4. **Rank #4 (High):** Kotak Bank `9182736450` (Ashok Verma) — **₹10,000 residual retained**
  5. **Rank #5 (High):** ICICI Bank `4091823719` (Devendra Singh) — **₹5,000 residual retained**
  6. **Rank #6 (High):** SBI Bank `5519283746` (Manoj Meena) — **₹5,000 residual retained**
- **Action Triggers:** Click **`Freeze`** on any row to automatically pre-fill a Section 91 CrPC notice for that specific bank and branch manager.

---

### 4.6 Digital & Infrastructure Intelligence (OSINT)
*Location: Left Sidebar → Domain & IP Intelligence*
- **Target Analysis:** Passive reconnaissance on `secure-invest-rajasthan.xyz`.
- **Infrastructure Hierarchy:**
  $$\text{Domain: secure-invest-rajasthan.xyz} \longrightarrow \text{A Record} \longrightarrow \text{IP: 185.220.101.45} \longrightarrow \text{ASN: AS9009 (M247 Ltd)} \longrightarrow \text{Offshore Tor Exit Node}$$
- **Threat Indicator:** High-risk bulletproof hosting located in Romania used for Telegram-based investment scams and malicious APK distribution.

---

### 4.7 Cross-Case Syndicate Correlator
*Location: Left Sidebar → Cross-Case Intelligence*
- Automatically correlates entities across the 3 state FIRs:
  - **Exact Account Match (Strong):** Axis Bank `1192837465` is identified in both **FIR 104/2024 (Jaipur South)** and **FIR 072/2024 (Jodhpur)**.
  - **Direct Domain Match (Direct):** Phishing domain `kyc-verify-portal.net` was used in both the Jaipur and Jodhpur cases.
  - **Shared Server IP (Contextual):** IP `185.220.101.45` hosts infrastructure for both the Jaipur investment scam and the **FIR 119/2024 (Kota)** loan extortion ring.

---

### 4.8 Reports & Evidentiary Vault
*Location: Left Sidebar → Reports & Evidence*
- **Cryptographic Hashes:** Shows SHA-256 digests for all uploaded CSV statements.
- **Re-Verify All Hashes:** Re-runs browser-side Web Crypto hashing to prove files have not been tampered with.
- **PDF Export:** Generates an official case report ready for submission to senior supervisory officers or the court.
- **Excel Export:** Generates a 9-sheet comprehensive workbook containing:
  1. `Transactions`
  2. `Mule_Accounts`
  3. `Money_Trail`
  4. `Priority_List`
  5. `Digital_Infra`
  6. `Cross_Case_Matches`
  7. `Evidence_Register`
  8. `Audit_Log`

---

### 4.9 Statutory Lawful Information Requests (Section 91 CrPC)
*Location: Left Sidebar → Sec 91 CrPC Requests*
- Pre-formats legal notices under Section 91 CrPC / Section 94 BNSS:
  - Addressed to the Branch Manager / Nodal Officer of the target bank.
  - Auto-fills target account, beneficiary holder name, IFSC, transaction UTR, and exact residual exposure.
  - Mandates a debit freeze and production of Account Opening Forms (AOF), KYC dossiers, and IP session logs within 24 hours.
- **Actions:** **`COPY NOTICE TEXT`** and **`DOWNLOAD SIGNED NOTICE (PDF)`**.

---

### 4.10 Settings & Heuristic Calibration
*Location: Left Sidebar → Settings & Help*
- Allows investigators to adjust rule weights (Rapid in-out, Many-to-one, Dormancy, Velocity, etc.) and risk thresholds.
- Clicking **`SAVE & RECALCULATE ALL`** dynamically updates the scores across the entire platform.
- **Pristine Demo Reset:** Restores the platform to its clean initial state with one click.

---

## 5. Synthetic Dataset Reference Table

| Entity ID | Entity Type | Details / Bank / Registrar | Financial / Digital Role |
| :--- | :--- | :--- | :--- |
| **Rajesh Kumar Sharma** | Complainant / Victim | HDFC Bank `501004918231` | Victim of ₹1,00,000 Telegram Ponzi scam |
| **`UTR-2024-RJ-894102`** | Victim Primary UTR | IMPS Inflow (18 Oct 10:00:15 IST) | Root of money trail |
| **`9182736450`** (Acc A) | Mule Account | Kotak Mahindra Bank (Ashok Verma) | Layer 1 Primary Collector (₹10,000 retained) |
| **`4091823719`** (Acc B) | Mule Account | ICICI Bank (Devendra Singh) | Layer 2 Layering Account (₹5,000 retained) |
| **`5519283746`** (Acc C) | Mule Account | State Bank of India (Manoj Meena) | Layer 2 Layering Account (₹5,000 retained) |
| **`1192837465`** (Acc D) | Mule Account (Consolidator)| Axis Bank (Suresh Traders) | **Layer 3 Terminal Sink (₹50,000 parked)** • Shared with FIR 072/2024 |
| **`8829103948`** (Acc E) | Mule Account (Integration) | HDFC Bank (Vikash Cloud Sol) | **Layer 3 Terminal Sink (₹15,000 parked)** • Shared with FIR 119/2024 |
| **`7738291045`** (Acc F) | Mule Account (Integration) | Yes Bank (Royal Enterprises) | **Layer 3 Terminal Sink (₹15,000 parked)** |
| **`secure-invest-rajasthan.xyz`** | Phishing Domain | Namecheap Inc. | Fake trading portal (IP: 185.220.101.45) |
| **`kyc-verify-portal.net`** | Phishing Domain | Public Domain Registry / Cloudflare | Phishing credential harvester (FIR 104 & 072) |
| **`185.220.101.45`** | Server IPv4 | AS9009 (M247 Ltd) Romania | Tor Exit Node & bulletproof hosting proxy |

---

## 6. Self-Test Mathematical Verification Matrix

Evaluators can verify the integrity of MuleNet by clicking the **`SELF-TESTS`** button:

| # | Test Name | Formula / Verification Rule | Expected Result |
| :---: | :--- | :--- | :--- |
| **1** | Statement Reconciliation | $\text{Opening} + \sum \text{Credits} - \sum \text{Debits} == \text{Closing}$ | **PASSED** (Mathematical equation holds) |
| **2** | Chronological Attribution | Pre-fund debit ($t < t_{\text{victim}}$) excluded | **PASSED** (`TXN-001` excluded from trail) |
| **3** | Fund Conservation Law | $\text{Victim Inflow} == \sum \text{Residual} + \text{Outflow}$ | **PASSED** (₹1,00,000 == ₹1,00,000, 0 error) |
| **4** | Risk Score Normalization | $0 \le \text{Score} \le 100$ for all nodes | **PASSED** (All scores normalized) |
| **5** | Cross-Case Syndicate Match | Exact identifier match across stored cases | **PASSED** (Axis Bank `1192837465` matched) |
| **6** | Cryptographic Hash Seal | SHA-256 64-char hex digest verification | **PASSED** (Web Crypto digests consistent) |

---

## 7. Recommended Production Architecture

To scale MuleNet from this single-file prototype to an enterprise-grade production platform across all 40+ police districts in Rajasthan, Team TechTonicX recommends:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        MULENET STATE PRODUCTION STACK                   │
├────────────────────────────────────────────────────────────────────────┤
│  FRONTEND (React + Vite + Tailwind CSS + Cytoscape.js)                 │
│  - High-density forensic dashboard                                     │
│  - Secure SSO authentication via Rajasthan Police SSO portal           │
├────────────────────────────────────────────────────────────────────────┤
│  API GATEWAY & MICROSERVICES (FastAPI / Python 3.12 + Go)              │
│  - Bank Statement Ingestion Worker (Celery + Redis queue)              │
│  - High-throughput PDF & OCR parsing (Tesseract v5 + LayoutLM)         │
│  - Tracing & Graph Processing Engine                                   │
├────────────────────────────────────────────────────────────────────────┤
│  DATABASE LAYER                                                        │
│  - Graph Database: Neo4j (Multi-hop mule network traversal & cycles)   │
│  - Relational Database: PostgreSQL with TimescaleDB (Financial ledger) │
│  - Object Storage: MinIO / S3 (Encrypted statement repository)        │
├────────────────────────────────────────────────────────────────────────┤
│  SECURITY & LEGAL CHAIN OF CUSTODY                                     │
│  - Hardware Security Module (HSM) for signing Sec 65B BSA certificates │
│  - Append-only cryptographic ledger for immutable officer audit trails │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Summary of Evaluator FAQ

**Q: Does this prototype require Node.js, Python, or an active web server to evaluate?**  
*A: No. It is an entirely self-contained single HTML file (`index.html`) that can be opened directly from disk in any web browser.*

**Q: Can I test my own statement data?**  
*A: Yes. You can drag and drop your own CSV or Excel bank statement into the Ingestion screen, or test with the three sample statements provided in `sample_data/`.*

**Q: What makes MuleNet technically superior to a standard dashboard?**  
*A: MuleNet has a real analytical pipeline. It enforces strict chronological ordering (never attributing money retroactively), balances total funds across multi-hop branches without double counting, and calculates actionable residual balances for immediate debit freezing.*

---
*MuleNet — Developed by Team TechTonicX for the Rajasthan Police Hackathon.*  
*Empowering Law Enforcement to turn fragmented evidence into prioritized action.*
