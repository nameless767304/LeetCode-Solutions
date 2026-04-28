class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        self.stack_2 = []
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())

        val = self.stack_2.pop()
        self.stack_1 = [] 
        
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())

        return val

    def peek(self) -> int:
        self.stack_2 = []
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())

        val = self.stack_2[-1]
        self.stack_1 = [] 
        
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())

        return val


    def empty(self) -> bool:
        return False if len(self.stack_1) else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()