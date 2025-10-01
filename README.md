# Client Data Validator CLI

This tool validates and enhances client data from a CSV file, including address validation and GEO coordinate fetching.

## Features

- Validates client fields (name, email, address, postcode, etc.)
- Checks address and postcode logic
- Fetches latitude/longitude for valid addresses
- Outputs only valid rows with coordinates
- Logs invalid rows and errors

## Usage

### Command Line

Run from the CLI with input and output file paths:

```
python main.py <input_csv_path> <output_csv_path>
```

Or as a module:

```
python -m client_validator.main <input_csv_path> <output_csv_path>
```

### Example

```
python main.py data/input.csv data/output.csv
```

## Requirements

- Python 3.12+
- See `requirements.txt` for dependencies

## Project Structure

- `client_validator/` - Main code modules
- `data/` - Input and output CSV files

## Customization

- Update validation logic in `address_verification.py` for different countries
- Add reference data for postcode-locality-state mapping if needed

