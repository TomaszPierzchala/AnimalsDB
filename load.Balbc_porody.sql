SELECT COUNT(*) FROM excel.Balbc_porody;
TRUNCATE TABLE excel.Balbc_porody;

LOAD DATA INFILE '/Users/tomek/git/AnimalsDB/Balbc_porody.csv'
INTO TABLE excel.Balbc_porody
FIELDS TERMINATED BY ','  -- Separator pól (przecinek w przypadku CSV)
ENCLOSED BY '"'          -- Znak otwierający i zamykający pole (jeśli stosowane)
LINES TERMINATED BY '\n' -- Separator linii (nowa linia)
IGNORE 1 LINES
(female,mating_nr,mating_date,male,plug_date,pregnancy,parturition,nr_of_birth_pups,weaning,nr_of_F,nr_of_M,sum_of_pups,comments);

