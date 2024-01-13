""" merge nested pdfs at script root """

from os.path import dirname,abspath,basename,join
from subprocess import run
from glob import glob

FORCE_PIP_INSTALL = False

try:
    from pypdf import PdfWriter
except ModuleNotFoundError:
    if FORCE_PIP_INSTALL:
        run(["pip", "install", "pypdf"])
        from pypdf import PdfWriter

SCRIPT_ROOT = abspath(dirname(__file__))
MERGE_FILE = basename(SCRIPT_ROOT)+"-docs.pdf"

if __name__ == "__main__":
    print("\n## Merge PDF Docs ##\n")
    with PdfWriter() as merger:
        for pdf in glob(f"{SCRIPT_ROOT}/**/*.pdf", recursive=True):
            if MERGE_FILE not in pdf:
                print("[+] ", pdf)
                merger.append(pdf)
        merger.write(join(SCRIPT_ROOT,MERGE_FILE))
    print(f"\nURL: file://{join(SCRIPT_ROOT,MERGE_FILE).replace(chr(92),'/')}")
