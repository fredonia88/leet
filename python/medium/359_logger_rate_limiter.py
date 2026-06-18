class Logger:

    def __init__(self):
        self.messages = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messages: 
            self.messages[message] = timestamp
            return True
        elif timestamp - self.messages[message] >= 10:
            self.messages[message] = timestamp
            return True
        else:
            return False

if __name__ == '__main__':
    logger = Logger()
    logs = [[1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]]
    result = [logger.shouldPrintMessage(log[0], log[1]) for log in logs]
    print(result)
        