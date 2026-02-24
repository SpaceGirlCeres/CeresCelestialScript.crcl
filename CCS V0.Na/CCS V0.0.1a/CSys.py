import pygame
import pygame_gui
import sys
import time

from CStd import *
from CErr import *

class CIRCLEngine:
    def __init__(self, screen = "", width = 800, height = 600, name = "CIRCLE Window", icon="crcl.png"):
        pygame.init()

        self.width = width
        self.height = height
        self.name = name
        self.icon = icon
        self.screen = screen


    global White, Black
    White = (255, 255, 255)
    Black = (0, 0, 0)

    def create_window(self):
        self.icon = pygame.image.load(self.icon)

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name)
        pygame.display.set_icon(self.icon)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
        sys.exit()

class System:
    def __init__(self):
        pass

    class COut:
        def __init__(self):
            pass

        # unformated printing, can take in 1 vaiable
        def prntln(self, text="", cvar=""):
            if cvar == "":
                print(text)
            else:
                if cvar in Var.vars:
                    print(f"{text}{Var.vars[cvar][1]}")
                else:
                    Error.var_err(Var, "var_name!", cvar)

        # Formated Printing UNFINISHED
        def prntf(self):
            pass

    class Cin:
        def __init__(self):
            pass

        def uIn(self, prompt = ""):
            return input(f"{prompt}")