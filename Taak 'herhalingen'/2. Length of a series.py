# l = []
# while 0 not in l:
#     l.append(int(input()))
    
# print(len(l) - 1)

'''
===========================
======= No list way =======
===========================
'''

x = 1 # initialize x
length = -1 # set length to -1 because the 0 at the end will also be counted

while x != 0: # while the input isnt zero
    x = int(input()) # ask for an input
    length += 1 # make length 1 more

print(length) 
