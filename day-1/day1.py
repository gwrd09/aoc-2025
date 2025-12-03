def findPassword(input_file):
    dial_num = 50
    count = 0
    try:
        with open(input_file, "r") as file:
            for line in file:
                dial_num, count = assess(line, dial_num, count)
            print(dial_num, count, line)
    except FileNotFoundError:
        print("Error: File not found.")

def assess(textLine, dial_num, count):
    num = int(textLine[1:])

    if textLine[0] == "L":
        
        for _ in range(num):
            dial_num -= 1
            if dial_num % 100 == 0:
                count += 1

        dial_num = dial_num % 100
                
    elif textLine[0] == "R":
        
        for _ in range(num):
            dial_num += 1
            if dial_num % 100 == 0:
                count += 1

        dial_num = dial_num % 100

    else:
        print("Error: Invalid line format.")
    return dial_num, count
    
findPassword("input.txt")