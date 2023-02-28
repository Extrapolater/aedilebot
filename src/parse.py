import json
def load_json_to_dict(filename):
    with open(filename) as f:
        dict = json.load(f)
        return dict
def load_location_names(filename):
    with open(filename) as f:
        return f.read().split(";")
def get_all_names(dictionary, field_name="Additional Names"):
    names_dictionary = {}
    for key,value in dictionary.items():
        additional_names = [value["Name"]]

        if field_name in value:
            additional_names.extend(value[field_name].split(";"))

        for name in additional_names:
            if name == "":
                continue
            if name in names_dictionary:
                raise RuntimeError(f"Name {name} repeats itself in {names_dictionary[name]} and {key}")
            names_dictionary[name] = key
    return names_dictionary



# Structure Json parser
location_names = load_location_names("..\data\Location_names.json")

def check_if_location_name(name):
    return name in location_names

targets = load_json_to_dict("..\data\Targets.json")
damages = load_json_to_dict("..\data\Damage.json")
weapons = load_json_to_dict("..\data\Weapons.json")

targets_dictionary = get_all_names(targets)
weapons_dictionary = get_all_names(weapons)

print("Cool")
#slang