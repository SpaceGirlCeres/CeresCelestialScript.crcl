import importlib
from CErr import *

class Interpreter:
    def __init__(self, text="", included={}):
        self.filename=input("Type the file name you wish to run:\n")
        self.text = text
        self.included = included

    def load_file(self):
        if self.filename[-5:] != ".crcl":
            rec=self.filename
            while rec[0] != ".":
                rec = rec[1:]
            return Error.file_err(self, "!crcl", ".crcl", rec)

        try:
            with open(self.filename, "r") as file:
                self.text = file.read()
        except FileNotFoundError:
            return Error.file_err(self, "file!found", self.filename)

    def include(self, libs=[]):
        for module_name in libs:
            try:
                module = importlib.import_module(module_name)
                self.included[module_name] = module
            except ImportError as e:
                return Error.import_err(self, "lib!found", module_name)


Interpreter.__init__(Interpreter)
Interpreter.load_file(Interpreter)
