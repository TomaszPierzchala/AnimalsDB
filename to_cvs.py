import pandas as pd
import csv

def excel_to_csv(input_excel, output_csv, sheet_names):
    TYPE = ['Balbc', 'C57Bl6']
    HODOWLA = 1

    HEADER = HODOWLA if all(item in sheet_names for item in TYPE) else 0
    print(f'HEADER {HEADER}, sheet names: {sheet_names}')
    # Wczytaj plik Excela
    excel_data = pd.read_excel(input_excel, sheet_name=sheet_names, header=HEADER)
    # Stwórz pustą ramkę danych, do której dodasz dane z różnych zakładek
    combined_data = pd.DataFrame()

    # Usuń dwa pierwsze wiersze
    #non_empty_rows = non_empty_rows.iloc[1:]
    

    for sheet_name, sheet_data in excel_data.items():
        # Odfiltruj wiersze, które są całkowicie puste
        non_empty_rows = sheet_data.dropna(how='all')
        # if sheet_name in TYPE:
        data = non_empty_rows.copy()
        if HEADER == HODOWLA:
            data = data.drop(data.columns[3], axis=1)

                   
        for type in TYPE:
            if type in sheet_name:
                if type == sheet_name:
                    # animal table
                    column_name = 'an_strain'
                    # remove rows without an_id
                    data = data[data['an_id'].notna()]
                    # set an_id to an integer
                    data['an_id'] = data['an_id'].astype('int')
                else:
                    column_name = 'cb_strain'
                data[ column_name] = type

                
        combined_data = pd.concat([combined_data, data], ignore_index=True)
    
    combined_data.replace('?', '\\N', inplace=True)
    # Zapisz do jednego pliku CSV
    combined_data.to_csv(output_csv, index=False,  na_rep=r'\N')
    print(f'Zapisano dane do pliku {output_csv}.')

if __name__ == "__main__":
    # Podaj nazwę pliku Excela, do którego chcesz uzyskać dostęp
    input_excel_file = 'Hodowla.xlsx'

    # Wywołaj funkcję do konwersji
    excel_to_csv(input_excel_file, 'Hodowla.csv', ['Balbc', 'C57Bl6'])

    excel_to_csv(input_excel_file, 'Hodowla_porody.csv', ['Balbc_porody', 'C57Bl6_porody'])
