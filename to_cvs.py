import pandas as pd

def excel_to_csv(input_excel, output_csv, sheet_names):
    # Wczytaj plik Excela
    excel_data = pd.read_excel(input_excel, sheet_name=None)

    # Przetwórz wybrane zakładki i zapisz do pliku CSV
    for sheet_name in sheet_names:
        if sheet_name in excel_data:
            sheet_data = excel_data[sheet_name]

            # Tutaj możesz wstawić kod do wykonania, jeśli nazwa zakładki jest 'Nazwa'
            # Na przykład, usuń czwartą kolumnę tylko w tej zakładce
            if sheet_name == 'Balbc' or sheet_name == 'C57Bl6':
                sheet_data = sheet_data.drop(sheet_data.columns[3], axis=1)


            sheet_data.to_csv(f'{output_csv}_{sheet_name}.csv', index=False)
            print(f'Zapisano zakładkę "{sheet_name}" do pliku CSV.')

if __name__ == "__main__":
    # Podaj nazwę pliku Excela, do którego chcesz uzyskać dostęp
    input_excel_file = 'Hodowla.xlsx'

    # Podaj nazwę pliku CSV, do którego chcesz zapisać dane
    output_csv_file = 'Hodowla'

    # Podaj listę nazw zakładek, które chcesz przekonwertować
    selected_sheets = ['Balbc', 'C57Bl6', 'Balbc_porody', 'C57Bl6_porody']

    # Wywołaj funkcję do konwersji
    excel_to_csv(input_excel_file, output_csv_file, selected_sheets)
