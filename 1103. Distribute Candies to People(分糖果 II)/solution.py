from typing import List
'''
可以利用等差数列公式求解轮数

'''

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0 for _ in range(num_people)]
        episode = 0
        num = (1 + num_people) / 2
        people_use, last_use = 0, 0
        while people_use < candies:
            last_use = people_use
            people_use += num * num_people
            episode += 1
            num += num_people
        last_use = candies - last_use
        for i in range(num_people):
            now_last = i + 1 + (episode - 1) * num_people
            if last_use >= now_last:
                result[i] = int((i + 1 + now_last) / 2 * episode)
                last_use -= now_last
            else:
                result[i] = int((i + 1 + now_last - num_people) / 2 * (episode - 1) + last_use)
                last_use = 0
        return result


if __name__ == '__main__':
    so = Solution()
    candies = 7
    num_people = 4
    print(so.distributeCandies(candies,num_people))
