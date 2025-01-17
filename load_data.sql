LOAD DATA INFILE '/Users/tomek/git/AnimalsDB/Hodowla.csv'
INTO TABLE animals.animals
FIELDS TERMINATED BY ','  -- Separator pól (przecinek w przypadku CSV)
ENCLOSED BY '"'          -- Znak otwierający i zamykający pole (jeśli stosowane)
LINES TERMINATED BY '\n' -- Separator linii (nowa linia)
IGNORE 1 LINES
(an_id,an_sex,an_birth_dt, @ignore ,an_procedure,an_loc,an_rack,an_cage,an_origin,an_mother,an_father,an_death_dt,an_note,an_strain,an_transgenic_line,an_gene,an_genotype);

