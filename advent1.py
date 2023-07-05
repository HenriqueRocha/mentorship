floor = 0
input = ""
file = open("input.txt", "r")
while True:
    instruction = file.read(1)

    if not instruction:
        break

    if instruction == '(':
        floor += 1
    if instruction == ')':
        floor -= 1

print(floor)
file.close()





