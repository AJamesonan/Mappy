from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

import os


db=os.environ.get('DATABASE')
create_users_table = """CREATE TABLE IF NOT EXISTS `users` (
`id` bigint NOT NULL AUTO_INCREMENT,
`created_at` datetime DEFAULT CURRENT_TIMESTAMP,
`email` varchar(255) DEFAULT NULL,
`password` varchar(128) DEFAULT NULL,
`updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
`user_name` varchar(30) DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""
connectToMySQL(db).query_db(create_users_table)
create_places_table = """CREATE TABLE IF NOT EXISTS `places` (
`id` bigint NOT NULL AUTO_INCREMENT,
`city` varchar(30) DEFAULT NULL,
`coordinates` float DEFAULT NULL,
`created_at` datetime(6) DEFAULT NULL,
`name` varchar(30) DEFAULT NULL,
`place_id` varchar(255) DEFAULT NULL,
`state` varchar(255) DEFAULT NULL,
`street_address` varchar(30) DEFAULT NULL,
`updated_at` datetime(6) DEFAULT NULL,
`zip` bigint DEFAULT NULL,
`user_id` bigint DEFAULT NULL,
PRIMARY KEY (`id`),
KEY `FKqmg0l98kpihrma9jr4hx0x22b` (`user_id`),
CONSTRAINT `FKqmg0l98kpihrma9jr4hx0x22b` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""
connectToMySQL(db).query_db(create_places_table)

