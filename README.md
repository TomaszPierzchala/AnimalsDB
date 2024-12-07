## Transfering Excel data to CSV and then to MySql

1. Transfer Excel data to CSV with `to_cvs.py`
    - link newset excel to a `Breeding.xlsx`
    - creates CSV files per each tab of excel file
2. Run LOAD DATA INFILE ... for all CSV files
    - create DataBase `excel` with nessesary tabels (each per excel tab) with `animals.sql`
    - run `$ ./readdata.sh`
