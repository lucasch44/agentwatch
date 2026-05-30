
class LoopDetector:
    def __init__(self):
        self.last = None
        self.count = 0

    def check(self, action):
        if action == self.last:
            self.count += 1
        else:
            self.last = action
            self.count = 1
        return self.count >= 5
