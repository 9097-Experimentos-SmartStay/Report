#!/usr/bin/env python3
"""Build the report using Python's standard library only."""

import argparse
import html
import json
import posixpath
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
NOTICE = "<!-- Generado con python3 scripts/build_report.py. Editar los archivos de docs/, no este README. -->"
BREAK = '\n\n---\n\n<div style="page-break-after: always;"></div>\n\n'


def prose_blocks(text):
    """Keep fenced code examples intact when finding headings or rewriting links."""
    prose = []
    fence = None
    for line in text.splitlines(keepends=True):
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\n"))
        if fence:
            yield False, line
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
        elif match:
            if prose:
                yield True, "".join(prose)
                prose = []
            fence = match[1]
            yield False, line
        else:
            prose.append(line)
    if prose:
        yield True, "".join(prose)


def rewrite_links(text, source):
    def target(url):
        parts = urlsplit(html.unescape(url))
        if parts.scheme or parts.netloc or not parts.path or parts.path.startswith("/"):
            return url
        path = posixpath.normpath(posixpath.join(source.parent.as_posix(), parts.path))
        local = ROOT / unquote(path)
        if not local.is_file():
            raise ValueError(f"{source}: archivo enlazado inexistente: {url}")
        return urlunsplit(("", "", path, parts.query, parts.fragment))

    def rewrite(block):
        # Mask inline code before rewriting HTML or Markdown links.
        code = []

        def protect(match):
            code.append(match[0])
            return f"\x00{len(code) - 1}\x00"

        block = re.sub(r"(`+).*?\1", protect, block)
        block = re.sub(
            r"(\b(?:src|href)\s*=\s*)([\"'])(.*?)(\2)",
            lambda m: m[1] + m[2] + target(m[3]) + m[4], block,
        )
        block = re.sub(
            r"(!?\[[^\]\n]*\]\()(<[^>\n]+>|[^\s)]+)",
            lambda m: m[1] + ("<" + target(m[2][1:-1]) + ">" if m[2].startswith("<") else target(m[2])),
            block,
        )
        block = re.sub(
            r"(?m)^( {0,3}\[[^\]\n]+\]:\s*)(<[^>\n]+>|\S+)",
            lambda m: m[1] + ("<" + target(m[2][1:-1]) + ">" if m[2].startswith("<") else target(m[2])),
            block,
        )
        return re.sub(r"\x00(\d+)\x00", lambda m: code[int(m[1])], block)

    return "".join(rewrite(block) if prose else block for prose, block in prose_blocks(text))


def headings(text):
    for prose, block in prose_blocks(text):
        if prose:
            for match in re.finditer(r"(?m)^ {0,3}(#{1,6})\s+(.+?)\s*$", block):
                title = re.sub(r"\s+#+\s*$", "", match[2])
                title = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", title)
                title = html.unescape(re.sub(r"<[^>]*>", "", title))
                title = re.sub(r"[*`~]", "", title)
                yield len(match[1]), title


def slug(title):
    return "".join(
        char for char in title.lower()
        if char in " -_" or unicodedata.category(char)[0] in "LNM"
    ).replace(" ", "-")


def build():
    manifest = json.loads((ROOT / "docs/report.json").read_text(encoding="utf-8"))

    def read(filename):
        source = Path(filename)
        text = (ROOT / source).read_text(encoding="utf-8")
        if re.search(r"(?m)^(<<<<<<< |=======\s*$|>>>>>>> )", text):
            raise ValueError(f"{filename}: conflicto de Git pendiente")
        return rewrite_links(text, source).strip()

    cover = read(manifest["cover"])
    info = read(manifest["info"])
    sections = [
        "# " + entry["heading"] if "heading" in entry else read(entry["file"])
        for entry in manifest["sections"]
    ]
    body = BREAK.join([info, *sections])
    used = set()

    def anchor(title):
        base = slug(title)
        value = base
        count = 0
        while value in used:
            count += 1
            value = f"{base}-{count}"
        used.add(value)
        return value

    for _, title in headings(cover):
        anchor(title)
    anchor("Tabla de Contenido")
    toc = []
    for section, base_level in [(info, 2), *((section, 1) for section in sections)]:
        for level, title in headings(section):
            link = anchor(title)
            depth = max(0, level - base_level)
            label = title.replace("[", "\\[").replace("]", "\\]")
            toc.append("  " * depth + f"- [{label}](#{link})")
    return NOTICE + "\n\n" + cover + "\n\n## Tabla de Contenido\n\n" + "\n".join(toc) + BREAK + body + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Comprobar que README.md coincide con sus fuentes")
    args = parser.parse_args()
    try:
        report = build()
    except (OSError, ValueError, KeyError) as error:
        print(error, file=sys.stderr)
        return 1
    output = ROOT / "README.md"
    if args.check:
        if not output.exists() or output.read_text(encoding="utf-8") != report:
            print("README.md desactualizado. Ejecutar: python3 scripts/build_report.py", file=sys.stderr)
            return 1
        print("README.md coincide con los archivos fuente.")
    else:
        output.write_text(report, encoding="utf-8")
        print("README.md generado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
