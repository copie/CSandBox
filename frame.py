from stack import stack
from g import builtin, global_
import copy


class MyFrame:
    def __init__(self, co):
        """dict 是保存 局部变量的,不要误认为是 f.local 了
        它在新的 frame 中和 f.global 是相同的.
        不要问我为什么这样处理因为 Python 源码的实现也是这样处理的."""
        self.co_consts = co.consts
        self.co_cellvars = co.cellvars
        self.co_freevars = co.freevars
        self.co_name = co.name
        self.co_names = co.names
        self.co_nlocals = co.nlocals
        self.co_argcount = co.argcount
        self.co_varnames = co.varnames
        self.stack = stack(size=co.stacksize)
        self.global_ = None
        self.local = None
        self.bulitin = None
        self.dict = copy.deepcopy(co.dict)
        self.index = None
        self.co_code = self.code_to_int(co.code)
        self.blocks = stack(size=20)  # python 中块级操作的堆栈.方便运行时堆栈的恢复

    def code_to_int(self, code):
        """将 co.co_code 中的 bytes 转为 [int]."""
        return [int(x) for x in code]


def new_frame(co_code):
    f = MyFrame(co_code)
    f.global_ = global_
    f.local = global_
    f.builtin = builtin
    f.index = 0
    return f
