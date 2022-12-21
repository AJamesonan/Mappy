INSERT INTO dojos (id,name,created_at,updated_at)
VALUES (1,'Mr. Myagis',NOW(), NOW());
INSERT INTO dojos (id,name,created_at,updated_at)
VALUES (2,'Jungle Gyms',NOW(), NOW());
INSERT INTO dojos (id,name,created_at,updated_at)
VALUES (3,'Dodo Dojo',NOW(), NOW());
DELETE FROM dojos WHERE id =1;
DELETE FROM dojos WHERE id =2;
DELETE FROM dojos WHERE id =3;
INSERT INTO dojos (id,name,created_at,updated_at)
VALUES (1,'Mr. Myagis',NOW(), NOW());
INSERT INTO dojos (id,name,created_at,updated_at)
VALUES (2,'Jungle Gyms',NOW(), NOW());
INSERT INTO dojos (id,name,created_at,updated_at)
VALUES (3,'Dodo Dojo',NOW(), NOW());

INSERT INTO ninjas (id,first_name,last_name,age,created_at,updated_at,dojo_id)
VALUES (1,'Hank', 'Hill', 43, NOW(), NOW(),2);
INSERT INTO ninjas (id,first_name,last_name,age,created_at,updated_at,dojo_id)
VALUES (2,'Hanq', 'Hill', 42, NOW(), NOW(),2);
INSERT INTO ninjas (id,first_name,last_name,age,created_at,updated_at,dojo_id)
VALUES (3,'Hank', 'Trill', 40, NOW(), NOW(),2);

INSERT INTO ninjas (id,first_name,last_name,age,created_at,updated_at,dojo_id)
VALUES (1,'Hank', 'Hill', 43, NOW(), NOW(),2);
INSERT INTO ninjas (id,first_name,last_name,age,created_at,updated_at,dojo_id)
VALUES (1,'Hank', 'Hill', 43, NOW(), NOW(),2);
INSERT INTO ninjas (id,first_name,last_name,age,created_at,updated_at,dojo_id)
VALUES (1,'Hank', 'Hill', 43, NOW(), NOW(),2);