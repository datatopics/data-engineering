import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

MODULES_FILE = PROJECT_ROOT / "course" / "modules" / "modules.json"

PROGRESS_FILE = PROJECT_ROOT / "course" / "progress" / "progress.json"


def get_modules() -> list[dict]:
    modules = json.loads(MODULES_FILE.read_text(encoding="utf-8"))

    progress = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))

    enriched_modules = []

    for module in modules:
        enriched_modules.append(
            {
                **module,
                "completed": progress.get(
                    module["id"],
                    False,
                ),
            }
        )

    return enriched_modules
