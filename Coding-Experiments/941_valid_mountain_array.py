class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_element: int = max(arr)
        found: bool = False
        prev: int | float = float("-inf")

        if arr[0] == max_element or arr[-1] == max_element:
            return False

        for element in arr:

            if element == max_element:
                found = True
                max_element = None

            elif not found:
                if element <= prev:
                    return False

            elif found:
                if element >= prev:
                    return False

            prev = element
        return True