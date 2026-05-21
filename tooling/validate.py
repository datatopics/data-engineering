import json
import sys
from pathlib import Path

from validators import foundations

PROJECT_ROOT = Path(__file__).resolve().parents[1]

PROGRESS_FILE = PROJECT_ROOT / "course" / "progress" / "progress.json"


VALIDATORS = {
    "foundations": foundations.validate,
}


def update_progress(module_id: str) -> None:
    progress = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))

    progress[module_id] = True

    PROGRESS_FILE.write_text(
        json.dumps(progress, indent=2),
        encoding="utf-8",
    )


def main() -> None:
    if len(sys.argv) < 2:
        print("Missing module name.")
        sys.exit(1)

    module_name = sys.argv[1]

    validator = VALIDATORS.get(module_name)

    if not validator:
        print(f"Validator not found: {module_name}")
        sys.exit(1)

    validation_result = validator()

    if not validation_result:
        print("Validation failed.")
        sys.exit(1)

    update_progress(module_name)

    print("Validation successful.")
    print(f"Module completed: {module_name}")


if __name__ == "__main__":
    main()
