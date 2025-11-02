import os

# ✅ Add your GTK bin path here
os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")

from weasyprint import HTML

# Test PDF creation
HTML("body.html").write_pdf("weasy.pdf")
# print("✅ PDF created successfully!")