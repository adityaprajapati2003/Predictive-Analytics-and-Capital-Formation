"""Hard filters: stage, subsector, geography, ticket size."""


def passes(startup: dict, investor: dict) -> bool:
    if investor.get("stages") and startup["stage"] not in investor["stages"]:
        return False
    if investor.get("subsectors") and startup["subsector"] not in investor["subsectors"]:
        return False
    return True
