import pymupdf
from pathlib import Path

folder = Path("C:/Users/floba/OneDrive - Universität Zürich UZH/HS26/data_analysis_with_python/data-analysis-with-python-hs26/week_2/pdf_folder")

for pdf in folder.glob("*.pdf"):
    pdf_folder = folder.parent / pdf.stem
    pdf_folder.mkdir()
    pdf_file = pymupdf.open(pdf)
    for i, page in enumerate(pdf_file):
       pix = page.get_pixmap(dpi=300)
       pix.save(f"{pdf_folder}/page-{i}.png")
pdf_file.close()