# Cisco Circuit Info Tool (Python + GUI)

This tool automates the extraction of circuit-related information from Cisco routers using SSH.  
It's designed to support SD-WAN migrations and WAN inventory audits by generating a fast, Excel-based overview of:

- Tunnel interfaces
- Private subinterfaces
- VRF assignments
- QoS blocks
- CDP neighbors (fallback)

---

## 🔧 Features

- ✅ GUI-based tool using PySide6
- 🔐 SSH access via Netmiko
- 📋 Reads router IPs from Excel
- 🧠 Intelligent parsing of tunnel, VRF, and private subinterface blocks
- 📤 Outputs a clean Excel file:
  - One column per device
  - Circuit descriptions and routing layout
- 💡 Optional: CDP-based discovery and fiber handoff hints

---

## 📸 Screenshot
<img width="884" height="593" alt="Screenshot 2025-07-24 184010" src="https://github.com/user-attachments/assets/d3e2ef05-1f5e-4879-a7da-c7a1cbcdf984" />




## 📂 Folder Structure

.
├── circuitinfo20.py # Main Python script
├── /inputs/ # Folder for input Excel IP list
├── /outputs/ # Folder for generated Excel report
├── requirements.txt # Python dependencies
└── README.md

Copy
Edit
📋 2. Requirements
Explain how to install dependencies.

markdown
Copy
Edit
## 📋 Requirements

- Python 3.8 or higher
- Install dependencies:
- pip install PySide6
pip install netmiko
pip install openpyxl
pip install pandas
pip install qdarkstyle


---

### 🚀 3. How to Use (step-by-step)

Clear steps to run the tool:

```markdown
## 🚀 How to Use

1. Run the script:
   ```bash
   python circuitinfo19.py
Select the Excel file with router IPs (IP column required)

Enter SSH credentials in the GUI prompt

Wait for the tool to extract data

Output Excel will appear in /outputs/

yaml
Copy
Edit

---

### 📘 4. Example Use Case

Shows what the tool is for in real life:

```markdown
## 📘 Example Use Case

A network engineer preparing for an SD-WAN migration needs:

- All tunnel and private circuit details
- VRF and routing info per site
- An Excel inventory to pass to deployment teams
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
SD-WAN Migration GUI Tool
A modern PySide6-based GUI application for network engineers to automate the extraction, mapping, and organization of WAN circuit data for SD-WAN migrations.
Designed to work with output from the Circuit Info Collector tool as part of a seamless migration workflow. 

Features
User-Friendly GUI:

Select source Circuit Info Excel workbook and Migration Planning workbook.

Output file selector for new Excel results.

Option to process all sheets, or a specific sheet only.

Configurable starting row.

Persistent user configuration (remembers your last settings).

Automation & Parsing:

Reads per-site and per-circuit data, extracting key details (provider, handoff, VLAN, bandwidth, interface descriptions, circuit IDs, IPs, peers).

Identifies public/private provider types using keywords and regex.

Auto-maps primary/secondary circuits into the migration planning sheet.

Cleans and normalizes circuit description fields.

Detects handoff type (fiber/copper), calculates subnet prefix, and peer IPs automatically.

Progress Tracking:

Live progress bar in the GUI.

Error handling and completion pop-up.

Professional Look:

Clean, modern interface using qdarkstyle.

Dependencies
Python 3.x

PySide6

openpyxl

qdarkstyle

How to Use
Launch the script:
python migv15.py

In the GUI:

Select your Circuit Info Workbook (output from Circuit Info Collector).

Select your Migration Planning Workbook (where to write results).

Choose whether to process all circuit sheets or just one.

Select the output file path.

Set your starting row if needed.

Click “Run Migration.”

On completion, open your output file to see the fully organized migration data.

Use Cases
Pre-migration planning:
Quickly map WAN circuits and details from multiple sites into a standardized migration planning workbook.

Bulk project automation:
Mass-processing of circuit info for SD-WAN cutovers, saving hours of manual work.

Consistent documentation:
Output is structured, normalized, and ready for handoff or further automation.

This tool is the recommended next step after running the Circuit Info Collector. Together, they form a complete workflow for SD-WAN and WAN migration inventory management.
This tool automates that — no manual CLI work required.

