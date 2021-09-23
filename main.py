import pandas
import numpy as np

OUTPUT_COLUMNS = ['שם', 'מסלול', 'אפיק', 'תשואה חודשית', 'תשואה 12 חודשים', 'תשואה מצטברת', 'דמי ניהול']

def scrape(name, course, typee):
    return 1, 2, 3, 4

def main():
    df = pandas.read_excel('Clients.xlsx')
    output_rows = []
    output_df = pandas.DataFrame()

    for i in range(df.shape[0]):
        name, course, typee = df.iloc[i]
        print(f'Scraping for {name[::-1]} | {course[::-1]} | {typee[::-1]}')
        monthly_return, ytd_return, accumulated_return, fees = scrape(name, course, typee)
        print(f'Results')
        print(f'monthly_return: {monthly_return}')
        print(f'ytd_return: {ytd_return}')
        print(f'accumulated_return: {accumulated_return}')
        print(f'fees: {fees}')
        print()
        output_rows.append([name, course, typee, monthly_return,\
            ytd_return, accumulated_return, fees])

    # Saving the current columns with additional scapred info
    output_df = pandas.DataFrame(np.array(output_rows), columns=OUTPUT_COLUMNS)
    print(f'Final Table:')
    print(output_df)

if __name__ == "__main__":
    main()
