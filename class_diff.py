class Difference:

    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        diff_arr = []
        for i in self.__elements:
            for j in  self.__elements:
                if abs(i - j) in diff_arr or i == j:
                    continue
                else:
                    diff_arr.append(abs(i - j))
        if not diff_arr:
            diff_arr.append(0)
        self.maximumDifference = max(diff_arr)



_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)