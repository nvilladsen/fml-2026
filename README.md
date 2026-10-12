# Forecasting with Machine Learning

Course site for Forecasting with Machine Learning, Aarhus University. Hand-written HTML pages plus Reveal.js lectures built with Quarto. The lectures run Python in the browser (Pyodide), so students need no installation. The site is published with GitHub Pages straight from the `main` branch.

## Structure

| path | what it is |
|:--|:--|
| `index.html`, `syllabus.html`, `schedule.html`, `literature.html`, `setup.html`, `downloads.html` (Code & data), `exam_info.html` | hand-written pages |
| `assets/nav.html` | the top bar, stamped into every root page by `tools/build_nav.py` |
| `assets/footer.html` | name, email and credit line, stamped into every root page by `tools/build_nav.py` |
| `assets/site.css` | site styles, colour tokens at the top, dark mode follows the system |
| `session_NN/session_NN.qmd` | lecture source, with the slide SCSS next to it or in `theme/` |
| `session_NN/session_NN.html`, `session_NN_files/` | rendered lecture, committed because Pages serves the files as they are |
| `_extensions/r-wasm/live/` | the quarto-live extension (MIT, see `LICENSE.md` inside), which provides `live-revealjs` and the `{pyodide}` cells |
| `.nojekyll` | tells Pages to skip Jekyll |
| `tools/` | `build_nav.py` and `check_site.py` |

## Common edits

- **Email, name or credit line on every page:** edit `assets/footer.html`, then run `python tools/build_nav.py`.
- **Menu entries:** edit `assets/nav.html` and the `PAGES` list in `tools/build_nav.py`, then run `python tools/build_nav.py`.
- **Colours and fonts of the site:** the `:root` block at the top of `assets/site.css`. The slide SCSS does not affect the site pages.
- **Text on a page:** edit the page, save, refresh the browser. No rendering is needed.
- **Slides:** edit the `.qmd` or the SCSS, then `quarto render session_NN/session_NN.qmd`.

## Local workflow

Requires [Quarto](https://quarto.org) 1.4 or later (built with 1.8.27) and Python 3.

```bash
quarto render session_03/session_03.qmd   # rebuild one lecture
python tools/build_nav.py                 # after editing nav.html or footer.html
python tools/check_site.py                # before every push
python -m http.server 8000                # preview at http://localhost:8000/
```

Preview over HTTP. The live cells do not run from `file://`.

`check_site.py` verifies that the menu and footer are up to date, that every `session_NN.qmd` has a rendered `.html`, and that every local link resolves. It does not test external links, paths inside the SCSS, or the live cells.

## Images and files

- Slide images: next to the deck (`session_03/img/`) or shared (`assets/img/`), referenced in the `.qmd` relative to the `.qmd`.
- PDFs and other downloads: `downloads/`.
- Do not use `url(...)` to a file inside the slide SCSS. Quarto compiles the SCSS into a CSS file inside `session_NN_files/`, so the path breaks. Use a data URI, or place the image in the `.qmd`.

## First-time publishing on GitHub

1. Create an empty repository on GitHub. Pages works on private repositories with GitHub Pro, but the published site is public even when the repository is private. Do not enable Pages until the site should be public.
2. In this folder:

```bash
git init -b main
git add .
git commit -m "Initial course site"
git remote add origin https://github.com/<user>/<repo>.git
git push -u origin main
```

3. When ready to publish: Settings, Pages, Build and deployment, Deploy from a branch, `main` and `/ (root)`, save.
4. The site is live at `https://<user>.github.io/<repo>/` after a minute or two. Every later push to `main` updates it.

## Adding a session

1. Copy `session_03/` to `session_NN/`, rename the `.qmd`, and change the title and subtitle.
2. `quarto render session_NN/session_NN.qmd`
3. Add a card in `index.html`, a row in `schedule.html` and a section in `downloads.html`.
4. `python tools/check_site.py`, then commit the `.qmd`, the `.html` and the `_files/` folder.

## Placeholders to fill

Every placeholder is in square brackets, and most sit in an amber note box on the page. Search for `[` and `Placeholder` to find them all.

## Credit and third-party code

The slide theme is adapted from Jonas Theill Bøjstrup, Machine Learning in Finance, Aarhus University (2026), https://theill95.github.io/mlfin-2026/, CC BY 4.0. The credit line is in `assets/footer.html`.

[quarto-live](https://github.com/r-wasm/quarto-live) by George Stagg and contributors, MIT licence. Pyodide is loaded from a CDN at run time.
