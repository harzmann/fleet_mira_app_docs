# Fleet Mira App documentation

Public product description, installation guide and end-user manual for **Fleet Mira App**.

- **Deutsch:** https://harzmann.github.io/fleet_mira_app_docs/de/
- **English:** https://harzmann.github.io/fleet_mira_app_docs/
- Application source: `harzmann/fleet_mira_app` (private; access required).

## Authoring and publication

Edit paired Markdown pages under `docs/en` and `docs/de`. Shared screenshots and the Fleet Mira documentation design assets live under `docs/assets`, `docs/stylesheets` and `docs/javascripts`. The design follows `harzmann/fleet_mira_docs`: MkDocs Material, blue light/slate palettes, navigation sections, search, code copying and the same image lightbox. This repository contains the editable source, not a copy of another product's generated site.

```sh
python -m venv .venv
# Activate the virtual environment for your shell.
python -m pip install -r requirements.txt
python scripts/sync_assets.py
python scripts/validate_docs.py
python -m mkdocs build --strict
python scripts/check_site.py
python -m mkdocs serve
```

Pushes to `main` build and deploy GitHub Pages through `.github/workflows/pages.yml`; pull requests validate without publishing. Pages must use **GitHub Actions** as its publishing source. Pages publishes documentation. APKs are explicitly published through GitHub Releases; a documentation deployment alone does not publish an APK or declare it production-ready.

Use synthetic demonstration data for screenshots. Do not commit credentials, customer data, internal server addresses, signing keys, APKs or private development reports. Application language coverage must be described separately from documentation language coverage.

With i18n fallback disabled, the German build needs a local asset overlay. `docs/assets/screenshots` is the canonical screenshot source; `scripts/sync_assets.py` refreshes its identical `docs/de/assets/screenshots` copies. Commit both together; validation checks their hashes.
