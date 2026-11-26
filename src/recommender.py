"""
Route recommender for Baguio City jeepney routes.

Lab 1: starter module. Matches a destination to routes.
Lab 2+: will rank routes by demand and travel time.
"""


def find_matching_routes(routes: list, destination: str) -> list:
    """
    Find routes whose destinations match the user's destination.

    Args:
        routes: list of route dicts, each with a 'destinations' list.
        destination: the user's desired destination (case-insensitive).

    Returns:
        A list of matching route dictionaries.
    """
    destination = destination.strip().lower()

    if not destination:
        return []

    matches = []

    for route in routes:
        for place in route.get("destinations", []):
            place = place.lower()
            if destination in place or place in destination:
                matches.append(route)
                break

    return matches


if __name__ == "__main__":
    sample_routes = [
        {"name": "Route A", "destinations": ["burnham park", "city market"]},
        {"name": "Route B", "destinations": ["wright park", "the mansion"]},
    ]

    results = find_matching_routes(sample_routes, "burnham")
    print(f"Found {len(results)} matching route(s):")
    for r in results:
        print(f"  - {r['name']}")
