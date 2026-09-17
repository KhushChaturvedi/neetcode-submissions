class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        pairs = self.store[key]

        left = 0
        right = len(pairs) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if pairs[mid][0] <= timestamp:
                result = pairs[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return result
