class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0
        r = len(people) - 1
        boats = 0

        while l <= r:
            rem = limit - people[r]
            boats+=1
            r-=1
            if rem>=people[l]:
                l+=1


        

        return boats