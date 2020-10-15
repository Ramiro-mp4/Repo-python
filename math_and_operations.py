# num_given = int(input("give a number "))

# if(num_given % 2 == 0) :
#     print("even")
# else:
#     print("odd")

# str1 = "hello"
# str2 = "world!"
# str3 = " "
# print(str1 + str3 + str2)

# x = 5
# x += 2
# print(x)

# multi_string = """
# Hello 
# I
# am
# a 
# multi
# string
# line
# """
# print(multi_string)


# if (5 > 7):
#     print ("hello")
# else:
#     print("goodbye")


# expression = "hello" if 6 >=6 else "goodbye"
# print (expression)


# sale = True

# store_message = "hello. we have a sale today!" if sale else "we dont have a sale today"

# print(store_message)


# if((not 2**3 == 8) or (4**2 == 8)):
#     print("true")
# else:
#     print ("false")
try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a/b)
except ZeroDivisionError:
    print("b was equal to zero, computers can't divide by zero!")
    b = int(input("b: "))
    print(a/b)