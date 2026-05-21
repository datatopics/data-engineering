import json
from pathlib import Path

DOCS_PATH = Path(__file__).resolve().parents[3] / "docs"


def get_available_languages() -> list[dict]:
    languages = []

    for path in DOCS_PATH.iterdir():
        if not path.is_dir():
            continue

        config_path = path / "config.json"

        if not config_path.exists():
            continue

        config = json.loads(config_path.read_text(encoding="utf-8"))

        languages.append(config)

    return sorted(
        languages,
        key=lambda language: language["label"],
    )


def load_markdown(language: str, filename: str) -> str:
    file_path = DOCS_PATH / language / filename

    if not file_path.exists():
        return f"Missing documentation file: {file_path}"

    return file_path.read_text(encoding="utf-8")
