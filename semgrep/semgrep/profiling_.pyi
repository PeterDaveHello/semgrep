from typing import NamedTuple

Times = NamedTuple(
    "Times", [("parse_time", float), ("match_time", float), ("run_time", float)]
)

class ProfilingData:
    def __init__(self) -> None: ...
