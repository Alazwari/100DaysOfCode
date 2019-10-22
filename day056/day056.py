# Day 56

import json

x = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "pets": None,
    "cars": [
        {"model": "BMW 750", "color": "blue"},
        {"model": "Nissan Z", "color": "black"}
    ]
}

print(json.dumps(x, indent=4, separators=(". ", " = ")))