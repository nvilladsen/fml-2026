# Forecasting with Machine Learning

Course site for Forecasting with Machine Learning, Aarhus University. The site consists of HTML pages and Reveal.js lectures built with Quarto. The lectures run Python in the browser (Pyodide), so no installation is needed to use them. The site is published with GitHub Pages from the `main` branch.

## Structure

| path | description |
|:--|:--|
| `index.html`, `syllabus.html`, `schedule.html`, `literature.html`, `setup.html`, `downloads.html`, `exam_info.html` | course pages |
| `assets/` | site styles, images, and the shared menu and footer |
| `session_NN/session_NN.qmd` | lecture source, with the slide SCSS alongside it or in `theme/` |
| `session_NN/session_NN.html`, `session_NN_files/` | rendered lecture |
| `_extensions/r-wasm/live/` | the quarto-live extension, which provides the in-browser Python cells |
| `tools/` | helper scripts for the menu and footer (`build_nav.py`) and for checking links (`check_site.py`) |

## Local workflow

Requires [Quarto](https://quarto.org) 1.4 or later and Python 3.

```bash
quarto render session_03/session_03.qmd   # rebuild one lecture
python tools/build_nav.py                 # update menu and footer on all pages
python tools/check_site.py                # check menu, footer, rendered lectures and local links
python -m http.server 8000                # preview at http://localhost:8000/
```

The site must be previewed over HTTP, since the live cells do not run from `file://`.

## Credits

The slide theme is adapted from Jonas Theill Bøjstrup, Machine Learning in Finance, Aarhus University (2026), https://theill95.github.io/mlfin-2026/, CC BY 4.0.

[quarto-live](https://github.com/r-wasm/quarto-live) by George Stagg and contributors, MIT licence. Pyodide is loaded from a CDN at run time.