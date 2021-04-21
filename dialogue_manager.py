from dialogue import Dialogue
from option import Option
from options_manager import OptionsManager
from utils import get_dialogues


class DialogueManager:
    def __init__(self):
        self.dialogues_list = list()
        self.current_dialogue = None
        self.active = False

        self.otions_manager = OptionsManager()

    def activate(self):
    	self.active = True

    def deactive(self):
    	self.active = False
    	self.dialogues_list = list()
    	self.current_dialogue = False

    def set_active_dialogue(self, name):
        try:
        	self.dialogues = get_dialogues(name)
        except:
        	print(f'no dialogue named {name}.')

        self.current_dialogue = self.dialogues.pop(0)["dialogue"]

    def trigger_dialogue(self):
    	if self.active:

    		if len(self.dialogues_list) == 0:
    			print('no more dialogues')
    			self.deactivate()
    			return

	    	print(self.current_dialogue)
	    	if self.current_dialogue.options:
	    		next_dialogue_id = self.options_manager.show_options(self.current_dialogue.options)
	    	else:
	    		input()
	    		next_dialogue_id = self.current_dialogue.next

	    	next_dialogue = None
	    	for dialogue in self.dialogues_list:
	    		if dialogue["id"] == next_dialogue_id:
	    			next_dialogue = dialogue["dialogue"]

	    	if next_dialogue == None:
	    		print('something went wrong')

	    	self.current_dialogue = self.dialogues_list.pop(next_dialogue)["dialogue"]

	    else:
	    	
	    	print('dialogue manager is not active')

