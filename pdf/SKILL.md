<!-- markdownlint-disable MD003 MD022 MD026 MD041 -->
---
name: pdf
description: >-
  PDF file inspection, object-level editing, and lossless size reduction using
  qpdf, pdf-parser.py, pdfsizeopt, and Ghostscript.

  Maintained at: <https://github.com/Cogni-AI-OU/cogni-ai-agent-skills>
license: MIT

---
# PDF Skill

Analyze, edit, and shrink PDF files at the object level without losing content.

## When to Activate

- Reducing PDF file size (lossless or lossy)
- Inspecting PDF internals (objects, streams, fonts, metadata)
- Editing or removing specific PDF objects (fonts, images, metadata)
- Diagnosing PDF bloat (duplicate fonts, embedded attachments, large streams)

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
qpdf --json --json-stream-data=file input.pdf > analysis.json
jq '[.qpdf[1] | to_entries[] | select(.value.stream) | {obj: .key, length: .value.stream.length}]
  | sort_by(-.length) | .[:20]' analysis.json
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

## Maintenance

Note that this file should be updated if outdated or steps/examples are not working.
