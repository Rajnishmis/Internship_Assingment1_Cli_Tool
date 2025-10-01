# Client Data Validator CLI

Client Data Validator CLI is a command-line tool that helps ensure the accuracy and quality of client data stored in CSV files. It automatically validates essential fields such as names, emails, addresses, and postcodes, checks for consistency between location details, and enriches valid records with geographic coordinates like latitude and longitude. The tool separates clean, usable data from invalid entries by exporting valid rows into a new CSV file and logging problematic records with detailed error messages. By automating data validation and enhancement, it saves time, reduces errors, and ensures that businesses can rely on their client information for analytics, mapping, logistics, or customer communications.

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
## Workflow
CSV Input --> Validation --> Geocoding --> Valid Output CSV
                      

## Requirements

- Python 3.12+
- See `requirements.txt` for dependencies

## Project Structure

- `client_validator/` - Main code modules
- `data/` - Input and output CSV files

## Customization

- Update validation logic in `address_verification.py` for different countries
- Add reference data for postcode-locality-state mapping if needed

