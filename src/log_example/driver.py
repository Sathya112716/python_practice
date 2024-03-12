from util import cal_percent

my_list = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9, 9]
percentages = cal_percent(my_list)

for key, value in percentages.items():
    print(f"{key}: {value}%")
