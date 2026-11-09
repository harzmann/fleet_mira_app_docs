"""Copy shared screenshots into the German i18n overlay (fallback is disabled)."""
from pathlib import Path
import shutil

docs = Path(__file__).resolve().parents[1] / "docs"
count = 0
for image in (docs / "assets/screenshots").rglob("*.png"):
    target = docs / "de/assets/screenshots" / image.relative_to(docs / "assets/screenshots")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(image, target)
    count += 1
print(f"Synchronized {count} German screenshot assets")
