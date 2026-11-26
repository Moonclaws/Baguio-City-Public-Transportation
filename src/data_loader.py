"""
Data loader for Baguio City jeepney routes.

Laboratory Session 1: starter module. Loads route data from a JSON file.
"""

import json
from pathlib import Path


def load_routes(filepath: str) -> list:
    """
    Load jeepney route data from a JSON file.

    Args:
        filepath: path to the JSON file containing route data.

    Returns:
        A list of route dictionaries.
    """
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"Route data not found: {filepath}")

    with open(path, "r", encoding="utf-8") as f:
        routes = json.load(f)

    return routes


if __name__ == "__main__":
    print("Data loader ready.")
    print("Usage: load_routes('data/routes.json')")
