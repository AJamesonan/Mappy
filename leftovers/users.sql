INSERT INTO users (first_name, last_name, email,created_at, updated_at)
VALUES ('Hanq','Trill', 'hanq@propane.org', NOW(),NOW());
INSERT INTO users (first_name, last_name, email,created_at, updated_at)
VALUES ('Pank','Dill', 'hanq@propane.org', NOW(),NOW());
INSERT INTO users (first_name, last_name, email,created_at, updated_at)
VALUES ('Stanq','Vill', 'hanq@propane.org', NOW(),NOW());

DELETE FROM users 
WHERE id = 4; 
DELETE FROM users 
WHERE id = 5; 
DELETE FROM users 
WHERE id = 6; 

UPDATE users SET
last_name = 'Pancakes'
WHERE id =3;

