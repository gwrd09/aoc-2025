import re

def splitID(input_file):
    id_list = []
    try:
            with open(input_file, "r") as file:
                contents = file.read()
                id_list = contents.split(",")
            return id_list
    except FileNotFoundError:
        print("Error: File not found.")

def searchRange(range_input):
    ranges = range_input.split("-")
    invalid_id_list = []
     
    for i in range(int(ranges[0]), int(ranges[1]) + 1):
        pattern = re.compile(r"^(\d+)\1$")
        if pattern.search(str(i)):
            invalid_id_list.append(i)

    return invalid_id_list

def addInvalidID(invalids):
    invalid_sum = 0
    for item in invalids:
        invalid_sum += item
    return invalid_sum

id_list = splitID("input.txt")
invalid_id_list = []
for i in range(len(id_list)):
    for x in searchRange(id_list[i]):
        invalid_id_list.append(x)
print(addInvalidID(invalid_id_list))