from CStd import *
from CErr import *

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
                    print(Var.get(out))
                else:
                    print(text)

        # Formatted Printing Mostly Finished
        def prntf(self, text="", vars:list=[]):
            out = f""
            v_index=0
            for char in text:
                if char != "~":
                    out += char
                else:
                    if v_index > len(vars)-1:
                        return Error.str_err(self, "fstr_index", len(vars), v_index+1)
                    out += str(vars[v_index])
                    v_index+=1
            print(out)

    class Cin:
        def __init__(self):
            pass

        def uIn(self, prompt = ""):
            return input(f"{prompt}")