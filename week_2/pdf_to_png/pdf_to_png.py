import pymupdf
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from time import sleep

def pdf_to_png(pdf):
    # create folder for pngs
    png_folder = pdf.parent / f"{pdf.stem}_png"
    if not png_folder.exists():
        png_folder.mkdir()
    for attempt in range(2): # try twice: existing files should work the first time, newly created files need a delay
        try:
            with pymupdf.open(pdf) as pdf_file:
                # iterate through pdf pages and convert page by page to png
                for i, page in enumerate(pdf_file):
                    pix = page.get_pixmap(dpi=300)
                    pix.save(f"{png_folder}/page-{i}.png")
            break
        except pymupdf.FileDataError: 
            if attempt == 0:
                sleep(5) # delay

class MyHandler(FileSystemEventHandler):
    # if an event occurs
    def on_any_event(self, event):
        # check that event has not to do with a directory
        if not event.is_directory:
            # if a file has either been created or modified, save the path of the file and pass it to the pdf_to_png function
            if event.event_type in ("created", "modified"):
                pdf = Path(event.src_path)
                if pdf.suffix.lower() == ".pdf":
                    pdf_to_png(pdf)

folder = Path("C:/Users/floba/OneDrive - Universität Zürich UZH/HS26/data_analysis_with_python/data-analysis-with-python-hs26/week_2/pdf_to_png/pdf_folder")

handler = MyHandler()
observer = Observer()
observer.schedule(handler, folder, recursive=True) # recursive=True means that it also observes subfolders

# iterate through existing pdfs and convert them, before starting the observer
for pdf in folder.rglob("*.pdf"):
    pdf_to_png(pdf)

# start the observer
try:
    observer.start()
    observer.join()
except KeyboardInterrupt:
    observer.stop()
    observer.join() # use join again to make sure the observer thread terminates (differentiate carefully between observer thread and normal thread)