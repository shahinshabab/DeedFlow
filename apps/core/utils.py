import json
from decimal import Decimal
from datetime import date, datetime


class SafeJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        return super().default(obj)


def pretty_json(data):
    return json.dumps(data or {}, indent=2, ensure_ascii=False, cls=SafeJSONEncoder)
