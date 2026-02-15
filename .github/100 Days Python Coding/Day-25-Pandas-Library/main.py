import pandas as pd
# from pandas.core.interchange.dataframe_protocol import DataFrame
#
# data = pd.read_csv("weather_data.csv")
# data_dic = data.to_dict()
# # print(data_dic)
# data_list = data["temp"].to_list()
# # print(data["temp"].mean())
# # print(data["temp"].max())
#
# # Get data in a row
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
#
# # monday = data[data.day == "Monday"]
# # print(type(monday.temp))
# # monday_temp_fanh = (monday.temp * 1.8) + 32
# # print(monday_temp_fanh)
#
# # Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "Cuppy", "Sharone"],
#     "scores": [73, 89, 80]
# }
# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")


squirrel_data = pd.read_csv("2018_Squirrel_Data_.csv")
# print(squirrel_data["Primary Fur Color"])
primary_fur = (squirrel_data["Primary Fur Color"].value_counts())
print(primary_fur)
primary_fur.to_csv("squirrel_count.csv")


