import argparse
import logging
from client_validator.csv_io import read_csv, write_csv
from client_validator.validation import validate_row
from client_validator.address_verification import validate_location_postcode
from client_validator.geo import fetch_geo_coordinates


def process_csv(input_path, output_path):
    rows = read_csv(input_path)
    valid_rows = []
    invalid_count = 0
    geo_success_count = 0
    for row in rows:
        errors = validate_row(row)
        errors += validate_location_postcode(row)
        geo = fetch_geo_coordinates(row.get('Residential Address Street'))
        if geo:
            row['latitude'] = geo['latitude']
            row['longitude'] = geo['longitude']
            geo_success_count += 1
        else:
            row['latitude'] = ''
            row['longitude'] = ''
        # Only include rows that are valid AND have coordinates
        if not errors and row['latitude'] and row['longitude']:
            valid_rows.append(row)
        else:
            invalid_count += 1
            logging.info(
                f"Row invalid or missing coordinates: {errors} | Data: {row}")
    print(f"Valid rows: {len(valid_rows)}")
    print(f"Invalid rows: {invalid_count}")
    print(f"Addresses with fetched GEO location: {geo_success_count}")
    if valid_rows:
        fieldnames = list(valid_rows[0].keys())
        write_csv(output_path, valid_rows, fieldnames)
        print(f"Output written to {output_path}")
    else:
        print("No valid rows found.")


def main():
    parser = argparse.ArgumentParser(
        description="Validate and enhance client CSV data.")
    parser.add_argument("input", help="Path to input CSV file")
    parser.add_argument("output", help="Path to output CSV file")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    process_csv(args.input, args.output)


if __name__ == "__main__":
    main()
