from operator import le, lt, ge, gt, eq, ne, is_, is_not, contains, not_
from function import Function
from frame import new_frame

frames = []


class OpCode:
    cmp_op = (lt, le, eq, ne, gt, ge, lambda a, b: contains(b, a),
              lambda a, b: not_(contains(b, a)), is_, is_not)  # 支持的比较运算符

    def __init__(self, frame):
        self.frame = frame
        self.stack = frame.stack
        self.co_code = frame.co_code
        self.co_consts = frame.co_consts
        self.co_cellvars = frame.co_cellvars
        self.co_freevars = frame.co_freevars
        self.co_consts = frame.co_consts
        self.co_name = frame.co_name
        self.co_names = frame.co_names
        self.co_nlocals = frame.co_nlocals
        self.co_argcount = frame.co_argcount
        self.global_ = frame.global_
        self.local = frame.local
        self.builtin = frame.builtin
        self.dict = frame.dict
        self.co_varnames = frame.co_varnames
        self.blocks = frame.blocks
        self.if_return = False
        self.opcode_dict = {'1': 'POP_TOP',
                            '2': 'ROT_TWO',
                            '3': 'ROT_THREE',
                            '4': 'DUP_TOP',
                            '5': 'DUP_TOP_TWO',
                            '9': 'NOP',
                            '10': 'UNARY_POSITIVE',
                            '11': 'UNARY_NEGATIVE',
                            '12': 'UNARY_NOT',
                            '15': 'UNARY_INVERT',
                            '16': 'BINARY_MATRIX_MULTIPLY',
                            '17': 'INPLACE_MATRIX_MULTIPLY',
                            '19': 'BINARY_POWER',
                            '20': 'BINARY_MULTIPLY',
                            '22': 'BINARY_MODULO',
                            '23': 'BINARY_ADD',
                            '24': 'BINARY_SUBTRACT',
                            '25': 'BINARY_SUBSCR',
                            '26': 'BINARY_FLOOR_DIVIDE',
                            '27': 'BINARY_TRUE_DIVIDE',
                            '28': 'INPLACE_FLOOR_DIVIDE',
                            '29': 'INPLACE_TRUE_DIVIDE',
                            '50': 'GET_AITER',
                            '51': 'GET_ANEXT',
                            '52': 'BEFORE_ASYNC_WITH',
                            '55': 'INPLACE_ADD',
                            '56': 'INPLACE_SUBTRACT',
                            '57': 'INPLACE_MULTIPLY',
                            '59': 'INPLACE_MODULO',
                            '60': 'STORE_SUBSCR',
                            '61': 'DELETE_SUBSCR',
                            '62': 'BINARY_LSHIFT',
                            '63': 'BINARY_RSHIFT',
                            '64': 'BINARY_AND',
                            '65': 'BINARY_XOR',
                            '66': 'BINARY_OR',
                            '67': 'INPLACE_POWER',
                            '68': 'GET_ITER',
                            '69': 'GET_YIELD_FROM_ITER',
                            '70': 'PRINT_EXPR',
                            '71': 'LOAD_BUILD_CLASS',
                            '72': 'YIELD_FROM',
                            '73': 'GET_AWAITABLE',
                            '75': 'INPLACE_LSHIFT',
                            '76': 'INPLACE_RSHIFT',
                            '77': 'INPLACE_AND',
                            '78': 'INPLACE_XOR',
                            '79': 'INPLACE_OR',
                            '80': 'BREAK_LOOP',
                            '81': 'WITH_CLEANUP_START',
                            '82': 'WITH_CLEANUP_FINISH',
                            '83': 'RETURN_VALUE',
                            '84': 'IMPORT_STAR',
                            '85': 'SETUP_ANNOTATIONS',
                            '86': 'YIELD_VALUE',
                            '87': 'POP_BLOCK',
                            '88': 'END_FINALLY',
                            '89': 'POP_EXCEPT',
                            '90': 'STORE_NAME',
                            '91': 'DELETE_NAME',
                            '92': 'UNPACK_SEQUENCE',
                            '93': 'FOR_ITER',
                            '94': 'UNPACK_EX',
                            '95': 'STORE_ATTR',
                            '96': 'DELETE_ATTR',
                            '97': 'STORE_GLOBAL',
                            '98': 'DELETE_GLOBAL',
                            '100': 'LOAD_CONST',
                            '101': 'LOAD_NAME',
                            '102': 'BUILD_TUPLE',
                            '103': 'BUILD_LIST',
                            '104': 'BUILD_SET',
                            '105': 'BUILD_MAP',
                            '106': 'LOAD_ATTR',
                            '107': 'COMPARE_OP',
                            '108': 'IMPORT_NAME',
                            '109': 'IMPORT_FROM',
                            '110': 'JUMP_FORWARD',
                            '111': 'JUMP_IF_FALSE_OR_POP',
                            '112': 'JUMP_IF_TRUE_OR_POP',
                            '113': 'JUMP_ABSOLUTE',
                            '114': 'POP_JUMP_IF_FALSE',
                            '115': 'POP_JUMP_IF_TRUE',
                            '116': 'LOAD_GLOBAL',
                            '119': 'CONTINUE_LOOP',
                            '120': 'SETUP_LOOP',
                            '121': 'SETUP_EXCEPT',
                            '122': 'SETUP_FINALLY',
                            '124': 'LOAD_FAST',
                            '125': 'STORE_FAST',
                            '126': 'DELETE_FAST',
                            '127': 'STORE_ANNOTATION',
                            '130': 'RAISE_VARARGS',
                            '131': 'CALL_FUNCTION',
                            '132': 'MAKE_FUNCTION',
                            '133': 'BUILD_SLICE',
                            '135': 'LOAD_CLOSURE',
                            '136': 'LOAD_DEREF',
                            '137': 'STORE_DEREF',
                            '138': 'DELETE_DEREF',
                            '141': 'CALL_FUNCTION_KW',
                            '142': 'CALL_FUNCTION_EX',
                            '143': 'SETUP_WITH',
                            '144': 'EXTENDED_ARG',
                            '145': 'LIST_APPEND',
                            '146': 'SET_ADD',
                            '147': 'MAP_ADD',
                            '148': 'LOAD_CLASSDEREF',
                            '149': 'BUILD_LIST_UNPACK',
                            '150': 'BUILD_MAP_UNPACK',
                            '151': 'BUILD_MAP_UNPACK_WITH_CALL',
                            '152': 'BUILD_TUPLE_UNPACK',
                            '153': 'BUILD_SET_UNPACK',
                            '154': 'SETUP_ASYNC_WITH',
                            '155': 'FORMAT_VALUE',
                            '156': 'BUILD_CONST_KEY_MAP',
                            '157': 'BUILD_STRING',
                            '158': 'BUILD_TUPLE_UNPACK_WITH_CALL',
                            '257': 'EXCEPT_HANDLER'}

    def opcode_1(self, oparg):
        """弹出栈顶元素."""
        # define POP_TOP                   1
        self.stack.pop()

    def opcode_2(self, oparg):
        """交换栈顶和第二个的位置."""
        # define ROT_TWO                   2
        top = self.stack.top()
        second = self.stack.second()
        self.stack.set_top(second)
        self.stack.set_second(top)

    def opcode_3(self, oparg):
        """栈顶三个元素之间交换."""
        # define ROT_THREE                 3
        top = self.stack.pop()
        second = self.stack.pop()
        third = self.stack.pop()
        self.stack.push(top)
        self.stack.push(third)
        self.stack.push(second)

    def opcode_4(self, oparg):
        """复制栈顶并压入栈."""
        # define DUP_TOP                   4
        top = self.stack.top()
        self.stack.push(top)

    def opcode_5(self, oparg):
        """复制栈顶两个元素并压入栈, 顺序不变."""
        # define DUP_TOP_TWO               5
        top = self.stack.top()
        second = self.stack.second()
        self.stack.push(second)
        self.stack.push(top)

    def opcode_9(self, oparg):
        # define NOP                       9
        code = "NOP"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_10(self, oparg):

        # define UNARY_POSITIVE           10
        code = "UNARY_POSITIVE"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_11(self, oparg):
        """针对 -a 运算的字节码."""
        # define UNARY_NEGATIVE           11
        value = self.stack.pop()
        res = -value
        self.stack.push(res)

    def opcode_12(self, oparg):
        # define UNARY_NOT                12
        code = "UNARY_NOT"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_15(self, oparg):
        # define UNARY_INVERT             15
        value = self.stack.pop()
        res = ~value
        self.stack.push(res)

    def opcode_16(self, oparg):
        # define BINARY_MATRIX_MULTIPLY   16
        code = "BINARY_MATRIX_MULTIPLY"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_17(self, oparg):
        # define INPLACE_MATRIX_MULTIPLY  17
        code = "INPLACE_MATRIX_MULTIPLY"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_19(self, oparg):
        """乘方运算."""
        # define BINARY_POWER             19
        right = self.stack.pop()
        left = self.stack.pop()
        res = left ** right
        self.stack.push(res)

    def opcode_20(self, oparg):
        """乘法运算."""
        # define BINARY_MULTIPLY          20
        rigth = self.stack.pop()
        left = self.stack.pop()
        res = left * rigth
        self.stack.push(res)

    def opcode_22(self, oparg):
        """取模运算."""
        # define BINARY_MODULO            22
        divisor = self.stack.pop()
        dividend = self.stack.pop()
        res = dividend % divisor
        self.stack.push(res)

    def opcode_23(self, oparg):
        """加法运算."""
        # define BINARY_ADD               23
        right = self.stack.pop()
        left = self.stack.pop()
        res = left + right
        self.stack.push(res)

    def opcode_24(self, oparg):
        """减法运算."""
        # define BINARY_SUBTRACT          24
        right = self.stack.pop()
        left = self.stack.pop()
        res = left - right
        self.stack.push(res)

    def opcode_25(self, oparg):
        """如果 index 是数字的话就是按照索引取值,如果是 slice 就是取子序列."""
        # define BINARY_SUBSCR            25
        index = self.stack.pop()
        list_ = self.stack.pop()
        value = list_[index]
        self.stack.push(value)

    def opcode_26(self, oparg):
        """除法运算."""
        # define BINARY_FLOOR_DIVIDE      26
        right = self.stack.pop()
        left = self.stack.pop()
        res = left // right
        self.stack.push(res)

    def opcode_27(self, oparg):
        """真除法运算."""
        # define BINARY_TRUE_DIVIDE       27
        right = self.stack.pop()
        left = self.stack.pop()
        res = left / right
        self.stack.push(res)

    def opcode_28(self, oparg):
        """就地除法运算."""
        # define INPLACE_FLOOR_DIVIDE     28
        right = self.stack.pop()
        left = self.stack.pop()
        left //= right
        self.stack.push(left)

    def opcode_29(self, oparg):
        """就地真除法运算."""
        # define INPLACE_TRUE_DIVIDE      29
        right = self.stack.pop()
        left = self.stack.pop()
        left /= right
        self.stack.push(left)

    def opcode_50(self, oparg):
        # define GET_AITER                50
        code = "GET_AITER"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_51(self, oparg):
        # define GET_ANEXT                51
        code = "GET_ANEXT"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_52(self, oparg):

        # define BEFORE_ASYNC_WITH        52
        code = "BEFORE_ASYNC_WITH"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_55(self, oparg):
        """就地加法运算."""
        # define INPLACE_ADD              55
        right = self.stack.pop()
        left = self.stack.pop()
        left += right
        self.stack.push(left)

    def opcode_56(self, oparg):
        """就地减法运算."""
        # define INPLACE_SUBTRACT         56
        right = self.stack.pop()
        left = self.stack.pop()
        left -= right
        self.stack.push(left)

    def opcode_57(self, oparg):
        """就地乘法运算."""
        # define INPLACE_MULTIPLY         57
        right = self.stack.pop()
        left = self.stack.pop()
        left *= right
        self.stack.push(left)

    def opcode_59(self, oparg):
        """就地取模运算."""
        # define INPLACE_MODULO           59
        right = self.stack.pop()
        left = self.stack.pop()
        left %= right
        self.stack.push(left)

    def opcode_60(self, oparg):
        """将一个序列插入另外一个序列 a[1:2] = [1,2,3,4,5,6]."""
        # define STORE_SUBSCR             60
        s = self.stack.pop()
        x = self.stack.pop()
        other_list = self.stack.pop()
        x[s] = other_list

    def opcode_61(self, oparg):
        # define DELETE_SUBSCR            61
        code = "DELETE_SUBSCR"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_62(self, oparg):
        """左移运算"""
        # define BINARY_LSHIFT            62
        right = self.stack.pop()
        left = self.stack.pop()
        res = left << right
        self.stack.push(res)

    def opcode_63(self, oparg):
        """右移运算"""
        # define BINARY_RSHIFT            63
        rigth = self.stack.pop()
        left = self.stack.pop()
        res = left >> rigth
        self.stack.push(res)

    def opcode_64(self, oparg):
        """与运算"""
        # define BINARY_AND               64
        rigth = self.stack.pop()
        left = self.stack.pop()
        res = left & rigth
        self.stack.push(res)

    def opcode_65(self, oparg):
        """异或运算"""
        # define BINARY_XOR               65
        rigth = self.stack.pop()
        left = self.stack.pop()
        res = left ^ rigth
        self.stack.push(res)

    def opcode_66(self, oparg):
        """或运算"""
        # define BINARY_OR                66
        rigth = self.stack.pop()
        left = self.stack.pop()
        res = left | rigth
        self.stack.push(res)

    def opcode_67(self, oparg):
        """就地乘方运算."""
        # define INPLACE_POWER            67
        right = self.stack.pop()
        left = self.stack.pop()
        left **= right
        self.stack.push(left)

    def opcode_68(self, oparg):
        """获取可迭代对象的迭代器."""
        # define GET_ITER                 68
        a = self.stack.pop()
        it = iter(a)
        self.stack.push(it)

    def opcode_69(self, oparg):
        # define GET_YIELD_FROM_ITER      69
        code = "GET_YIELD_FROM_ITER"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_70(self, oparg):
        # define PRINT_EXPR               70
        code = "PRINT_EXPR"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_71(self, oparg):
        # define LOAD_BUILD_CLASS         71
        # code = "LOAD_BUILD_CLASS"
        # raise RuntimeError("使用到未实现的字节码:"+code)
        print(self.stack)
    def opcode_72(self, oparg):
        # define YIELD_FROM               72
        code = "YIELD_FROM"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_73(self, oparg):
        # define GET_AWAITABLE            73
        code = "GET_AWAITABLE"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_75(self, oparg):
        # define INPLACE_LSHIFT           75
        code = "INPLACE_LSHIFT"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_76(self, oparg):
        # define INPLACE_RSHIFT           76
        code = "INPLACE_RSHIFT"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_77(self, oparg):
        """按位与运算"""
        # define INPLACE_AND              77
        right = self.stack.pop()
        left = self.stack.pop()
        left &= right
        self.stack.push(left)

    def opcode_78(self, oparg):
        # define INPLACE_XOR              78
        code = "INPLACE_XOR"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_79(self, oparg):
        """按位或运算"""
        # define INPLACE_OR               79
        right = self.stack.pop()
        left = self.stack.pop()
        left |= right
        self.stack.push(left)

    def opcode_80(self, oparg):
        """循环结束."""
        # define BREAK_LOOP               80
        self.frame.index = self.forend
        self.stack.pop()

    def opcode_81(self, oparg):

        # define WITH_CLEANUP_START       81
        code = "WITH_CLEANUP_START"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_82(self, oparg):
        # define WITH_CLEANUP_FINISH      82
        code = "WITH_CLEANUP_FINISH"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_83(self, oparg):
        """返回值."""
        # define RETURN_VALUE             83
        value = self.stack.pop()
        index = frames.index(self.frame)
        if (index != 0):
            frame = frames[index-1]
            frame.stack.push(value)
            self.if_return = True
        else:
            exit(0)

    def opcode_84(self, oparg):
        # define IMPORT_STAR              84
        code = "IMPORT_STAR"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_85(self, oparg):
        # define SETUP_ANNOTATIONS        85
        code = "SETUP_ANNOTATIONS"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_86(self, oparg):
        # define YIELD_VALUE              86
        code = "YIELD_VALUE"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_87(self, oparg):
        """这个我只针对了 for 进行的处理."""
        # define POP_BLOCK                87
        p = self.blocks.pop()
        index = len(self.stack)
        while index > p:
            self.stack.pop()
            index -= 1

    def opcode_88(self, oparg):
        # define END_FINALLY              88
        code = "END_FINALLY"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_89(self, oparg):
        # define POP_EXCEPT               89
        code = "POP_EXCEPT"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_90(self, oparg):
        """给相应对象设置名字."""
        # define STORE_NAME               90
        value = self.stack.pop()
        name = self.co_names[oparg]
        self.local[name] = value

    def opcode_91(self, oparg):
        # define DELETE_NAME              91
        code = "DELETE_NAME"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_92(self, oparg):
        """从堆栈中获取一个可迭代的对象然后对它进行拆包然后倒序压入栈"""
        # define UNPACK_SEQUENCE          92
        sequence = self.stack.pop()
        for item in sequence[::-1]:
            self.stack.push(item)

    def opcode_93(self, oparg):
        # define FOR_ITER                 93
        it = self.stack.top()
        try:
            value = next(it)
            self.stack.push(value)
        except StopIteration:
            self.stack.pop()
            self.frame.index += oparg

    def opcode_94(self, oparg):
        # define UNPACK_EX                94
        code = "UNPACK_EX"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_95(self, oparg):
        # define STORE_ATTR               95
        code = "STORE_ATTR"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_96(self, oparg):
        # define DELETE_ATTR              96
        code = "DELETE_ATTR"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_97(self, oparg):
        # define STORE_GLOBAL             97
        name = self.co_names[oparg]
        value = self.stack.pop()
        self.global_[name] = value

    def opcode_98(self, oparg):
        # define DELETE_GLOBAL            98
        code = "DELETE_GLOBAL"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_100(self, oparg):
        # define LOAD_CONST              100
        value = self.co_consts[oparg]
        self.stack.push(value)

    def opcode_101(self, oparg):
        # define LOAD_NAME               101
        name = self.co_names[oparg]
        value = None
        if name in self.local:
            value = self.local[name]
        if not value:
            if name in self.global_:
                value = self.global_[name]
        if not value:
            if name in self.builtin:
                value = self.builtin[name]
        self.stack.push(value)

    def opcode_102(self, oparg):
        # define BUILD_TUPLE             102
        list_ = []
        for _ in range(oparg):
            a = self.stack.pop()
            list_.append(a)
        res = tuple(list_[::-1])
        self.stack.push(res)

    def opcode_103(self, oparg):
        # define BUILD_LIST              103
        list_ = []
        for i in range(oparg):
            value = self.stack.pop()
            list_.append(value)
        self.stack.push(list_[::-1])

    def opcode_104(self, oparg):
        # define BUILD_SET               104
        code = "BUILD_SET"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_105(self, oparg):
        # define BUILD_MAP               105
        res = {}
        values = []
        keys = []
        for _ in range(oparg):
            values.append(self.stack.pop())
            keys.append(self.stack.pop())
        for key, value in zip(keys[::-1], values[::-1]):
            res[key] = value
        self.stack.push(res)

    def opcode_106(self, oparg):
        """屏蔽所以 LOAD_ATTR 中以 __ 开头的并且不是 __init__ 的所有属性"""
        # define LOAD_ATTR               106
        c = self.stack.pop()
        name = self.co_names[oparg]
        assert not (name.startswith("__") and name != "__init__")
        res = getattr(c, name)
        self.stack.push(res)

    def opcode_107(self, oparg):
        # define COMPARE_OP              107
        right = self.stack.pop()
        left = self.stack.pop()
        cmp_ = self.cmp_op[oparg]
        res = cmp_(left, right)
        self.stack.push(res)

    def opcode_108(self, oparg):
        # define IMPORT_NAME             108
        code = "IMPORT_NAME"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_109(self, oparg):
        # define IMPORT_FROM             109
        code = "IMPORT_FROM"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_110(self, oparg):
        # define JUMP_FORWARD            110
        self.frame.index += oparg

    def opcode_111(self, oparg):
        # define JUMP_IF_FALSE_OR_POP    111
        cond = self.stack.top()
        if cond is True:
            self.stack.pop()
        else:
            self.frame.index = oparg

    def opcode_112(self, oparg):
        # define JUMP_IF_TRUE_OR_POP     112
        cond = self.stack.top()
        if cond is True:
            self.frame.index = oparg
        else:
            self.stack.pop()

    def opcode_113(self, oparg):
        # define JUMP_ABSOLUTE           113
        self.frame.index = oparg

    def opcode_114(self, oparg):
        # define POP_JUMP_IF_FALSE       114
        a = self.stack.pop()
        if a:
            pass
        else:
            self.frame.index = oparg

    def opcode_115(self, oparg):
        # define POP_JUMP_IF_TRUE        115
        a = self.stack.pop()
        if a:
            self.frame.index = oparg

    def opcode_116(self, oparg):
        # define LOAD_GLOBAL             116
        name = self.co_names[oparg]
        if name in self.global_:
            value = self.global_[name]
        else:
            value = self.builtin[name]
        self.stack.push(value)

    def opcode_119(self, oparg):
        # define CONTINUE_LOOP           119
        code = "CONTINUE_LOOP"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_120(self, oparg):
        # define SETUP_LOOP              120
        p = len(self.stack)
        self.blocks.push(p)    # 将当前运行时栈长度压入 blocks 栈
        self.forend = self.frame.index + oparg

    def opcode_121(self, oparg):
        # define SETUP_EXCEPT            121
        code = "SETUP_EXCEPT"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_122(self, oparg):
        # define SETUP_FINALLY           122
        code = "SETUP_FINALLY"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_124(self, oparg):
        # define LOAD_FAST               124
        name = self.co_varnames[oparg]
        try:
            value = self.dict[self.co_varnames[oparg]]
        except KeyError as e:
            raise TypeError("missing " + name)
        self.stack.push(value)

    def opcode_125(self, oparg):
        # define STORE_FAST              125
        name = self.co_varnames[oparg]
        value = self.stack.pop()
        self.dict[name] = value

    def opcode_126(self, oparg):
        # define DELETE_FAST             126
        code = "DELETE_FAST"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_127(self, oparg):
        # define STORE_ANNOTATION        127
        code = "STORE_ANNOTATION"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_130(self, oparg):
        # define RAISE_VARARGS           130
        code = "RAISE_VARARGS"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_131(self, oparg):
        # define CALL_FUNCTION           131
        args = []

        for _ in range(oparg):
            args.append(self.stack.pop())

        func = self.stack.pop()
        if callable(func):
            res = func(*args[::-1])
            self.stack.push(res)
        elif(isinstance(func, Function)):
            frame = new_frame(func)
            if oparg > frame.co_argcount:
                raise TypeError(
                    f"{frame.co_name}() takes {frame.co_argcount} positional \
                        arguments but {oparg} were given")

            if oparg < frame.co_argcount:
                raise TypeError(
                    f"{frame.co_name}() missing {frame.co_argcount - oparg} \
                    required positional arguments: "
                    + ",".join(frame.co_varnames[oparg:]))

            for name, value in zip(func.varnames, args[::-1]):
                frame.dict[name] = value

            frames.append(frame)
            run(frame)
            frames.pop()
        else:
            raise RuntimeError("有些事情没有考虑到")

    def opcode_132(self, oparg):
        # define MAKE_FUNCTION           132
        name = self.stack.pop()
        mycode = self.stack.pop()
        f = Function(name, mycode)
        for i in f.freevars:
            f.dict[i] = self.dict[i]
        self.stack.push(f)

    def opcode_133(self, oparg):
        # define BUILD_SLICE             133
        args = []
        for _ in range(oparg):
            args.append(self.stack.pop())
        value = slice(*args[::-1])
        self.stack.push(value)

    def opcode_135(self, oparg):
        # define LOAD_CLOSURE            135
        key = self.co_cellvars[oparg]
        value = self.dict[key]
        self.stack.push(value)

    def opcode_136(self, oparg):
        # define LOAD_DEREF              136
        cell = self.co_freevars[oparg]
        value = self.dict[cell]
        self.stack.push(value)

    def opcode_137(self, oparg):
        # define STORE_DEREF             137
        value = self.stack.pop()
        key = self.co_cellvars[oparg]
        self.dict[key] = value

    def opcode_138(self, oparg):
        # define DELETE_DEREF            138
        code = "DELETE_DEREF"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_141(self, oparg):
        # define CALL_FUNCTION_KW        141
        code = "CALL_FUNCTION_KW"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_142(self, oparg):
        # define CALL_FUNCTION_EX        142
        code = "CALL_FUNCTION_EX"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_143(self, oparg):
        # define SETUP_WITH              143
        code = "SETUP_WITH"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_144(self, oparg):
        """计算下一条字节码的参数"""
        # define EXTENDED_ARG            144
        oldoparg = oparg
        oparg = self.frame.co_code[self.frame.index+1]
        oparg |= oldoparg << 8
        self.frame.co_code[self.frame.index+1] = oparg

    def opcode_145(self, oparg):
        # define LIST_APPEND             145
        v = self.stack.pop()
        list_ = self.stack.peek(oparg)
        list_.append(v)

    def opcode_146(self, oparg):
        # define SET_ADD                 146
        code = "SET_ADD"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_147(self, oparg):
        # define MAP_ADD                 147
        key = self.stack.pop()
        value = self.stack.pop()
        map_ = self.stack.peek(oparg)
        map_[key] = value

    def opcode_148(self, oparg):
        # define LOAD_CLASSDEREF         148
        code = "LOAD_CLASSDEREF"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_149(self, oparg):
        # define BUILD_LIST_UNPACK       149
        code = "BUILD_LIST_UNPACK"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_150(self, oparg):
        # define BUILD_MAP_UNPACK        150
        code = "BUILD_MAP_UNPACK"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_151(self, oparg):
        # define BUILD_MAP_UNPACK_WITH_CALL 151
        code = "BUILD_MAP_UNPACK_WITH_CALL"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_152(self, oparg):
        # define BUILD_TUPLE_UNPACK      152
        code = "BUILD_TUPLE_UNPACK"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_153(self, oparg):
        # define BUILD_SET_UNPACK        153
        code = "BUILD_SET_UNPACK"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_154(self, oparg):
        # define SETUP_ASYNC_WITH        154
        code = "SETUP_ASYNC_WITH"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_155(self, oparg):
        # define FORMAT_VALUE            155
        code = "FORMAT_VALUE"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_156(self, oparg):
        # define BUILD_CONST_KEY_MAP     156
        keys = self.stack.pop()
        values = []
        for _ in range(oparg):
            t = self.stack.pop()
            values.append(t)
        values = values[::-1]
        res = dict(zip(keys, values))
        self.stack.push(res)

    def opcode_157(self, oparg):
        # define BUILD_STRING            157
        code = "BUILD_STRING"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_158(self, oparg):
        # define BUILD_TUPLE_UNPACK_WITH_CALL 158
        code = "BUILD_TUPLE_UNPACK_WITH_CALL"
        raise RuntimeError("使用到未实现的字节码:"+code)

    def opcode_257(self, oparg):
        # define EXCEPT_HANDLER 25
        code = "EXCEPT_HANDLER"
        raise RuntimeError("使用到未实现的字节码:"+code)


def run(f):
    run_code = OpCode(f)
    co_code = f.co_code
    while True:
        code = str(co_code[f.index])
        oparg = int(co_code[f.index+1])
        f.index += 2
        # import time
        # time.sleep(0.2)
        # print("下一个字节码的地址是",f.index)
        # print(run_code.opcode_dict[code],"     ",oparg)
        func = getattr(run_code, "opcode_"+code)
        if func:
            func(oparg)
        if f.index == len(co_code) or run_code.if_return is True:
            break
