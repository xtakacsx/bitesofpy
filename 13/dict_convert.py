from collections import namedtuple
from datetime import datetime
import json

blog = dict(
    name="PyBites",
    founders=("Julian", "Bob"),
    started=datetime(year=2016, month=12, day=19),
    tags=["Python", "Code Challenges", "Learn by Doing"],
    location="Spain/Australia",
    site="https://pybit.es",
)

# define namedtuple here
Student = namedtuple(
    "Student", ["name", "founders", "started", "tags", "location", "site"]
)


def dict2nt(dict_: dict):
    return Student(**dict_)


def nt2json(nt):
    return json.dumps(nt._asdict(), indent=4, default=str)
