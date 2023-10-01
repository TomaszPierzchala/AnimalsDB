LOAD DATA INFILE '/Users/tomek/git/AnimalsDB/Hodowla_29.09.23.xlsx-Balbc.csv'
INTO TABLE animals.animals
FIELDS TERMINATED BY ','  -- Separator pól (przecinek w przypadku CSV)
-- ENCLOSED BY '"'          -- Znak otwierający i zamykający pole (jeśli stosowane)
LINES TERMINATED BY '\n' -- Separator linii (nowa linia)
IGNORE 1 LINES; 
