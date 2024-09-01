"""
Given a list of numbers and a number k, return whether any 
two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, 
return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def solve(nums, k):

    seen = set()

    for i in nums:
        complement = k - i
        if complement in seen:
            return True
        seen.add(i)
    return False

print(solve([10, 15, 3, 7], 17))
print(solve([], 1))

    


