CREATE DATABASE IF NOT EXISTS convenient_recipes;
USE convenient_recipes;
DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS Favorites CASCADE;

CREATE TABLE Users (
    user_id int4  AUTO_INCREMENT,
    email varchar(255) UNIQUE,
    password varchar(255),
  CONSTRAINT users_pk PRIMARY KEY (user_id)
);

CREATE TABLE Favorites
(
  user_id int4,
  recipe_name VARCHAR(255),
  recipe VARCHAR(500),
  likes 0
  INDEX idx (user_id)
);