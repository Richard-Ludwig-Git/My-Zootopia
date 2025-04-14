import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")

for fox in animals_data:
    try:
        print(f"Name:",fox["name"])
        print(f"Diet:", fox["characteristics"]["diet"])
        print("Location: ", end="")
        print(", ".join(fox["locations"]))
        print(f"Type:", fox["characteristics"]["type"])
    except KeyError:
        print()
        continue
    print()
