---
name: pdf
description: 'PDF file inspection, object-level editing, and lossless size reduction using qpdf, pdf-parser.py, pdfsizeopt, and Ghostscript. You MUST load this skill when inspecting, editing, or optimizing PDF files.'
license: MIT

---
# PDF Skill

<!-- markdownlint-disable MD013 MD023 MD031 MD032 -->

## When to Use
- When inspecting PDF file structure to identify bloat sources (large streams, duplicate fonts, embedded metadata).
- When reducing PDF file size through lossless or lossy compression methods.
- When performing object-level editing on PDF files using QDF (qpdf human-readable format).
- When extracting forensic information from PDFs (object statistics, stream dumps) using `pdf-parser.py`.
- When batch-optimizing PDFs for web distribution or archival storage.
- When verifying page count, dimensions, and metadata are preserved after optimization.

## When Not to Use
- When the PDF is digitally signed or contains legal certifications — object-level editing may break signatures or validation.
- When simple text extraction suffices — use `pdftotext` or other poppler-utils instead of full object inspection.
- When the user only needs to merge or split PDF pages — use `qpdf --empty --pages ... -- output.pdf` or `pdfunite` rather than this skill's full workflow.
- When the PDF should remain fully uncompressed for debugging — object-level editing with QDF is the right approach, but skip lossy reduction steps.

## Gotchas
- Running Ghostscript (`gs`) first is destructive — it rewrites the entire document and prevents object-level editing; always inspect with `qpdf --json` first.
- The `--recompress-flate` flag in qpdf may produce larger files on already-well-compressed content — always verify size reduction with `ls -lh`.
- Lossy reduction with Ghostscript presets (`/screen`, `/ebook`) can degrade image quality significantly — use `/printer` or `/prepress` for document preservation.
- Always verify page count and dimensions after reduction — `diff <(pdfinfo input.pdf | grep -E 'Pages|Page size') <(pdfinfo optimized.pdf | grep -E 'Pages|Page size')` catches unintended alterations.

Analyze, edit, and shrink PDF files at the object level without losing content.

## Tool Selection

| Tool | Install (Ubuntu) | Strength |
| ---- | ---------------- | -------- |
| qpdf | `sudo apt install qpdf` | Object-level JSON inspection, QDF editing, lossless recompression |
| pdf-parser.py | `wget -O …/pdf-parser.py` (Didier Stevens) | Object stats, stream dump, forensic analysis |
| pdfsizeopt | Single-file Python script (`curl`) | Best automated lossless reduction (dedup fonts/streams) |
| Ghostscript (gs) | `sudo apt install ghostscript` | Fast lossy reduction via presets |
| mutool (MuPDF) | `sudo apt install mupdf-tools` | Quick `clean` + `linearize` |
| poppler-utils | `sudo apt install poppler-utils` | `pdfinfo`, `pdfimages`, `pdftotext` utilities |

## Inspection (Identify Bloat)

```bash
# Page count, size, fonts, metadata
pdfinfo input.pdf

# Object statistics — spot huge /FlateDecode streams or duplicate fonts
pdf-parser.py -a input.pdf

# Export full object graph as JSON; find largest streams
qpdf --json --json-stream-data=file input.pdf > /tmp/analysis.json
jq '[.qpdf[1] | to_entries[] | select(.value.stream) | {obj: .key, length: .value.stream.length}]
  | sort_by(-.length) | .[:20]' /tmp/analysis.json
```

## Lossless Size Reduction

### Automated (Zero Manual Editing)

```bash
# pdfsizeopt — best for duplicate fonts/streams/EML-style bloat
pdfsizeopt --use-pngout=no input.pdf output.pdf

# qpdf — recompress streams + generate object streams
qpdf --compress-streams=y --object-streams=generate --recompress-flate --linearize \
  input.pdf qpdf-opt.pdf
```

### Manual Object Pruning via QDF

```bash
# Convert to human-readable QDF format
qpdf --qdf input.pdf editable.qdf

# Edit editable.qdf: locate huge object IDs from inspection step,
# delete entire "obj … endobj" blocks for unused /XObject or metadata.
# Then repack:
qpdf editable.qdf optimized.pdf
```

## Lossy Reduction (Ghostscript)

```bash
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
  -dNOPAUSE -dQUIET -dBATCH -sOutputFile=gs-opt.pdf input.pdf
```

Preset options: `/screen` (72 dpi), `/ebook` (150 dpi), `/printer` (300 dpi),
`/prepress` (300 dpi, color-preserving).

## Post-Execution QA Gate

Always verify after any reduction:

```bash
ls -lh input.pdf optimized.pdf
pdfinfo optimized.pdf
diff <(pdfinfo input.pdf | grep -E 'Pages|Page size') \
     <(pdfinfo optimized.pdf | grep -E 'Pages|Page size')
```

Confirm: file size decreased, page count unchanged, page dimensions preserved.

## What to Avoid

- Running Ghostscript first — it rewrites the entire document and cannot do object-level edits
- Using `pdfcpu` or `exiftool` alone — insufficient object-level control
- Skipping the inspection step — always identify bloat sources before attempting reduction

## Related Skills

- **robust-commands**:
  You MUST load this skill when executing commands requiring resilient error recovery or fallbacks.
