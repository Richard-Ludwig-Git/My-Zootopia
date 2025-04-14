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
        output += "<li class='cards__item'>\n"
        output += f"<div class='card__title'>{fox["name"]}<br/>\n</div>"
        output += f"<p class='card__text'>\n <strong>Diet: </strong>{fox["characteristics"]["diet"]}<br/>\n"
        output += "<strong>Location: </strong>"
        output += f" {", ".join(fox["locations"])}<br/>\n"
        output += f"<strong>Type: </strong>{fox["characteristics"]["type"]}<br/>\n"
        output += "</p>"
        output += "</li>"
    except KeyError:
        output += "\n"
        continue

temp_with_data = template.replace("__REPLACE_ANIMALS_INFO__", output)
print(temp_with_data)
with open("animals.html", "w") as makepage:
    makepage.write(temp_with_data)