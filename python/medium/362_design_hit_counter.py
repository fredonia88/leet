class HitCounter:

    def __init__(self):
        self.hit_map = {}

    def hit(self, timestamp: int) -> None:
        self.hit_map[timestamp] = self.hit_map.get(timestamp, 0) + 1

    def getHits(self, timestamp: int) -> int:
        hits = 0
        for tm, hit in self.hit_map.items():
            if timestamp - tm < 300:
                hits += hit
        return hits
    
if __name__ == '__main__':
    sol = HitCounter()
    for i in range(1, 8):
        if i < 4:
            print(sol.hit(i))
        elif i == 5:
            print(sol.hit(300))
        elif i == 4:
            print(sol.getHits(4))
        elif i == 6:
            print(sol.getHits(300))
        else:
            print(sol.getHits(301))
