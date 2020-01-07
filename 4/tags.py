import os
from collections import Counter
import urllib.request
import re

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    pattern = re.compile(r"<category>(.*?)</category>")

    matches = pattern.finditer(content)
    return Counter(([match.group(1) for match in matches])).most_common(n)

