# names = [["jenny", 61], ["alexus", 70], ["sam", 67], ["grace", 64]]

# names = ["jenny", "alexus"]

# print(names[0])
#print(names)
#0, 1, 2, 3, 4 ...

# names_and_heights = [["jenny", 67], ["alexus", 70]]

# print(names_and_heights[0][1])
# print(names_and_heights[0][0] + " is " + str(names_and_heights[0][1]) + " inches tall")

# names = ["jenny", "alexus"] #zip() does not include the items from the longer list if list lengths are not the same
#  heights = [67, 70]

# names_and_heights = list(zip(names, heights))

# tuples: (x, y) and cannot be changed
# list: [x. y]

# print(list(names_and_heights))

# print(names_and_heights[0][0])

names = ["jenny", "alexus"]
print("before adding \"sam\": " + str(names))
names.append("sam")
print("after adding\"sam\": " + str(names))
print("hello world")
# "hello world"

# names.insert(0, "alex")

#range(x)
#start: 0
#stop: x-1
#step: 1
even_range = list(range(0, 21, 2))
print(even_range)

#range(x, y)
#start: x
#stop: y-1
#step: 1

zero_to_five = list(range(0, 6))
print(zero_to_five)