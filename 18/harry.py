import os
import urllib.request
import re
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_harry_most_common_word():
    with open(harry_text, "rt", encoding='utf-8') as f:
        data = f.read()
        harry_data = re.split(r'[;,."\s]\s*', data)
        harry_data = [data.lower() for data in harry_data]

    with open(stopwords_file, "rt", encoding="utf-8") as f:
        data = f.readlines()
        filter_data = [element.rstrip() for element in data]
        filter_data.append("")

    words = filter(lambda x: x.isalnum and x not in filter_data, harry_data)

    return Counter(words).most_common()[0]
