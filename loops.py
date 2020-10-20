
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# print(names[5])
# print(names[6])

# names = ["alex", "allistar","andrew" ,"angelo" ,"elijah" ,"goerge", "jonathan"]
# for person in names: 
#     print(person)

# rng = list(range(6))
# print(rng)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
for num in lst:
    print(num*2)
print(lst)

list_length = len(lst)
for index in range(len(lst)):
    lst[index] = 2 * lst[index]
    print(lst[index])

print(lst)