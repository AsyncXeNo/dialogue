from dialogue import Dialogue
from option import Option
from utils import get_dialogues


class DialogueManager:
    def __init__(self):
        self.dialogues = list()
        self.active = False

    def activate(self):
    	self.active = True

    def set_active_dialogue(self, name):
        pass

    def trigger_dialogue(self):
    	pass