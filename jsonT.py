import json
info = [{
    "name": "Tom",
    "gender": "M",
    "other": None
}, {
    "name": "Jack",
    "gender": "F",
    "other": None
}
]

print("json")

json.dump(info, open("base_python/datas/json_dump.json", "w"))
