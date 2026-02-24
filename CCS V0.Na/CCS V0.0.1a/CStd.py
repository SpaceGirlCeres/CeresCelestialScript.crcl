from CErr import *

class Var:
    vars = {}

    def __init__(self, typed, value):
        self.typed = typed
        self.value = value


    def let(self, name, typed, value):
        types = {"int": int, "flt": float, "bol": bool, "dic": dict, "str": str}
        if typed not in types:
            return Error.var_err(self, "var_type!", typed)
        else:
            self.typed = types[typed]

        if type(value) != self.typed:
            return Error.var_err(self, "val!=type", f"{self.typed}", f"{type(value)}")

        if name in Var.vars:
            return Error.var_err(self, "dupe_name", f"{name}")

        Var.vars[f'{name}'] = (typed, value)