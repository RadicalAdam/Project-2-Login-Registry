import csv
import os

def read_csv(file_path: str) -> list:
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

def write_csv(file_path: str, data: dict) -> None:
    try:
        file_exists = os.path.exists(file_path) and os.path.getsize(file_path) > 0

        with open(file_path, mode='a' if file_exists else 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['username', 'password', 'email', 'name']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()  

            writer.writerow(data)

    except FileNotFoundError:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['username', 'password', 'email', 'name']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(data)

