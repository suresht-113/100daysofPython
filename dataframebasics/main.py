# with open("weather_Data.csv") as data:
#     weather = data.readlines()
#
# print(weather)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures =[]
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list= data["temp"].to_list()
# print(temp_list)
# average_temp = data["temp"].mean()
# max_Value = data["temp"].max()

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_farh = monday_temp * 9/5 + 32

# create a dataframe from scratch
# data_dict ={
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data2 = pandas.DataFrame(data_dict)
# data2.to_csv("new_data.csv")
# print(data2)

# finding count of squirrel in the dataset using value counts
# dataset https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/explore/query/SELECT%0A%20%20%60x%60%2C%0A%20%20%60y%60%2C%0A%20%20%60unique_squirrel_id%60%2C%0A%20%20%60hectare%60%2C%0A%20%20%60shift%60%2C%0A%20%20%60date%60%2C%0A%20%20%60hectare_squirrel_number%60%2C%0A%20%20%60age%60%2C%0A%20%20%60primary_fur_color%60%2C%0A%20%20%60highlight_fur_color%60%2C%0A%20%20%60combination_of_primary_and%60%2C%0A%20%20%60color_notes%60%2C%0A%20%20%60location%60%2C%0A%20%20%60above_ground_sighter%60%2C%0A%20%20%60specific_location%60%2C%0A%20%20%60running%60%2C%0A%20%20%60chasing%60%2C%0A%20%20%60climbing%60%2C%0A%20%20%60eating%60%2C%0A%20%20%60foraging%60%2C%0A%20%20%60other_activities%60%2C%0A%20%20%60kuks%60%2C%0A%20%20%60quaas%60%2C%0A%20%20%60moans%60%2C%0A%20%20%60tail_flags%60%2C%0A%20%20%60tail_twitches%60%2C%0A%20%20%60approaches%60%2C%0A%20%20%60indifferent%60%2C%0A%20%20%60runs_from%60%2C%0A%20%20%60other_interactions%60%2C%0A%20%20%60geocoded_column%60%2C%0A%20%20%60%3A%40computed_region_efsh_h5xi%60%2C%0A%20%20%60%3A%40computed_region_f5dn_yrer%60%2C%0A%20%20%60%3A%40computed_region_yeji_bk3q%60%2C%0A%20%20%60%3A%40computed_region_92fq_4b7q%60%2C%0A%20%20%60%3A%40computed_region_sbqj_enih%60/page/filter
# data = pandas.read_csv("squirrel_count.csv")
# fur_color = data["Primary Fur Color"].value_counts()
# data2 = pandas.DataFrame(fur_color)
# data2.to_csv("count.csv")

# alternate method
data = pandas.read_csv("squirrel_count.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict ={
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("count.csv")