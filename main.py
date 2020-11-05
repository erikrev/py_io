# jabber = open("sample.txt", "r")
#
# for line in jabber:
#     if "dolor" in line.lower():
#         print(line, end=" ")
#
# jabber.close()

# with open("sample.txt", "r") as jabber:
#     for line in jabber:
#         if "dolor" in line.lower():
#             print(line, end=" ")

# with open("sample.txt", "r") as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end="")
#         line = jabber.readline()

f = open("C:\\Users\\erik\\Desktop\\[FreeCourseSite.com] Udemy - Learn Python Programming Masterclass\\"
         "10. Input and Output (IO) in Python\\2.1 sample.txt.txt", "r")
for line in f:
    print(line)
