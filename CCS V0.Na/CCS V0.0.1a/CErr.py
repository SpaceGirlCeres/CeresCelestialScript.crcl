class Error:
    def __init__(self, err_type, expct, rec, arg):
        self.err_type = err_type
        self.expct = expct
        self.rex = rec
        self.arg = arg

    def var_err(self, err_type, expct="", rec=""):
        print(f'Variable error {err_type}\n')
        if err_type == "var_type!":
            print(f"Variable Type `{expct}` Not Found")
            quit(1)
        if err_type == "val!=type":
            print(f"Expected type {expct}, Got {rec}")
            quit(1)
        if err_type == "dupe_name":
            print(f"Duplicate variable '{expct}'")
            quit(1)
        if err_type == "var_name!":
            print(f"Variable Name '{expct}' Not Found")
            quit(1)

    def str_err(self, err_type, expct="", rec=""):
        print(f'String error {err_type}\n')
        if err_type == "fstr_index":
            print(f"FString index out of range, Expected at most {expct} inputs, got {rec} inputs")
            quit(2)