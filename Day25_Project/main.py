
# import csv
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#         if row[1] !="temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#========================================================
# import pandas
# data=pandas.read_csv("weather_data.csv")
# data_list=data["temp"].to_list()
# print(data["temp"].max())
# avg=sum(data_list)/len(data_list)
# print(int(avg))
# #=
# print(data["temp"].mean())
#
# #Get Data in Columns
# print(data["day"])
# #Get Data in row
# print(data[data.temp==data["temp"].max()])
#
# monday=data[data.day=="Monday"]
# monday_temp=monday.temp
# monday_tempF=monday_temp *9/5 +32
# print(monday_tempF)
#
# #Create A dataFrame from scratch
# data_dict={
#     "students":["Amy","James","Angela"],
#     "Scores":[76,56,65]
# }
# data4=pandas.DataFrame(data_dict)
# print(data4)
# data.to_csv("data4.csv")

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
black_count = 0
gray_count = 0
red_count = 0
for color in data["Primary Fur Color"]:
    if color == "Black":
        black_count += 1
    elif color == "Gray":
        gray_count += 1
    elif color == "Cinnamon":
        red_count += 1
data_dict={
    "Fur Color ":["Gray","Cinnamon","Black"],
    "Count":[gray_count,red_count,black_count]
}
data1=pandas.DataFrame(data_dict)
data1.to_csv("squirrel_count.csv")