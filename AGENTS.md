# Fleet Mira App documentation

- Public end-user documentation only; the application repository is private.
- Keep `docs/en` and `docs/de` paired and synchronized. English is the default route, German is `/de/`.
- Preserve the established `fleet_mira_docs` design: MkDocs Material, blue palettes, search/navigation and shared image-lightbox assets. Do not replace it with a separate site framework.
- Describe only capabilities verified against the application source. Mark the development status and prerequisites explicitly. Do not invent production releases, store downloads, hardware approvals, signature validation, live driving-time calculations or automatic document-authenticity checks.
- Use synthetic screenshots and no secrets, customer records, internal hosts or private operational instructions.
- Run `python scripts/validate_docs.py`, `python -m mkdocs build --strict` and `python scripts/check_site.py` before pushing.
