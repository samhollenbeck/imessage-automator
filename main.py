import os
import csv

class Person:
  def __init__(self, first_name, last_name, number):
    self.first_name = first_name
    self.last_name = last_name
    self.number = number

def read_file(file_path):
    text = ""
    with open(file_path, 'r') as f:
        lines = f.readlines()
   
    for i in range(len(lines)):
        if i == len(lines) - 1:
            text += lines[i]
        else:
            text += lines[i] + "\n"
    return text

# def read_csv(csv_path):
#     with open(csv_path) as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         line_count = 0
#         for row in csv_reader:
#             if line_count == 0:
#                 print(f'Column names are {", ".join(row)}')
#                 line_count += 1
#             else:
#                 print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#                 line_count += 1
#         print(f'Processed {line_count} lines.')

def send_message(phone_number, message):
    os.system('osascript send.applescript {} "{}"'.format(phone_number, message))

people = []

print('lol')
send_message('9794505910', read_file('sample.txt'))
        