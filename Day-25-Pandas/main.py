# with open(file="weather_data.csv", mode="r") as f:
#     data = f.readlines()
#
# print(data)

# import csv
#
# with open(file="weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for idx, row in enumerate(data):
#         if idx > 0:
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
import pandas

# print(type(data_frame))
# print(data_frame)
# print(type(data_frame["temp"]))
# print(data_frame.describe())

# data_dict = data_frame.to_dict()
# print(data_dict)
#
# temp_list = data_frame["temp"].to_list()
# print(temp_list)

# avg_temp = round(sum(temp_list) / len(temp_list), 2)
# print(avg_temp)

# avg_temp = data_frame["temp"].mean()
# print(avg_temp)
#
# max_temp = data_frame["temp"].max()
# print(max_temp)
#
# print(data_frame["condition"])
# print(data_frame.condition)

# print(data_frame[data_frame.temp == data_frame.temp.max()])
#
# monday = data_frame[data_frame.day == "Monday"]
# celcius_to_fahrenheit = lambda x: (9/5) * x + 32
# print(celcius_to_fahrenheit(monday.temp))

# data_dict = {
#     "Students": ["Mateusz", "Ola", "Paweł"],
#     "Scores": [80, 68, 89]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("./new_data.csv")
import pandas as pd

data_frame_squirell = pd.read_csv(filepath_or_buffer="2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data_series_fur_color = data_frame_squirell["Primary Fur Color"]
# print(data_series_fur_color.unique())
fur_color_1_series = data_frame_squirell[data_frame_squirell["Primary Fur Color"] == "Cinnamon"]
fur_color_2_series = data_frame_squirell[data_frame_squirell["Primary Fur Color"] == "Gray"]
fur_color_3_seriec = data_frame_squirell[data_frame_squirell["Primary Fur Color"] == "Black"]

num_cinnamon = fur_color_1_series["Primary Fur Color"].count()
num_gray = fur_color_2_series["Primary Fur Color"].count()
num_black = fur_color_3_seriec["Primary Fur Color"].count()

output_dict = {"Fur Color": ["Cinnamon", "Gray", "Black"],
               "Count": [num_cinnamon, num_gray, num_black]}

output_df = pd.DataFrame(output_dict)
output_df.to_csv("squirell_fur_count.csv", header=True)
