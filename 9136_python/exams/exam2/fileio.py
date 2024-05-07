
'''COMMON TYPES OF MODES'''
#r,w,x,a,b,t,+
#r - read
#w - open and truncate
#+ - appended after mode to allow read & write
'''COMMON METHODS'''
# file.readline() - reads one line at a time
# for line in file: - allows a looping readline()
# file.readlines() - returns a list of all lines in file


def read_csv_to_dict(filename):
    data_dict = {}

    with open(filename, 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        
        for header in headers:
            data_dict[header] = []

        for line in lines[1:]:
            values = line.strip().split(',')
            for i, value in enumerate(values):
                data_dict[headers[i]].append(value)

    return data_dict

# Example usage:
filename = 'data.csv'  # Change this to the path of your CSV file
data_dict = read_csv_to_dict(filename)

# Print the dictionary
for key, value in data_dict.items():
    print(key, ':', value)