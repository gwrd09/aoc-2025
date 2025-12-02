def findPassword(input_file):
    dial_num = 50
    count = 0
    try:
        with open(input_file, "r") as file:
            for line in file:
                print(dial_num, count, line)
                dial_num, count = assess(line, dial_num, count)
    except FileNotFoundError:
        print("Error: File not found.")

def assess(textLine, dial_num, count):
    num = textLine[1:]
    if textLine[0] == "L":
        dial_num = (dial_num - int(num)) % 100
    elif textLine[0] == "R":
        dial_num = (dial_num + int(num)) % 100
    else:
        print("Error: Invalid line format.")
    if dial_num == 0:
        count += 1
    return dial_num, count
    

findPassword("input.txt")