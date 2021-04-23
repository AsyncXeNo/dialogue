from dialogue import Dialogue
from option import Option
from options_manager import OptionsManager
from utils import get_dialogue


class DialogueManager:
	def __init__(self, options_manager):
		self.dialogues_list = list()
		self.current_dialogue_id = None
		self.active = False

		self.options_manager = options_manager

	def activate(self):
		self.active = True

	def deactivate(self):
		self.active = False
		self.dialogues_list = list()
		self.current_dialogue_id = False

	def set_active_dialogue(self, name):
		try:
			self.dialogues_list = get_dialogue(name)
		except:
			print(f'no dialogue named {name}.')

		self.current_dialogue_id = self.dialogues_list[0]["id"]

	def set_current_dialogue_id(self, id):
		self.current_dialogue_id = id


	def trigger_dialogue(self):

		if self.active:

			for dialogue in self.dialogues_list:
				if dialogue["id"] == self.current_dialogue_id:
					current_dialogue = dialogue["dialogue"]
					print('dialogue assigned')

			if current_dialogue:
				print(current_dialogue)

			if len(self.dialogues_list) == 0:
				print('no more dialogues')
				self.deactivate()
				return


			if current_dialogue.options:
				self.options_manager.activate()
				self.options_manager.set_options(current_dialogue.options)
				next_id = self.options_manager.show_options()
				self.current_dialogue_id = next_id
				self.options_manager.deactivate()
				self.trigger_dialogue()
				return 

			else:
				next_dialogue_id = None
				if current_dialogue.next:
					next_dialogue_id = current_dialogue.next

			next_dialogue = None

			if next_dialogue_id != None:
				for dialogue in range(len(self.dialogues_list)):
					if self.dialogues_list[dialogue]["id"] == next_dialogue_id:
						next_dialogue = self.dialogues_list[dialogue]

			if not (current_dialogue.options == None and current_dialogue.next == None):
				self.current_dialogue_id = self.dialogues_list[self.dialogues_list.index(next_dialogue)]["id"]
			else:
				self.deactivate()

			print('next dialogue id- {self.current_dialogue_id}')
				
		else:
			
			print('dialogue manager is not active')

