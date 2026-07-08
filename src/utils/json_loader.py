from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.utils.logger import get_logger

logger = get_logger(__name__)


def load_json(file_path: Path) -> dict[str, Any]:
    """
    Load and return JSON data from a file.

    Args:
        file_path: Path to the JSON file.

    Returns:
        Parsed JSON as a dictionary.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the JSON is invalid.
    """

    if not file_path.exists():
        logger.error("JSON file not found: %s", file_path)
        raise FileNotFoundError(f"{file_path} does not exist.")

    try:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError as exc:
        logger.exception("Invalid JSON in %s", file_path)
        raise ValueError(f"Invalid JSON in {file_path}") from exc