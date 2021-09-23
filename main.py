import pandas
import numpy as np

from finance_scraper import FundScraper

PERSON_OUTPUT_COLUMNS = ['שם', 'קופה', 'אפיק', 'מסלול']

def process_clients(clients):
    results = {}
    output = None
    for i in range(clients.shape[0]):
        name, typee, course, fund_name = clients.iloc[i]
        fund = FundScraper(typee, course, fund_name)
        client_df = pandas.DataFrame([[name, typee, course, fund_name]], columns=PERSON_OUTPUT_COLUMNS)
        print(f'Scraping for {fund.typee[::-1]} | {fund.course[::-1]} | {fund.name[::-1]}')

        if fund in results:
            roi_df = results[fund]
        else:
            roi_df = fund.get_roi_data()
            results[fund] = roi_df

        full_user_output = pandas.concat([client_df, roi_df], axis=1)

        if type(output) == type(None):
            output = full_user_output
        else:
            output = output.append(full_user_output)
    
    output.index = [i for i in range(len(output.index))]
    return output

def write_output_to_excel(output, output_excel_name):
    # print(f'Final Table:')
    # print(output)
    with pandas.ExcelWriter(output_excel_name) as excel_writer:
        output.to_excel(excel_writer)

def main():
    clients_dataframe = pandas.read_excel('Clients.xlsx')
    output = process_clients(clients_dataframe)
    write_output_to_excel(output, "Client_results.xlsx")


if __name__ == "__main__":
    main()
