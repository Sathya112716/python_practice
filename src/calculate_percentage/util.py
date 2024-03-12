import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def cal_percent(input):
    element_count = {}
    for element in input:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    # Calculate percentages
    total= len(input)
    percent_dict = {}
    for key, value in element_count.items():
        percent_dict[key] = (value / total) * 100

    return percent_dict

