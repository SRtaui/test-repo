import json

def task() -> float:
    with open("data.json", "r") as file:
        data = json.load(file)
    result = sum(item["score"] * item["weight"] for item in data)
    return round(result, 3)

print(task())
