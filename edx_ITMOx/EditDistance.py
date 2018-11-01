def edit_distance(a, b):
    





file = open("input.txt", "r")
a = file.readline()
b = file.readline()
file.close()

ed = edit_distance(a, b)

file = open("output.txt", "w")
file.write(ed)
file.close()
