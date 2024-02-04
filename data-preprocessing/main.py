from read_data import *
from utils import *

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

def write_data_to_file(data, output_file = 'output.csv'):
    with open(output_file, 'w') as file:
        for row in data:
            line = ','.join(map(str, row))
            file.write(line + '\n')

def dictionary_read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read all lines and store them in a list
            data = []
            lines = file.readlines()

            keys = lines[0].strip().split(',')
            for line in lines[1:]:
                values = line.strip().split(',')
                record = {
                    keys[j]: float(values[j]) if values[j].isdecimal() else values[j]
                    for j in range(len(keys))
                }
                data.append(record)

            return data
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def dictionary_calculate_mean_for_entry(data, entry):
    values = [sample[entry] for sample in data]
    mean_value = sum(values) / len(values)
    return mean_value

if __name__ == '__main__':
    data = read_file('/Users/becir/Downloads/top50header.csv')
    processed_data = replace_null_values(data, 4, calculate_mean_for_index(data, 4))
    write_data_to_file(processed_data)
    data_p = min_max_feature_scaling(data, 4)
    print(data_p)
    #preprocessed = replace_null_values(data)