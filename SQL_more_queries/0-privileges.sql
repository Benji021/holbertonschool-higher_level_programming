-- List all privileges of the MYSQL users
SELECT User, Host FROM mysql.user WHERE User IN ('user_0d_1', 'user_0d_2');
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'password1';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'password2';
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';