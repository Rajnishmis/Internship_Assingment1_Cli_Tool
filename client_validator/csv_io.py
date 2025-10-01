# Handles reading and writing CSV files
import csv

# Reading CSV Files


def read_csv(input_path):
    with open(input_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def write_csv(output_path, rows, fieldnames):
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
