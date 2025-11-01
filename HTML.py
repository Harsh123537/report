from bs4 import BeautifulSoup
from fpdf import FPDF
from fpdf.enums import XPos, YPos  # ✅ modern replacement for deprecated ln
import pandas as pd
import bleach

# === Load Excel ===
df = pd.read_excel('Agila.xlsx')
df1 = pd.read_excel('Agila.xlsx')
df.dropna(inplace=True)
df1.dropna(inplace=True)
df = df.set_index("DataField_Name")["Text"].to_frame().T
df.reset_index(drop=True, inplace=True)

def get_value(col):
    return df1[col].values[0] if col in df1.columns else ""

pr_id = get_value("PR_ID")
project = get_value("Project")
pr_state = get_value("State")
division = get_value("Division")

# === PDF CLASS ===
class PDF(FPDF):
    def __init__(self, pr_id, project, pr_state, division, orientation='P', unit='mm', format='A4'):
        super().__init__(orientation, unit, format)
        self.pr_id = pr_id
        self.project = project
        self.pr_state = pr_state
        self.division = division

    def header(self):
        logo_path = "download.png"
        logo_width = 30
        page_width = self.w
        x_centered = (page_width - logo_width) / 2

        # Center logo
        self.image(logo_path, x=x_centered, y=10, w=logo_width)

        # Title
        self.set_y(30)
        self.set_font('Helvetica', 'B', 11)  # ✅ Helvetica replaces Arial
        self.set_text_color(91, 43, 130)
        self.cell(0, 10, "Flex Field Report", align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_text_color(0, 0, 0)

        # === Left & Right Data ===
        left_text = [
            f"Division: {self.division}",
            f"PR ID: {self.pr_id}"
        ]
        right_text = [
            f"Project: {self.project}",
            f"PR State: {self.pr_state}"
        ]

        start_y = 40
        left_x = 10
        right_x = 140

        for i in range(len(left_text)):
            # Left Side
            if ":" in left_text[i]:
                label, value = left_text[i].split(":", 1)
                self.set_xy(left_x, start_y + i * 6)
                self.set_font('Helvetica', 'B', 9)
                self.cell(22, 5, f"{label.strip()}:", new_x=XPos.RIGHT, new_y=YPos.TOP)
                self.set_font('Helvetica', '', 9)
                self.cell(40, 5, f"{value.strip()}", new_x=XPos.RIGHT, new_y=YPos.TOP)

            # Right Side
            if ":" in right_text[i]:
                label, value = right_text[i].split(":", 1)
                self.set_xy(right_x, start_y + i * 6)
                self.set_font('Helvetica', 'B', 9)
                self.cell(22, 5, f"{label.strip()}:", new_x=XPos.RIGHT, new_y=YPos.TOP)
                self.set_font('Helvetica', '', 9)
                self.cell(40, 5, f"{value.strip()}", new_x=XPos.RIGHT, new_y=YPos.TOP)

        # Horizontal line
        self.set_y(start_y + len(left_text) * 6 + 5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 10)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)


# === Create PDF ===
pdf = PDF(pr_id, project, pr_state, division, 'P', 'mm', 'A4')
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Use modern fonts
font_path_normal = "C:\\Windows\\Fonts\\arial.ttf"
font_path_bold = "C:\\Windows\\Fonts\\arialbd.ttf"
pdf.add_font("DejaVu", "", font_path_normal)
pdf.add_font("DejaVu", "B", font_path_bold)
pdf.set_font("DejaVu", size=10)

# === Add Table Data ===
for index, row in df.iterrows():
    for column in df.columns:
        pdf.set_font('DejaVu', 'B', 10)
        label = f"{column}:"
        label_width = pdf.get_string_width(label) + 2
        pdf.cell(label_width, 5, label, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.set_font('DejaVu', '', 10)
        clean_text = str(row[column])
        value = bleach.clean(clean_text, tags=[], strip=True)
        soup = BeautifulSoup(value, "html.parser")
        value = soup.get_text(separator="\n", strip=True)

        page_width = 190
        value_width = page_width - label_width - 10
        pdf.multi_cell(value_width, 5, value, align='L')
        y = pdf.get_y()
        pdf.line(10, y, 200, y)  # safe separator
        pdf.set_xy(10, y + 3)
    pdf.ln(2)
    pdf.cell(0, 0, border=1)
    pdf.ln(3)

pdf.output('report4.pdf')
