import json

from option import Option
from dialogue import Dialogue

with open('data/dialogues.json') as f:
	dialogues_object = json.load(f)

with open('data/options.json') as f:
	options_object = json.load(f)


def get_dialogue(name):
	list_of_dialogues = []
	for dialogue in dialogues_object:
		if dialogue["name"] == name:
			for individual_dialogue in dialogue["dialogues"]:

				name = individual_dialogue["name"]
				string = individual_dialogue["string"]
				options = individual_dialogue["options"]
				options_list = None

				if options:
					for option in options_object:
						if option["name"] == name:
							for options_of_individual_dialogue in option["options"]:
								if options_of_individual_dialogue["id"] == options:
									options_list = []
									for choice in options_of_individual_dialogue["choices"]:
										options_list.append(Option(choice["string"], choice["dialogue"]))


				list_of_dialogues.append({
					"id": individual_dialogue["id"],
					"dialogue": Dialogue(name, string, options_list)
				})	

	return list_of_dialogues


for dialogue in get_dialogue("person1"):
	print(dialogue["dialogue"])