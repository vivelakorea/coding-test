class MyStack:

    def __init__(self):
        import collections
        """
        Initialize your data structure here.
        """
        self.d = collections.deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.d.append(x)
        for _ in range(len(self.d) - 1):
            self.d.append(self.d.popleft())
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.d.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return (self.d)[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.d) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(10)
obj.push(20)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()

print(param_2, param_3, param_4)