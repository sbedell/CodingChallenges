'''
CodeKata - "Elevator Maintenance" aka semver sorting

Should Take an input like this: 1.1.2 1.0 1.3.3 1.0.12 1.0.2
And output it sorted like this: [1.0, 1.0.2, 1.0.12, 1.1.2, 1.3.3]

Sample Input 2: 1.11 2.0.0 1.2 2 0.1 1.2.1 1.1.1 2.0
Sample Output 2: [0.1, 1.1.1, 1.2, 1.2.1, 1.11, 2, 2.0, 2.0.0]
'''

# Stub Code from HackerRank:
versions = input().strip().split(' ')

# Your code goes here
versions.sort(key=lambda s: [int(u) for u in s.split('.')])

# String manipulation to get the final answer:
answer = '['
for i in versions:
    answer += (i + ', ')

answer = answer[0: -2] #strip off the last comma and space
answer += ']'
    
print(answer)