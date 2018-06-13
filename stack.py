class stack:
    def __init__(self,*,size):
        self.size = size
        self.stack = []
    
    def push(self, value):
        assert len(self.stack)+1 <= self.size
        # print(self.stack)
        self.stack.append(value)
    
    def top(self):
        assert len(self.stack) != 0
        return self.stack[-1]
    
    def second(self):
        assert len(self.stack)-1 != 0
        return self.stack[-2]
    
    def pop(self):
        # assert len(self.stack) != 0
        return self.stack.pop()
    
    def set_value(self, index, value):
        assert len(self.stack)+1 <= self.size
        self.stack[index] = value
    
    def set_top(self, value):
        assert len(self.stack) != 0
        self.stack[-1] = value
    
    def set_second(self, value):
        assert len(self.stack)-1 != 0
        self.stack[-2] = value

    def peek(self,n): 
        return self.stack[-n]

    def __repr__(self):
        return str(self.stack)
    
    def __len__(self):
        return len(self.stack)