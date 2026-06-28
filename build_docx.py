#!/usr/bin/env python3
"""
Convert game-mechanics.md -> game-mechanics.docx with formatting preserved
(headings, tables, bold, lists).

Pipeline: markdown (with table support) -> HTML -> docx via htmldocx.
Auto-installs the two pure-Python deps if missing. Falls back to pypandoc.

Usage:  python build_docx.py [input.md] [output.docx]
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
IN_MD = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "game-mechanics.md")
OUT_DOCX = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "game-mechanics.docx")


def _pip_install(*pkgs):
    print(f"Installing: {', '.join(pkgs)} ...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", *pkgs])


def build_with_htmldocx(md_text):
    import markdown  # noqa
    from htmldocx import HtmlToDocx  # noqa
    from docx import Document  # noqa

    html = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists", "toc"],
    )
    doc = Document()
    HtmlToDocx().add_html_to_document(html, doc)
    doc.save(OUT_DOCX)


def build_with_pandoc(md_path):
    import pypandoc  # noqa
    pypandoc.convert_file(md_path, "docx", outputfile=OUT_DOCX)


def main():
    with open(IN_MD, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Primary: markdown + htmldocx
    try:
        try:
            build_with_htmldocx(md_text)
        except ImportError:
            _pip_install("markdown", "python-docx", "htmldocx")
            build_with_htmldocx(md_text)
        print(f"OK (htmldocx) -> {OUT_DOCX}")
        return
    except Exception as e:  # noqa
        print(f"htmldocx path failed: {e}\nTrying pandoc fallback...")

    # Fallback: pypandoc (downloads pandoc if needed)
    try:
        try:
            build_with_pandoc(IN_MD)
        except ImportError:
            _pip_install("pypandoc_binary")
            build_with_pandoc(IN_MD)
        print(f"OK (pandoc) -> {OUT_DOCX}")
    except Exception as e:  # noqa
        print(f"ERROR: both converters failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
