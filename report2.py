import pdfkit
import os
from bs4 import BeautifulSoup
import pandas as pd
import pytz
from datetime import datetime

UTC = pytz.utc
datetime_utc = datetime.now(UTC)
footer_left = 'Report Run by & on: Administrator on ' + datetime_utc.strftime('%d-%b-%Y %H:%M:%S') + ' GMT'

df = pd.read_excel('Agila.xlsx')
df1 = pd.read_excel('Agila.xlsx')
df.dropna(inplace=True)
df1.dropna(inplace=True)
df = df.set_index("E")["F"].to_frame().T
df.reset_index(drop=True, inplace=True)

def get_value(col):
    return df1[col].values[0] if col in df1.columns else ""

pr_id = get_value("A")
project = get_value("B")
pr_state = get_value("C")
division = get_value("D")
HEADER_FILE1 = os.path.abspath("header.html").replace("\\", "/")
def inplace_change(filename, old_string, new_string): 
    with open(filename) as f: 
        s = f.read() 
    with open(filename, 'w') as f: 
        s = s.replace(old_string, new_string) 
        f.write(s)
inplace_change(HEADER_FILE1,"#prid",f"{pr_id}")
inplace_change(HEADER_FILE1,"#project",f"{project}")
inplace_change(HEADER_FILE1,"#division",f"{division}")
inplace_change(HEADER_FILE1,"#prstate",f"{pr_state}")


# ------------------------------------------------------------------
# 1. Paths (absolute = safe)
# ------------------------------------------------------------------
path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# HEADER_FILE = os.path.abspath("header.html")  # ABSOLUTE PATH
HEADER_FILE = "file:///" + os.path.abspath("header.html").replace("\\", "/")
LOGO_PATH   = os.path.abspath(r"C:\Users\Harsh Agrawal\Documents\REPORT\download.png")
LOGO_URL    = f"file:///{LOGO_PATH.replace(os.sep, '/')}"

# ------------------------------------------------------------------
# 2. Generate PDF
# ------------------------------------------------------------------
def generate_pdf(division, project, pr_id, pr_state, run_date):
    
    options = {
        "page-size": "A4",
        "margin-top": "43mm",
        "margin-right": "5mm",
        "margin-bottom": "10mm",
        "margin-left": "5mm",

        # HEADER
        "header-html": HEADER_FILE,       # ABSOLUTE PATH
        "header-spacing": "5",

        # MISC
        "enable-local-file-access": None,
        "dpi": 185,
        "zoom": 1.0,
        "disable-smart-shrinking": "",
        'footer-left':footer_left,
        'footer-font-size':'6',
        'header-font-size':'6',
        "encoding": "UTF-8",
        "lowquality": None

        # IN-PLACE REPLACEMENT (dynamic values)
    }
    open("body.html", "w", encoding="utf-8").close()
    f1 = open("body.html","a",encoding='utf-8')
    f1.write(f'''<style>
* {{
  font-family: Calibri, sans-serif !important;
  font-size: 8px !important;
}}
table, td, th, p, span, b {{
  font-size: 8px !important;
}}
</style>''')
    for index, row in df.iterrows():
        for column in df.columns:
            f1 = open("body.html","a",encoding='utf-8')
            f1.write(f"<b>{column}:</b>")
            f1.write(f"<br>")
            f1.write(f"{row[column]}\n")
    pdfkit.from_file(
        "body.html",
        "flexfield_report.pdf",
        configuration=config,
        options=options
    )
    print(f"PDF generated: {os.path.abspath('flexfield_report.pdf')}")


# ------------------------------------------------------------------
# 3. Run
# ------------------------------------------------------------------
if __name__ == "__main__":
    generate_pdf(
        division="Weesp",
        project="Change Request",
        pr_id="31471",
        pr_state="Closed",
        run_date="27 October 2025, 06:07 PM (GMT)"
    )