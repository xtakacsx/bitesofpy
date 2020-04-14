from collections import Counter, defaultdict
import os
from urllib.request import urlretrieve
import re

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """

    with open(commit_log) as f:
        d = defaultdict(Counter)
        pattern = r"[\d]+"
        for commit in f:
            date, git = commit.split("|")
            dt = parse(date.replace("Date:", "").strip())
            if year and dt.year != year:
                continue
            dt = dt.strftime("%Y-%m")
            git = git.split(",")[1:]
            if len(git) > 1:
                inserts, deletes = git
                d[dt]["inserts"] += int(re.findall(pattern, inserts)[0])
                d[dt]["deletes"] += int(re.findall(pattern, deletes)[0])
            if len(git) == 1:
                if "(+)" in git[0]:
                    d[dt]["inserts"] += int(re.findall(pattern, git[0])[0])
                elif "(-)" in git[0]:
                    d[dt]["deletes"] += int(re.findall(pattern, git[0])[0])

    z = {k: v for k, v in sorted(d.items(), key=lambda item: sum(item[1].values()))}
    return list(z.keys())[0], list(z.keys())[-1]


print(get_min_max_amount_of_commits())
