from pprint import pprint
import json
from datetime import datetime
from datetime import timezone

FILENAME = '../tmp/fixtures.json'


def make_datetime(string):
    """
    >>> make_datetime('2013-10-21T13:28:06.419Z')
    datetime.datetime(2013, 10, 21, 13, 28, 6, 419000, tzinfo=datetime.timezone.utc)
    """
    return datetime.strptime(string, '%Y-%m-%dT%H:%M:%S.%fZ').replace(
        tzinfo=timezone.utc)


with open(FILENAME) as file:
    content = file.read()

for key, value in json.loads(content).items():
    print(value)
