import pandas
import numpy as np

from finance_scraper import FundScraper

PERSON_OUTPUT_COLUMNS = ['שם', 'קופה', 'אפיק', 'מסלול']

def process_clients(clients):
    results = {}
    output = None
    print('Begin Scraping...')
    for i in range(clients.shape[0]):
        name, typee, course, fund_name = clients.iloc[i]
        fund = FundScraper(typee, course, fund_name)
        client_df = pandas.DataFrame([[name, typee, course, fund_name]], columns=PERSON_OUTPUT_COLUMNS)

        if fund in results:
            roi_df = results[fund]
        else:
            roi_df = fund.get_roi_data()
            results[fund] = roi_df

        full_user_output = pandas.concat([client_df, roi_df], axis=1)
        output = output.append(full_user_output) if type(output) != type(None) else full_user_output 
    
        print(f'{i+1}/{clients.shape[0]}')

    output.index = [i for i in range(len(output.index))]
    print("Done.")
    return output

def write_output_to_excel(output, output_excel_name):
    with pandas.ExcelWriter(output_excel_name) as excel_writer:
        output.to_excel(excel_writer)

def main():
    input_path = input("Drag input file")
    clients_dataframe = pandas.read_excel(input_path)
    output = process_clients(clients_dataframe)
    write_output_to_excel(output, "Client_results.xlsx")


if __name__ == "__main__":
    main()
