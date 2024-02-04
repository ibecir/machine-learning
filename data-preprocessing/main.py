from read_data import *
from utils import *
from pathlib import Path

def calculate_mean_for_index(data, index):
    values = [sample[index] for sample in data if is_number(sample[index])]
    mean_value = sum(values) / len(values)
    return round(mean_value, 2)

def get_min_max_value(data, index):
    values = [sample[index] for sample in data if is_number(sample[index])]
    return min(values), max(values)

def replace_null_values(data, index, replace_value = 0):
    for entry in data:
        if isinstance(entry[index], str):
            entry[index] = replace_value

    return data

def min_max_feature_scaling(data, index):
    values = [sample[index] for sample in data]
    min, max = get_min_max_value(data, index)
    scaled_column = [(x - min) / (max - min) for x in values]

    for i, sample in enumerate(data):
        sample[index] = scaled_column[i]

    return data

def write_data_to_file(data, output_file = './output/output.csv'):
    with open(output_file, 'w') as file:
        for row in data:
            line = ','.join(map(str, row))
            file.write(line + '\n')

if __name__ == '__main__':
    path = str(Path(__file__).parent.absolute())
    data = read_file(path + '/files/top50header.csv')
    processed_data = replace_null_values(data, 4, calculate_mean_for_index(data, 4))
    write_data_to_file(processed_data, path + '/output/output.csv')
    data_p = min_max_feature_scaling(data, 4)
    print(data_p)
    #preprocessed = replace_null_values(data)