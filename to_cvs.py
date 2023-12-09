import pandas as pd

def excel_to_csv(input_excel, output_csv, sheet_names):
    TYPE = ['Balbc', 'C57Bl6']

    # Wczytaj plik Excela
    excel_data = pd.read_excel(input_excel, sheet_name=sheet_names, header=1)
    # Stwórz pustą ramkę danych, do której dodasz dane z różnych zakładek
    combined_data = pd.DataFrame()

    for sheet_name, sheet_data in excel_data.items():
        if sheet_name in TYPE:
            # Odfiltruj wiersze, które są całkowicie puste
            non_empty_rows = sheet_data.dropna(how='all')
            # Usuń dwa pierwsze wiersze
            #non_empty_rows = non_empty_rows.iloc[1:]

            data = non_empty_rows.drop(non_empty_rows.columns[3], axis=1)
            data["strain"] = sheet_name
            combined_data = pd.concat([combined_data, data], ignore_index=True)
    
        else:
            print(f'Nie robię nic dla zakładki {sheet_name}')

    # Zapisz do jednego pliku CSV
    combined_data.to_csv(output_csv, index=False,  na_rep=r'\N')
    print(f'Zapisano dane do pliku CSV.')

    """    # Przetwórz wybrane zakładki i zapisz do pliku CSV
        for sheet_name in sheet_names:
            if sheet_name in excel_data:
                sheet_data = excel_data[sheet_name]

                # Tutaj możesz wstawić kod do wykonania, jeśli nazwa zakładki jest 'Nazwa'
                # Na przykład, usuń czwartą kolumnę tylko w tej zakładce
                if sheet_name == 'Balbc' or sheet_name == 'C57Bl6':
                    sheet_data = sheet_data.drop(sheet_data.columns[3], axis=1)


                sheet_data.to_csv(f'{output_csv}_{sheet_name}.csv', index=False)
                print(f'Zapisano zakładkę "{sheet_name}" do pliku CSV.')
    """
if __name__ == "__main__":
    # Podaj nazwę pliku Excela, do którego chcesz uzyskać dostęp
    input_excel_file = 'Hodowla.xlsx'

    # Podaj nazwę pliku CSV, do którego chcesz zapisać dane
    output_csv_file = 'Hodowla.csv'

    # Podaj listę nazw zakładek, które chcesz przekonwertować
    selected_sheets = ['Balbc', 'C57Bl6', 'Balbc_porody', 'C57Bl6_porody']

    # Wywołaj funkcję do konwersji
    excel_to_csv(input_excel_file, output_csv_file, selected_sheets)
