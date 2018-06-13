class Function:
    def __init__(self, name, co_code):
        self.name = name
        self.code = co_code.co_code
        self.consts = co_code.co_consts
        self.cellvars = co_code.co_cellvars
        self.freevars = co_code.co_freevars
        self.names = co_code.co_names
        self.nlocals = co_code.co_nlocals
        self.argcount = co_code.co_argcount
        self.varnames = co_code.co_varnames
        self.stacksize = co_code.co_stacksize
        self.dict = {}

    def __repr__(self):
        return f"<Function {self.name}>"
