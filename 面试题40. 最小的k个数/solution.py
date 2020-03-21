from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        stack = list()
        if k <= 0:
            return stack

        def adjust(index, k):
            while 2 * index + 1 < k:
                max_index = 2 * index + 1
                if 2 * index + 2 < k and stack[2 * index + 2] > stack[max_index]:
                    max_index = 2 * index + 2
                if stack[index] < stack[max_index]:
                    stack[index], stack[max_index] = stack[max_index], stack[index]
                    index = max_index
                else:
                    break

        for i in range(len(arr)):
            if i < k:
                stack.append(arr[i])
                if i == k - 1:
                    index = k // 2 - 1
                    while index >= 0:
                        adjust(index, k)
                        index -= 1
            else:
                if arr[i] < stack[0]:
                    stack[0] = arr[i]
                    adjust(0, k)
        result = list()
        while stack:
            stack[0], stack[-1] = stack[-1], stack[0]
            result.append(stack[-1])
            stack.pop()
            adjust(0, len(stack))
        return result[::-1]


if __name__ == '__main__':
    so = Solution()
    print(so.getLeastNumbers([0, 1, 1, 2, 4, 4, 1, 3, 3, 2], 6))
