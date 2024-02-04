from utils import *

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read all lines and store them in a list
            data = []
            lines = file.readlines()

            keys = lines[0].split(',');
            for i in range(1, len(lines)):
                data.append(
                    [
                        float(lines[i].split(',')[j].strip('\n')) if is_number(lines[i].split(',')[j].strip('\n')) else lines[i].split(',')[j].strip('\n')
                        for j in range(len(keys))
                    ]
                )
            return data
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")