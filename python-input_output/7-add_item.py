#!/usr/bin/python3
"""Module containing load_from_json_file"""
import sys
from pathlib import Path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_path = Path("add_item.json")
arguments = sys.argv

"""Checks if the file exist
It creates the file if it doesn't"""
if not file_path.exists():
    save_to_json_file([], "add_item.json")

arg_list = []
for i in range(1, len(arguments)):
    arg_list.append(arguments[i])

""" Reads the data from the JSON file """
current_args = load_from_json_file(file_path)
""" update the whole list appending new data """
output_list = current_args + arg_list
""" Save the new list to the JSON file """
save_to_json_file(output_list, file_path)
