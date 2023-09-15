class MyHashSet(object):
    def __init__(self):
        self.hashSet = [[] for i in range(101)]

    def binSearch(self, numList, val):
        length = len(numList)
        left, right, = 0, length - 1
        while left < right:
            midpoint = (left + right) // 2
            if numList[midpoint] == val:
                return True, midpoint
            elif numList[midpoint] < val:
                left = midpoint + 1
            else:
                right = midpoint - 1
        if left < len(numList) and numList[left] < val:
            left += 1
        if left < len(numList) and numList[left] == val:
            return True, left
        return False, left

    def add(self, key):
        if len(self.hashSet[key % 100]) == 0:
            self.hashSet[key % 100].append(key)
        else:
            found = self.binSearch(self.hashSet[key % 100], key)
            if not found[0]:
                self.hashSet[key % 100].insert(found[1], key)

    def remove(self, key):
        result = self.binSearch(self.hashSet[key % 100], key)
        if result[0]:
            self.hashSet[key % 100].pop(result[1])

    def contains(self, key):
        return self.binSearch(self.hashSet[key % 100], key)[0]