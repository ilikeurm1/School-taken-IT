# s = []
# while 0 not in s:
#     s.append(int(input()))

# print(sum(s))

'''
===========================
======= No list way =======
===========================
'''

x = 1 # initialize x
sum = 0 # initialize the sum

while x != 0: # while the input isnt zero
    x = int(input()) # ask for an input
    sum += x # add that input to the sum

print(sum)
