import tomllib
from collections import defaultdict
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[3]


EXTENSION_LANGUAGE_MAPPING = {
    ".py": "Python",
    ".sql": "SQL",
    ".yml": "YAML",
    ".yaml": "YAML",
    ".toml": "TOML",
    ".md": "Markdown",
    ".sh": "Shell",
}


LANGUAGE_COLORS = {
    "Python": "#3572A5",
    "SQL": "#E38C00",
    "YAML": "#CB171E",
    "TOML": "#9C4221",
    "Markdown": "#083FA1",
    "Shell": "#89E051",
    "Dockerfile": "#384D54",
}


def detect_languages() -> list[dict]:
    totals = defaultdict(int)

    for file_path in PROJECT_ROOT.rglob("*"):
        if not file_path.is_file():
            continue

        if ".venv" in file_path.parts:
            continue

        if ".git" in file_path.parts:
            continue

        if file_path.name == "Dockerfile":
            language = "Dockerfile"

        else:
            language = EXTENSION_LANGUAGE_MAPPING.get(file_path.suffix.lower())

        if not language:
            continue

        try:
            line_count = len(
                file_path.read_text(
                    encoding="utf-8",
                    errors="ignore",
                ).splitlines()
            )

            totals[language] += line_count

        except Exception:
            continue

    total_lines = sum(totals.values())

    languages = []

    for language, lines in totals.items():
        percentage = round(
            (lines / total_lines) * 100,
            1,
        )

        languages.append(
            {
                "language": language,
                "lines": lines,
                "percentage": percentage,
                "color": LANGUAGE_COLORS.get(
                    language,
                    "#888888",
                ),
            }
        )

    return sorted(
        languages,
        key=lambda item: item["lines"],
        reverse=True,
    )


def detect_python_dependencies() -> list[str]:
    pyproject_path = PROJECT_ROOT / "pyproject.toml"

    if not pyproject_path.exists():
        return []

    with open(pyproject_path, "rb") as file:
        pyproject = tomllib.load(file)

    dependencies = pyproject["project"].get(
        "dependencies",
        [],
    )

    cleaned_dependencies = []

    for dependency in dependencies:
        cleaned_dependencies.append(dependency.split("==")[0])

    return sorted(cleaned_dependencies)


def detect_docker_services() -> list[str]:
    compose_path = PROJECT_ROOT / "docker-compose.yml"

    if not compose_path.exists():
        return []

    with open(compose_path, "r", encoding="utf-8") as file:
        compose = yaml.safe_load(file)

    services = compose.get("services", {})

    return sorted(services.keys())
