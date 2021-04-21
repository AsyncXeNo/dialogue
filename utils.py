import json

from option import Option
from dialogue import Dialogue

with open('data/dialogues.json') as f:
	dialogues_object = json.load(f)

with open('data/options.json') as f:
	options_object = json.load(f)


def get_options(name):
	options_list = []
	for option in options_object:
		if option["name"] == name:
			for option_for_individual_dialogue in option["options"]:
				option_id = option_for_individual_dialogue["id"]
				choices = []
				for choice in option_for_individual_dialogue["choices"]:
					choices.append(Option(choice["string"], choice["dialogue"]))

				options_list.append({
					"id": option_id,
					"list": choices
				})

	return options_list


print(get_options("person1"))


def get_dialogue(name):
	list_of_dialogues = []
	for dialogue in dialogues_object:
		if dialogue["name"] == name:
			for individual_dialogue in dialogue["dialogues"]:

				name = individual_dialogue["name"]
				string = individual_dialogue["string"]
				options = individual_dialogue["options"]
				next_dialogue = individual_dialogue["next"]

				options_list = None

				if options:
					for option in get_options("person1"):
						if option["id"] == options:
							options_list = option["list"]

				if options_list:
					print(f'options given to dialogue with id {individual_dialogue["id"]}')
				list_of_dialogues.append({
					"id": individual_dialogue["id"],
					"dialogue": Dialogue(name, string, options_list, next_dialogue)
				})	

	return list_of_dialogues


for dialogue in get_dialogue("person1"):
	print(dialogue["dialogue"])