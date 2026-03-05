import importlib
from CErr import *

class Interpreter:
    def __init__(self, text="", included={}, tokens={}):
        self.filename=input("Type the file name you wish to run:\n")
        self.text = text
        self.included = included
        self.tokens = tokens

        self.load_file()

    def load_file(self):
        if self.filename[-5:] != ".crcl":
            rec=self.filename
            while rec != "" and rec[0] != ".":
                rec = rec[1:]
            if rec == "":
                rec = "NULLTYPE"
            return Error.file_err(self, "!crcl", ".crcl", rec)

        try:
            with open(self.filename, "r") as file:
                self.text = file.read()
        except FileNotFoundError:
            return Error.file_err(self, "file!found", self.filename)

        self.tokenizer()

    def include(self, libs=[]):
        for module_name in libs:
            try:
                module = importlib.import_module(module_name)
                self.included[module_name] = module
            except ImportError:
                return Error.import_err(self, "lib!found", module_name)


    def tokenizer(self):
        # seperate self.text into lines
        lines = self.text.split("\n")

        # seperates tokens by spaces
        for line in range(len(lines)):
            self.tokens[line + 1] = lines[line].split(" ")


Interpreter()
