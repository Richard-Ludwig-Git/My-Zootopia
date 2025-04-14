import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def load_template(file_path):
    """ Loads a HTML Tamplate """
    with open(file_path, "r") as gettemp:
        return gettemp.read()

animals_data = load_data("animals_data.json")
template = load_template("animals_template.html")

output = ""
for fox in animals_data:
    try:
        output += f"Name: {fox["name"]}\n"
        output += f"Diet: {fox["characteristics"]["diet"]}\n"
        output += "Location: "
        output += f" {", ".join(fox["locations"])}\n"
        output += f"Type: {fox["characteristics"]["type"]}\n"
        output += "\n"
    except KeyError:
        output += "\n"
        continue

temp_with_data = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as makepage:
    makepage.write(temp_with_data)