'''
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". 
Input will always be valid, i.e. no negative integers.
'''

def count_sheep(n):
    count = ""
    i = 1
    while i <= n:
        count += f"{i} sheep..."
        i += 1
    return count


print(count_sheep(4))