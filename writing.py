# # cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
# #
# # with(open("cities.txt", "w")) as city_file:
# #     for city in cities:
# #         print(city, file=city_file)  # stdout pipe
# #
# # cities_empty = []
# #
# # with(open("cities.txt", "r")) as city_file:
# #     for city in city_file:
# #         cities.append(city.strip("\n"))
# #
# # print(cities)
# # for city in cities:
# #     print(city)
#
# with open("binary", "bw") as bin_file:
#     bin_file.write(bytes(range(17)))
#
# with open("binary", "br") as binFile:
#     for b in binFile:
#         print(b)

import pickle
imelda = ("More Mayhem", "Imelda May", "2011", ((1, "Pulling the rug"), (2, "Psycho")))

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)
