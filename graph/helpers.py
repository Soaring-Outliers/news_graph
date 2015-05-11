import json
def to_dict(*arrays):
    res = {}
    for array in arrays:
        for obj in array:
            if isinstance(obj, dict):
                d = obj
            else:
                d = obj.json_attributes()
            if d:
                res[int(d["id"])] = d
    return res
def to_json(*arrays):
    return json.dumps(to_dict(*arrays))