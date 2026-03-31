class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.insert(0, x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop(0)
        else:
            return -1
    
    def increment(self, k: int, val: int) -> None:
        for i in range(max(len(self.stack) - k, 0), len(self.stack)):
            self.stack[i] = self.stack[i] + val

if __name__ == '__main__':
    sol = CustomStack(3)
    sol.push(2)
    print(sol.stack)
    sol.push(3)
    print(sol.stack)
    sol.push(4)
    print(sol.stack)
    sol.pop()
    print(sol.stack)
    sol.increment(1,100)
    print(sol.stack)
    sol.pop()
    print(sol.stack)
    sol.pop()
    print(sol.stack)

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)