#week07-5.py ¾Ç²ß­pµe
#933. Number of Recent Calls
class RecentCounter:

    def __init__(self):
        self.quene = deque()


    def ping(self, t: int) -> int:
        self.quene.append(t)
        while self.quene[0] < t-3000:
            self.quene.popleft()
        return len(self.quene)
