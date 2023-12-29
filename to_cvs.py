import pandas as pd
import csv


def to_date(df):
    DATE_COLUMNS = ['mating date', 'plug date', 'pregnancy', 'parturition', 'weaning']
    for col in DATE_COLUMNS:
        # Konwertuj kolumnę dat do typu datetime
        df[col] = pd.to_datetime(df[col], errors='coerce')

        # Uzyskaj tylko datę (bez godzin i minut)
        df[col] = df[col].dt.date


def excel_to_csv(input_excel, output_csv, _sheet_name):
    MICE = ['Balbc', 'C57Bl6']
    MATCHING = ['Balbc_porody', 'C57Bl6_porody']
    HODOWLA = 1

    HEADER = HODOWLA if _sheet_name in MICE else 0
    print(f'HEADER {HEADER}, sheet names: {_sheet_name}')

    # Wczytaj plik Excela
    excel_data = pd.read_excel(input_excel, sheet_name=_sheet_name, header=HEADER)
    # Stwórz pustą ramkę danych, do której dodasz dane z różnych zakładek
    data = excel_data.copy()

    # Usuń dwa pierwsze wiersze
    #non_empty_rows = non_empty_rows.iloc[1:]
    
    # Odfiltruj wiersze, które są całkowicie puste
    data = data.dropna(how='all')
                
    if _sheet_name in MICE:
        # remove rows without an_id
        data = data[data['an_id'].notna()]
        # set an_id to an integer
        data['an_id'] = data['an_id'].astype('int')
        # trunccate white space
        data['an_sex'] = data['an_sex'].str.strip()
        
    elif _sheet_name in MATCHING:
        to_date(data)

    data.replace('?', '\\N', inplace=True)
    # Zapisz do jednego pliku CSV
    data.to_csv(output_csv, index=False,  na_rep=r'\N')
    print(f'Zapisano dane do pliku {output_csv}.')

if __name__ == "__main__":
    # Podaj nazwę pliku Excela, do którego chcesz uzyskać dostęp
    input_excel_file = 'Hodowla.xlsx'

    # Wywołaj funkcję do konwersji
    excel_to_csv(input_excel_file, 'Balbc.csv', 'Balbc')
    excel_to_csv(input_excel_file, 'C57Bl6.csv', 'C57Bl6')

    excel_to_csv(input_excel_file, 'Balbc_porody.csv', 'Balbc_porody')
    excel_to_csv(input_excel_file, 'C57Bl6_porody.csv', 'C57Bl6_porody')
