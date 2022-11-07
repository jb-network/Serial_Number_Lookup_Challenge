from pathlib import Path
from datetime import date
import re
import os
import time
import math

menu_boundary = "-" * 52
inner_menu = "-" * 4 + "\t" * 2 + "-" * 10
today_date = date.today().strftime("%d/%m/%y")
serial_number_pattern = r'N+[a-zA-Z]{3}\-\d{5}'
serial_number_locator = {}

def search_file(full_file_path, serial_number_pattern):
    current_file = open(full_file_path, 'r')
    file_text = current_file.read()
    if re.search(serial_number_pattern, file_text):
        return re.search(serial_number_pattern, file_text).group(0)
    else:
        return "Not Found"

def get_pattern():
    for root, dirs, files in os.walk("."):
        for target in files:
            search_result = search_file(Path(root, target), serial_number_pattern)
            if search_result != "Not Found":
                serial_number_locator[target] = search_result
    return None

def serial_number_parser(serial_number_locator):
    for file_name, serial_number in serial_number_locator.items():
        print(f"{file_name}\t{serial_number}")
        total_items = len(serial_number_locator)
    return total_items

print(menu_boundary)
print(f"Search date: {today_date}")
print("\nFILE		SERIAL NO.")
print(inner_menu)
start_time = time.time()
get_pattern()
total_items = serial_number_parser(serial_number_locator)
print(f"\nNumbers found: {total_items}")
end_time = time.time()
print(f"Search duration: {math.ceil(end_time - start_time)} seconds")
print(menu_boundary)
