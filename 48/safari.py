from collections import defaultdict
import os
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)


def _get_lines(log):
    with open(log) as f:
        return [line.strip() for line in f.readlines()]


def create_chart(log=None):
    log = log or SAFARI_LOGS
    lines = _get_lines(log)

    posts = defaultdict(list)

    for prev_line, line in zip(lines, lines[1:]):
        if 'sending to' in line:
            date = prev_line.split()[0]
            book_icon = 'python' in prev_line.lower() and PY_BOOK or OTHER_BOOK
            posts[date].append(book_icon)

    for date, books in posts.items():
        print(date, ''.join(books))
