# MyGemelScraping

## Overview

The MyGemelScraping repository is a web scraper designed for the MyGemel website. It provides vital comprising information for a financial manager by extracting data related to clients' investment funds. The code utilizes the `finance_scraper` library for efficient scraping.

## Functionality

The main code includes functions to process client information and retrieve Return on Investment (ROI) data for their respective investment funds.

### Process Client

The `process_client` function takes client details (name, type, course, fund name) and returns a DataFrame containing information about the client and their fund's ROI data.

### Process Clients

The `process_clients` function iterates through a DataFrame of clients, processes each client using the `process_client` function, and aggregates the results into a comprehensive DataFrame.

### Write Output to Excel

The `write_output_to_excel` function saves the aggregated client data, including ROI information, to an Excel file.

### Main Function

The `main` function reads client data from an input Excel file, processes the clients, and writes the results to an output Excel file.

## Usage

To use the MyGemelScraping tool, follow these steps:

1. **Prepare Input Excel File:**
   - Create an Excel file with client details (Columns: 'שם', 'קופה', 'אפיק', 'מסלול').

2. **Run the Script:**
   - Execute the script `MyGemelScraping.py` using a Python interpreter.

3. **Input File Prompt:**
   - The script will prompt you to drag and drop the input Excel file or use the default file 'Clients.xlsx'.

4. **Scraping Process:**
   - The script will begin scraping data from the MyGemel website for each client.

5. **Output Excel File:**
   - The aggregated results, including ROI data, will be saved in an output Excel file named 'Client_results.xlsx'.

## Dependencies

- Python 3.x
- pandas
- numpy
- finance_scraper

## Setup Instructions

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt` (if applicable).
3. Run the main script `MyGemelScraping.py` using a Python interpreter.

## Notes

- Ensure that the input Excel file ('Clients.xlsx' by default) is formatted correctly.
- Handle any runtime errors or client-specific issues during scraping.
