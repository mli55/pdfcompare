# pdfdelta

**pdfdelta** is a lightweight visual diff tool for born-digital PDFs. It is designed to compare revisions of academic papers and technical documents by highlighting changes directly on the original pages.

The tool generates two annotated files: **deletions** are marked on the old version, and **additions** are marked on the new version.

<p align="center">
  <img src="examples/old_marked.png" alt="Old PDF with deletions" width="48%" />
  <img src="examples/new_marked.png" alt="New PDF with additions" width="48%" />
</p>

<!-- --- -->

## Capabilities

<!-- * Annotates changes directly on the original PDF layout. -->
* Works fine with multi-column layouts and complex papers.
* Skips "fake" changes caused by text moving to a new line, paragraph and page breaking.
* Not confused by moving figures, tables, or math formulas.
<!-- * Uses PyMuPDF for fast, word-level difference detection. -->

## Installation

```sh
pip install pdfdelta
```
If you want to install directly from the repository:

```sh
pip install git+https://github.com/mli55/pdfdelta.git
```

## Usage

```sh
pdfdelta old.pdf new.pdf
```

This writes two annotated files:

- `old_marked.pdf` — original pages with deletions highlighted
- `new_marked.pdf` — revised pages with additions highlighted

### Options

| Flag | Default | Description |
| ---- | ------- | ----------- |
| `--old-out` | `old_marked.pdf` | Output path for the annotated old PDF |
| `--new-out` | `new_marked.pdf` | Output path for the annotated new PDF |
| `--opacity` | `0.35` | Highlight opacity (0.0–1.0) |


## Features

* **Direct Annotation**: Highlights changes as native PDF annotations on the original layout.
* **Layout Aware**: Optimized for multi-column papers and technical reports.
* **Noise Reduction**: Filters out visual artifacts caused by simple text reflow across lines or pages.
* **Structural Support**: Better handling of figures and tables.
<!-- * **No Heavy Dependencies**: Built on top of PyMuPDF for speed and reliability. -->


## How It Works

```
 old.pdf    new.pdf
   │           │
   ▼           ▼
┌──────────────────┐
│  Extract words   │  PyMuPDF: word text + bounding boxes
└────────┬─────────┘
         ▼
┌──────────────────┐
│  Global diff     │  Flatten all pages → SequenceMatcher
└────────┬─────────┘
         ▼
┌──────────────────┐
│  Word-level diff │  Per-word & sub-word precision
└────────┬─────────┘
         ▼
┌──────────────────┐
│  Reflow filter   │  Suppress cross-page / cross-column noise
└────────┬─────────┘
         ▼
┌──────────────────┐
│  Annotate PDFs   │  Highlights on original pages
└────────┬─────────┘
         ▼
 old_marked.pdf
 new_marked.pdf
```

## License

MIT