from __future__ import annotations

import sqlite3
from pathlib import Path

from src.utils.logger import get_logger

logger = get_logger(__name__)


def get_connection(db_path: Path) -> sqlite3.Connection:
    """
    Create and return a SQLite connection.
    """

    if not db_path.exists():
        logger.error("Database not found: %s", db_path)
        raise FileNotFoundError(f"{db_path} not found.")

    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row

    return connection