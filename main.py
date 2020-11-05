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

with open("sample.txt", "r") as jabber:
     line = jabber.readline()
     while line:
         print(line, end="")
         line = jabber.readline()
