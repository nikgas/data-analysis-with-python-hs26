import pymupdf
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

folder = Path("C:/Users/floba/OneDrive - Universität Zürich UZH/HS26/data_analysis_with_python/data-analysis-with-python-hs26/week_2/pdf_folder")

def pdf_to_png(pdf):
    png_folder = pdf.parent / f"{pdf.stem}_png"
    if not png_folder.exists():
        png_folder.mkdir()
    with pymupdf.open(pdf) as pdf_file:
        for i, page in enumerate(pdf_file):
            pix = page.get_pixmap(dpi=300)
            pix.save(f"{png_folder}/page-{i}.png")

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if not event.is_directory:
            if event.event_type in ("created", "modified"):
                pdf = Path(event.src_path)
                if pdf.suffix.lower() == ".pdf":
                    pdf_to_png(pdf)

handler = MyHandler()

observer = Observer()
observer.schedule(handler, folder, recursive=True)
observer.start()
observer.join()