class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # Start with a list of "x" placeholders
        k = [["x"] * len(nums)]
        l = len(nums)
        t = 0

        def assigner(a, c, arr):
            count = 0
            for i, val in enumerate(arr):
                if val == "x":   # look for "x" instead of 0
                    count += 1
                    if count == c:  # replace the c-th "x"
                        arr[i] = a
                        break
            return arr

        while t < len(nums):
            a = nums[t]
            E = []
            for arr in k:              # iterate over each current list
                for i in range(l):     # replace the i+1-th "x"
                    temp = arr[:]      # slicing instead of deepcopy
                    assigner(a, i+1, temp)
                    E.append(temp)
            k = E
            t += 1
            l -= 1

        return k