import heapq


class PriorityQueue:
    def __init__(self):
        self.REMOVED = -10 ** 9
        self.heap = []
        self.priorities = {}

    def insert(self, state, new_priority):
        old_priority = self.priorities.get(state)
        if old_priority is None or new_priority < old_priority:
            self.priorities[state] = new_priority
            heapq.heappush(self.heap, (new_priority, state))

    def extract_min(self):
        while len(self.heap) > 0:
            priority, state = heapq.heappop(self.heap)
            if self.priorities[state] == self.REMOVED:
                continue
            self.priorities[state] = self.REMOVED
            return state, priority
        return None, None

    def __len__(self):
        return len(self.heap)
