SELECT CONCAT('DROP TABLE IF EXISTS ', table_name, ';') AS drop_statement
FROM information_schema.tables
WHERE table_schema = 'hbnb_dev_db';