import pygame
pygame.init()

class OptionsManager:
	def __init__(self):
		self.active = False
		self.options = []

	def activate(self):
		self.active = True

	def deactivate(self):
		self.active = False
		self.options = []

	def set_options(self, options):
		self.options = options

	def show_options(self):
		for option in self.options:
			print (f'{self.options.index(option) + 1}. {option.string}')

		while True:
			number = input('type the number of option to choose and press enter.')
			try:
				number = int(number)
			except:
				print('please input a number')
				continue

			if number < 1 or number > len(self.options):
				print('pls enter a valid option number')
				continue

			else:
				break

		return self.options[number -1].dialogue_id
