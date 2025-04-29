CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

INSERT INTO users (username, password) VALUES ('john', 'password123');
INSERT INTO users (username, password) VALUES ('sandeep', 'sunny123');

SELECT * FROM users;