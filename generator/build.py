# generator/build.py
import os
import json
import sys

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data import DATASET
from views_html import HEADER_HTML, SIDEBAR_HTML, VIEW_OVERVIEW
from views_part2 import VIEW_CASES, VIEW_INGESTION, VIEW_TRANSACTIONS, VIEW_MULE_DETECTION, VIEW_MONEY_TRAIL
from views_part3 import (
    VIEW_FREEZE_PRIORITY, VIEW_CYBER_INTEL, VIEW_RELATIONSHIP_GRAPH,
    VIEW_CROSS_CASE, VIEW_TIMELINE, VIEW_REPORTS_EVIDENCE,
    VIEW_LAWFUL_REQUESTS, VIEW_AUDIT_LOG, VIEW_SETTINGS, MODALS_HTML
)
from app_js import APP_JS

def build_index_html():
    print("Assembling index.html for MuleNet...")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>MULENET — Financial Crime Intelligence & Money-Trail Analysis Platform</title>

  <!-- Google Fonts & Material Symbols -->
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Public+Sans:wght@400;500;600;700&display=swap" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet"/>

  <!-- CDN Libraries for Network Graph, Excel Parsing/Export, PDF Generation -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.28.1/cytoscape.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.8.2/jspdf.plugin.autotable.min.js"></script>

  <!-- Tailwind Forensic Theme Configuration -->
  <script>
    tailwind.config = {{
      darkMode: "class",
      theme: {{
        extend: {{
          colors: {{
            primary: "#0B192C",
            "primary-container": "#0e1c2f",
            "on-primary-container": "#77849c",
            secondary: "#1D4ED8",
            "secondary-container": "#4069f2",
            "on-secondary-container": "#ffffff",
            tertiary: "#D97706",
            surface: "#F8FAFC",
            "surface-container-lowest": "#FFFFFF",
            "surface-container-low": "#EFF4FF",
            "surface-container": "#E2E8F0",
            "surface-container-high": "#CBD5E1",
            "on-surface": "#0F172A",
            "on-surface-variant": "#475569",
            "outline-variant": "#CBD5E1",
            outline: "#94A3B8",
            error: "#DC2626"
          }},
          fontFamily: {{
            sans: ["Public Sans", "sans-serif"],
            mono: ["JetBrains Mono", "monospace"]
          }}
        }}
      }}
    }};
  </script>

  <style>
    body {{
      font-family: 'Public Sans', sans-serif;
      background-color: #F8FAFC;
      color: #0F172A;
      overflow-x: hidden;
    }}
    code, pre, .font-mono {{
      font-family: 'JetBrains Mono', monospace;
      font-variant-numeric: tabular-nums;
    }}
    /* Clean custom scrollbar for forensic density */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #F1F5F9;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #CBD5E1;
      border-radius: 3px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #94A3B8;
    }}
    .animate-bounce-subtle {{
      animation: bounceSubtle 2s infinite ease-in-out;
    }}
    @keyframes bounceSubtle {{
      0%, 100% {{ transform: translateY(0); }}
      50% {{ transform: translateY(-4px); }}
    }}
    /* Fixed high-contrast hover states for dark sidebar */
    .nav-item {{
      color: #CBD5E1 !important;
      transition: background-color 0.15s ease, color 0.15s ease;
    }}
    .nav-item:hover {{
      background-color: #1E293B !important;
      color: #FFFFFF !important;
    }}
    .nav-item.active {{
      background-color: #1D4ED8 !important;
      color: #FFFFFF !important;
      font-weight: 600 !important;
    }}
  </style>
</head>
<body class="bg-surface text-on-surface antialiased text-[13px]">

  <!-- Global Header -->
  {HEADER_HTML}

  <!-- Left Sidebar Navigation -->
  {SIDEBAR_HTML}

  <!-- Main Operational Canvas -->
  <div class="pl-64">
    <main class="w-full pt-16 min-h-screen px-3 md:px-4 py-3 bg-surface">
      <!-- 15 Views -->
      {VIEW_OVERVIEW}
      {VIEW_CASES}
      {VIEW_INGESTION}
      {VIEW_TRANSACTIONS}
      {VIEW_MULE_DETECTION}
      {VIEW_MONEY_TRAIL}
      {VIEW_FREEZE_PRIORITY}
      {VIEW_CYBER_INTEL}
      {VIEW_RELATIONSHIP_GRAPH}
      {VIEW_CROSS_CASE}
      {VIEW_TIMELINE}
      {VIEW_REPORTS_EVIDENCE}
      {VIEW_LAWFUL_REQUESTS}
      {VIEW_AUDIT_LOG}
      {VIEW_SETTINGS}
    </main>
  </div>

  <!-- Modals and Overlays -->
  {MODALS_HTML}

  <!-- Seed Dataset -->
  <script>
    const SEED_DATA = {json.dumps(DATASET, indent=2)};
  </script>

  <!-- Application Logic & Engines -->
  <script>
    {APP_JS}
  </script>
</body>
</html>
"""

    output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Successfully generated {output_path} ({len(html)} bytes).")

if __name__ == "__main__":
    build_index_html()
