def getData(input_file):
    try:
        with open(input_file, "r") as file:
            data = file.read().splitlines()
        return data
              
    except FileNotFoundError:
        print("Error: File not found.")

def findFirstDigit(line):
    index = 0
    highest_val = (0, 0)
    stored_index = 0

    for x in line[:-1]:
        num = int(x)

        if num > highest_val[0]:
            highest_val = (num, index)
            stored_index += 1
            index += 1

        else:
            stored_index += 1
            index += 1
             
    return highest_val

def findSecondDigit(line, val):
    index = val[1] + 1
    second_val = (0, 0)
    stored_index = val[1] + 1

    for x in line[stored_index:]:
        num = int(x)

        if num > second_val[0]:
            second_val = (num, index)
            stored_index += 1
            index += 1

        else:
            stored_index += 1
            index += 1
             
    return second_val

joltages = []
joltage_sum = 0
data = getData("input.txt")
for i in range(len(data)):
    first_val = findFirstDigit(data[i])
    second_val = findSecondDigit(data[i], first_val)
    joltages.append(int(str(first_val[0]) + str(second_val[0])))

for i in range(len(joltages)):
    joltage_sum += joltages[i]
print(joltage_sum)
