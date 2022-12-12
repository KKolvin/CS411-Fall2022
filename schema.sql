USE convenient_recipes;

CREATE TABLE Users (
    user_id int4  AUTO_INCREMENT,
    username varchar(255),
    email varchar(255) UNIQUE,
    password varchar(255),
  CONSTRAINT users_pk PRIMARY KEY (user_id)
);

CREATE TABLE User_Post_Recipe
(
  uid int4,
  recipe_id int4  AUTO_INCREMENT,
  recipe_name VARCHAR(255),
  likes int4,
  PRIMARY KEY (recipe_id),
  FOREIGN KEY (uid) REFERENCES Users(user_id)
);