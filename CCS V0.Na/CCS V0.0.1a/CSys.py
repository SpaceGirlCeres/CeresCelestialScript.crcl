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


        def prntln(self, text="",):
            if text[0] != "{" and text[len(text)-1] != "}":
                print(text)
            else:
                out = ""
                for char in text:
                    if char not in "{}":
                        out += char
                if out in Var.vars:
                    print(Var.vars[f"{out}"][1])
                else:
                    print(text)

        # Formated Printing Mostly Finished
        def prntf(self, text="", vars:list=[]):
            out = f""
            v_index=0
            for char in text:
                if char != "~":
                    out += char
                else:
                    out += str(vars[v_index])
                    v_index+=1
            print(out)

    class Cin:
        def __init__(self):
            pass

        def uIn(self, prompt = ""):
            return input(f"{prompt}")