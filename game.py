"""
1 - left click
2 - middle click
3 - right click
4 - scroll up
5 - scroll down
"""
"""
class Event:
    def __init__(self, event_type, event_dict=None, sdl_event=None, 
                 keep_userdata=False, **attributes):
        '''Create a new event object.
        Creates a new event with the given type. The event is created with the
        given attributes and values. The attributes can come from a dictionary
        argument, or as string keys from a dictionary. 
        The given attributes will be readonly attributes on the new event
        object itself. These are the only attributes on the Event object,
        there are no methods attached to Event objects.
        :Parameters:
            `event_type` : int
                Event type to create
            `event_dict` : dict
                Dictionary of attributes to assign.
            `sdl_event` : `SDL_Event`
                Construct a Pygame event from the given SDL_Event; used
                internally.
            `keep_userdata` : bool
                Used internally.
            `attributes` : additional keyword arguments
                Additional attributes to assign to the event.
"""
"""

"""

import pygame
from pygame_input import Inputs, Button
import sys

from dialogue_manager import DialogueManager
from options_manager import OptionsManager
from input import InputManager


class Game:
    def __init__(self):
        pygame.init()

        self.SCREEN_WIDTH = 500
        self.SCREEN_HEIGHT = 600
        self.CAPTION = 'dialogue_test'
        self.FPS = 60

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT,))
        pygame.display.set_caption(self.CAPTION)

        self.clock = pygame.time.Clock()

        self.options_manager = OptionsManager()
        self.dialogue_manager = DialogueManager(self.options_manager)
        print("Activated")
        self.dialogue_manager.activate()
        self.dialogue_manager.set_active_dialogue("person1")

    def on_interact(self):
        if self.dialogue_manager.active:
            self.dialogue_manager.trigger_dialogue()

    def event_handler(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
            
                self.on_interact()

    def key_handler(self):
        pass

    def graphics_handler(self):
        self.screen.fill(pygame.Color('gold'))

        # draw stuff here


        pygame.display.update()
        self.clock.tick(self.FPS)

    def run(self):
        while True:
            self.event_handler()
            self.key_handler()
            self.graphics_handler()

if __name__ == "__main__":
    game = Game()
    game.run()