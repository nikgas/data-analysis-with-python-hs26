import pymupdf
from pathlib import Path

folder = Path("C:/Users/floba/OneDrive - Universität Zürich UZH/HS26/data_analysis_with_python/data-analysis-with-python-hs26/week_2/pdf_folder")

for pdf in folder.rglob("*.pdf"):
    png_folder = pdf.parent / f"{pdf.stem}_png"
    if not png_folder.exists():
        png_folder.mkdir()
        with pymupdf.open(pdf) as pdf_file:
            for i, page in enumerate(pdf_file):
                pix = page.get_pixmap(dpi=300)
                pix.save(f"{png_folder}/page-{i}.png")