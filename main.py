import pandas
import numpy as np

OUTPUT_COLUMNS = ['שם', 'מסלול', 'אפיק', 'תשואה חודשית', 'תשואה 12 חודשים', 'תשואה מצטברת', 'דמי ניהול']

def scrape(course, typee):
    return 1, 2, 3, 4

def process_clients(clients):
    results = {}
    output = []
    for i in range(clients.shape[0]):
        name, course, typee = clients.iloc[i]
        print(f'Scraping for {name[::-1]} | {course[::-1]} | {typee[::-1]}')

        if (course, typee) in results:
            monthly_return, ytd_return, accumulated_return, fees = results[(course, typee)]
        else:
            monthly_return, ytd_return, accumulated_return, fees = scrape(course, typee)
            results[(course, typee)] = monthly_return, ytd_return, accumulated_return, fees

        print(f'Results')
        print(f'monthly_return: {monthly_return}')
        print(f'ytd_return: {ytd_return}')
        print(f'accumulated_return: {accumulated_return}')
        print(f'fees: {fees}')
        print()

        output.append([name, course, typee, monthly_return,\
            ytd_return, accumulated_return, fees])
    return output

def write_output_to_excel(output, output_excel_name):
    output_dataframe = pandas.DataFrame(np.array(output), columns=OUTPUT_COLUMNS)
    print(f'Final Table:')
    print(output_dataframe)
    with pandas.ExcelWriter(output_excel_name) as excel_writer:
        output_dataframe.to_excel(excel_writer)

def main():
    clients_dataframe = pandas.read_excel('Clients.xlsx')
    output = process_clients(clients_dataframe)
    write_output_to_excel(output, "Client_results.xlsx")


if __name__ == "__main__":
    main()
