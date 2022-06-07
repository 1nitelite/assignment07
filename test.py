"""
# Title: test.py
# Desc: for testing certain python commands
# Change Log: (Who, When, What)
# NToulas, 2022-Jun-05, Created File
"""

# data = []
# with open('mathIn.txt', 'r') as file:
#     for line in file:
#         data.append(line)
#     # info = file.read()
#     # data = file.readlines()
#
# # print(info)
# # print(type(info))
# print(data)
import pickle

with open('numbers.dat', 'rb') as file:
    numbers = pickle.load(file)
print(numbers)

with open('results.dat', 'rb') as file:
    results = pickle.load(file)
print(results)