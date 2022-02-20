import os
import csv
# import random

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

def read_csv(csv_path):
    people = []
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                people.append(Person(row[0], row[1], row[2]))
            line_count += 1
    return people

def message_all(people):
    for person in people:
        send_message(person.number, person.message)

def make_message(people):
    for person in people:
        person.message = person.first_name.lower() + "!! " + read_file('sample.txt')
    
def send_message(phone_number, message):
    os.system('osascript send.applescript {} "{}"'.format(phone_number, message))

people = read_csv('sample.csv')
make_message(people)
message_all(people)