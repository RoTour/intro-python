
# read file temperatures.txt

with open('resources/temperatures.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)