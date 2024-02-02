""" merge nested pdfs at script root """

from os.path import dirname,abspath,getmtime,basename,join
from subprocess import run
from glob import glob

try:
    from pypdf import PdfWriter # https://github.com/py-pdf/pypdf
except ModuleNotFoundError:
    run(["pip", "install", "pypdf"], check=True, shell=False)
    from pypdf import PdfWriter

SCRIPT_ROOT = abspath(dirname(__file__))
MERGE_FILE = basename(SCRIPT_ROOT)+"-docs.pdf"

if __name__ == "__main__":
    print("\nMerging PDF Docs:\n")
    with PdfWriter() as merger:
        for pdf in sorted(glob(f"{SCRIPT_ROOT}/**/*.pdf", recursive=True), key=getmtime, reverse=False):
            if MERGE_FILE not in pdf:
                print("[+] ", pdf)
                merger.append(pdf)
        merger.write(join(SCRIPT_ROOT,MERGE_FILE))
    print(f"\nURL: file://{join(SCRIPT_ROOT,MERGE_FILE).replace(chr(92),'/')}")
