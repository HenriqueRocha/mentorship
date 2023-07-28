#staircase function takes an integer n as input to rep size of stair
#It uses loop to iterate from  1 to n and generates each staircase pattern

def staircase(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)# calculates spaces and numver of #
        stairs = '#' * i   #calculates number of #
        print(spaces + stairs)

# Test the function
size = int(input("Enter the size of the staircase: "))
staircase(size)
