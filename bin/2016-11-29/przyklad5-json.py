from pprint import pprint
import json
import datetime

INPUT = '../../tmp/fixtures.json'
OUTPUT = '../../tmp/fixtures-new.json'


def make_datetime(string):
    """
    >>> make_datetime('2013-10-21T13:28:06.419Z')
    datetime.datetime(2013, 10, 21, 13, 28, 6, 419000, tzinfo=datetime.timezone.utc)
    """
    return datetime.datetime.strptime(string, '%Y-%m-%dT%H:%M:%S.%fZ').replace(
        tzinfo=datetime.timezone.utc)


with open(INPUT) as file:
    content = file.read()


data = json.loads(content)

for key, value in data.items():
    for element in value:
        element['timestamp'] = make_datetime(element['timestamp'])

"""
class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super(DatetimeEncoder, obj).default(obj)
        except TypeError:
            return '{:%Y-%m-%dT%H:%M:%S.%fZ}'.format(obj)


with open(OUTPUT, 'w') as file:
    d = json.dumps(data, cls=DatetimeEncoder)
    file.write(d)
"""

#d = json.dumps(data, indent=4, sort_keys=True, default=lambda x:str(x))
#print(d)

json.JSONEncoder.default = lambda self,obj: ('{:%Y-%m-%dT%H:%M:%S.%fZ}'.format(obj) if isinstance(obj, datetime.datetime) else None)


def _(obj):
    if isinstance(obj, datetime.datetime):
        # return '{:%Y-%m-%dT%H:%M:%S.%fZ}'.format(obj)
        return obj.isoformat()
    else:
        return None



d = json.dumps(data)
print(d)
