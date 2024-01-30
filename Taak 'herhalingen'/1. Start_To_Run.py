x = int(input())
y = int(input())
D = 1

while x <= y: # while we havent trained enough
    x += x * .1 # take 10 percent of x and add it to itself
    D += 1  # add a day of training

print(D)
