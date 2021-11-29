/********************************************************
* This script creates the database named my_music_store 
*********************************************************/

DROP DATABASE IF EXISTS my_music_store;
CREATE DATABASE my_music_store;
USE my_music_store;

-- create the tables for the database
CREATE TABLE customers (
  customer_id        INT            PRIMARY KEY   AUTO_INCREMENT,
  customer_name      VARCHAR(30)   NOT NULL,
  province           VARCHAR(20)   NOT NULL,
  city               VARCHAR(20)   NOT NULL,
  country            VARCHAR(20)   NOT NULL
);

CREATE TABLE artists (
  artist_id        INT            PRIMARY KEY   AUTO_INCREMENT,
  artist_name      VARCHAR(30)   NOT NULL,
  artist_country   VARCHAR(20)   NOT NULL
);

CREATE TABLE genres (
  genre_id        INT            PRIMARY KEY   AUTO_INCREMENT,
  genre_name      VARCHAR(20)   NOT NULL      UNIQUE
);

CREATE TABLE albums (
  album_id        INT            PRIMARY KEY   AUTO_INCREMENT,
  album_name      VARCHAR(30)   NOT NULL,
  album_language  VARCHAR(20)   NOT NULL,
  artist_id       INT            NOT NULL,
  genre_id        INT            NOT NULL,
  number_of_tracks INT           NOT NULL      DEFAULT 0,
  available_copies INT           NOT NULL      DEFAULT 0,
  album_cost_in_$   INT          NOT NULL,
  release_date    DATE                         DEFAULT NULL,
  CONSTRAINT albums_fk_artists
    FOREIGN KEY (artist_id)
    REFERENCES artists (artist_id),
  CONSTRAINT albums_fk_genres
    FOREIGN KEY (genre_id)
    REFERENCES genres (genre_id)
);

CREATE TABLE tracks (
  track_id        INT            PRIMARY KEY   AUTO_INCREMENT,
  track_name      VARCHAR(30)   NOT NULL,
  track_length    VARCHAR(10)   NOT NULL,
  album_id        INT            NOT NULL,
   CONSTRAINT tracks_fk_albums
	FOREIGN KEY (album_id)
    REFERENCES albums (album_id)
);

CREATE TABLE orders (
  order_id        INT            PRIMARY KEY   AUTO_INCREMENT,
  order_date      DATE                         DEFAULT NULL,
  customer_id     INT            NOT NULL,
  order_amount    INT            NOT NULL,
  CONSTRAINT orders_fk_customers
    FOREIGN KEY (customer_id)
    REFERENCES customers (customer_id)
);

CREATE TABLE orders_to_albums (
  order_id        INT            NOT NULL,
  album_id        INT            NOT NULL,
  CONSTRAINT orders_to_albums_fk_orders
    FOREIGN KEY (order_id)
    REFERENCES orders (order_id),
  CONSTRAINT orders_to_albums_fk_albums
    FOREIGN KEY (album_id)
    REFERENCES albums (album_id)
);

-- Insert data into the tables
INSERT INTO genres (genre_id, genre_name) VALUES
(1, 'Rock'),
(2, 'Pop'),
(3, 'Hip-Hop'),
(4, 'Jazz'),
(5, 'Classical'),
(6, 'Country'),
(7, 'Soft-Rock');

INSERT INTO artists (artist_id, artist_name, artist_country) VALUES
(1, 'AR Rahman', 'India'),
(2, 'Avicii', 'Sweden'),
(3, 'Taylor Swift', 'USA'),
(4, 'Justin Bieber', 'Canada'),
(5, 'Papon', 'India'),
(6, 'Drake', 'Canada'),
(7, 'Neha Kakkar', 'India'),
(8, 'Ed Sheeran', 'USA');

INSERT INTO customers (customer_id, customer_name, province, city, country) VALUES
(1, 'Shrey Patel', 'Gujarat', 'Ahmedabad', 'India'),
(2, 'Niah','Ontario', 'Waterloo', 'Canada'),
(3, 'Vrushti Shah', 'Maharashtra', 'Mumbai', 'India'),
(4, 'John','California', 'Las Vegas', 'USA'),
(5, 'Zee','Beijing', 'Beijing', 'China'),
(6, 'Andrew','Arizona', 'Phoenix', 'USA'),
(7, 'Stuart','British Columbia', 'Vancouver', 'Canada'),
(8, 'Mariam','Texas', 'Houston', 'USA'),
(9, 'Jasmin', 'Tamilnadu', 'Chennai', 'India'),
(10, 'Jhinping','Shanghai', 'Shanghai', 'China'),
(11, 'Kuldip', 'Gujarat', 'Ahmedabad', 'India'),
(12, 'Monica', 'Gujarat', 'Surat', 'India'),
(13, 'Krima', 'Gujarat', 'Ahmedabad', 'India'),
(14, 'Shreya', 'Gujarat', 'Surat', 'India'),
(15, 'Manan', 'Nevada', 'Las Vegas', 'USA');

INSERT INTO albums (album_id, album_name, album_language, artist_id, genre_id, number_of_tracks, available_copies, album_cost_in_$, release_date) VALUES
(1, 'Divide', 'English', 8, 02, 3, 10, 20, '2017-01-06'),
(2, 'Bombay', 'Hindi', 1, 06, 4, 20, 25, '1995-03-11'),
(3, 'Barfi', 'Hindi', 5, 04, 5, 30, 18, '2012-09-14'),
(4, 'Lover', 'English', 3, 02, 4, 5, 23, '2019-08-23'),
(5, 'Certified Loverboy', 'English', 6, 03, 6, 10, 30, '2021-09-03'),
(6, 'Lagaan', 'Hindi', 1, 05, 5, 5, 20, '2021-06-15'),
(7, 'Tim', 'English', 2, 04, 4, 2, 18, '2014-12-01'),
(8, 'Queen', 'Hindi', 7, 06, 2, 22, 25, '2017-08-30'),
(9, 'Believe', 'English', 4, 02, 3, 07, 22, '2012-06-15'),
(10, 'Purpose', 'English', 4, 01, 3, 10, 23, '2018-06-30'),
(11, 'Justice', 'English', 4, 03, 4, 09, 26, '2016-07-30'),
(12, 'Ranjhaana', 'Hindi', 1, 05, 3, 10, 21, '2012-03-15'),
(13, 'Cocktail', 'Hindi', 7, 05, 4, 22, 20, '2011-03-11'),
(14, 'Yaariyan', 'Hindi', 7, 05, 0, 12, 21, '2012-05-20'),
(15, 'Perfect', 'English', 8, 07, 4, 15, 24, '2017-09-26');

INSERT INTO tracks (track_id, track_name, track_length, album_id) VALUES
(1, 'I Forgot That You Existed', '00:02:50', 4),
(2, 'Cruel Summer', '00:02:58', 4),
(3, 'The Man', '00:03:10', 4),
(4, 'The Archer', '00:03:31', 4),
(5, 'Shape Of You', '00:03:53', 1),
(6, 'Eraser', '00:03:47', 1),
(7, 'Perfect', '00:04:23', 1),
(8, 'Bombay Theme', '00:07:24', 2),
(9, 'Humma', '00:05:11', 2),
(10, 'Kehna Hi Kya', '00:05:48', 2),
(11, 'Tu Hi Re', '00:07:12', 2),
(12, 'Chale Chalo', '00:06:40', 6),
(13, 'Mitwa', '00:06:47', 6),
(14, 'Ghanan Ghanan', '00:06:11', 6),
(15, 'Radha Kaise Na Jale', '00:05:34', 6),
(16, 'O Paalanhare', '00:05:18', 6),
(17, 'Champagne Poetry', '00:05:36', 5),
(18, "Papi's Home", '00:02:58', 5),
(19, 'Girls Want Girls', '00:03:41', 5),
(20, 'In The Bible', '00:04:56', 5),
(21, 'Fair Trade', '00:04:51', 5),
(22, 'Pipe Down', '00:03:25', 5),
(23, 'Someday', '00:05:40', 7),
(24, 'Kind In Jezelf', '00:04:57', 7),
(25, 'Engrenagem', '00:03:22', 7),
(26, 'At the Back of You', '00:04:23', 7),
(27, 'Boyfriend', '00:02:51', 9),
(28, 'Take You', '00:03:40', 9),
(29, 'Fall', '00:04:08', 9),
(30, 'Main Kya Karoon', '00:04:30', 3),
(31, 'Kyon', '00:04:26', 3),
(32, 'Phir Le Aaya Dil', '00:04:45', 3),
(33, 'Aashiyan', '00:03:56', 3),
(34, 'Ala Barfi', '00:05:19', 3),
(35, 'London Thumakda', '00:03:34', 8),
(36, 'Kinare', '00:03:32', 8),
(37, 'Sorry', '00:03:20', 10),
(38, 'No Pressure', '00:04:46', 10),
(39, 'Mark My Words', '00:02:14', 10), 
(40, 'Deserve You', '00:03:07', 11),
(41, 'Off My Face', '00:02:36', 11),
(42, 'Unstable', '00:02:38', 11),
(43, 'Hold On', '00:02:50', 11),
(44, 'Banrasiya', '00:04:49', 12),
(45, 'Tum Tak', '00:05:04', 12),
(46, 'Ay Sakhi', '00:04:06', 12),
(47, 'Tum Hi Ho Bandhu', '00:04:42', 13),
(48, 'Yaariyaan', '00:06:17', 13),
(49, 'Jugni', '00:06:57', 13),
(50, 'Second Hand Jawani', '00:04:02', 13),
(51, 'Baarish', '00:06:14', 14),
(52, 'Sunny Sunny', '00:04:03', 14),
(53, 'Meri Maa', '00:05:17', 14),
(54, 'Mujhe Ishq Se', '00:05:44', 14),
(55, 'ABCD', '00:03:25', 14),
(56, 'Perfect', '00:04:25', 15);

INSERT INTO orders (order_id, order_date, customer_id, order_amount) VALUES
(1, '2021-09-13', 1, 38),
(2, '2021-10-16', 2, 50),
(3, '2021-10-13', 3, 63),
(4, '2021-09-03', 5, 40),
(5, '2021-08-28', 1, 25),
(6, '2021-09-16', 4, 50),
(7, '2021-10-10', 2, 47),
(8, '2021-09-22', 13, 21),
(9, '2021-08-02', 10, 44),
(10, '2021-10-16', 4, 16),
(11, '2021-10-17', 7, 50),
(12, '2021-08-10', 8, 43),
(13, '2021-08-30', 9, 25),
(14, '2021-09-25', 7, 22),
(15, '2021-08-25', 11, 21),
(16, '2021-10-13', 14, 20),
(17, '2021-10-18', 9, 18),
(18, '2021-10-19', 6, 20),
(19, '2021-10-24', 15, 24);

INSERT INTO orders_to_albums(order_id, album_id) VALUES
(1, 1),
(1, 3),
(2, 5),
(2, 6),
(3, 1),
(3, 2),
(3, 3),
(4, 7),
(4, 9),
(5, 8),
(6, 5),
(6, 6),
(7, 11),
(7, 12),
(8, 12),
(9, 7),
(9, 11),
(10, 8),
(10, 12),
(11, 1),
(11, 5),
(12, 1),
(12, 4),
(13, 8),
(14, 9),
(15, 14),
(16, 13),
(17, 3),
(18, 1),
(19, 15);

/********************************************************
* NAME:-This script creates the view named country_to_album.
* USE:- This view brings album_name and count of sold albums with country of customers.
*********************************************************/
-- create a view
CREATE OR REPLACE VIEW country_to_album AS
	SELECT ca.country, a.album_name, MAX(no_of_albums) AS number_of_albums
		FROM albums a
			JOIN ( 
				SELECT c.country, oa.album_id, COUNT(oa.album_id) as no_of_albums
					FROM orders o
						JOIN customers c
							ON o.customer_id = c.customer_id
						JOIN orders_to_albums oa
							ON o.order_id = oa.order_id
					GROUP BY c.country, oa.album_id
            ) ca
				ON ca.album_id = a.album_id
		GROUP BY ca.country, a.album_name
        ORDER BY country, number_of_albums DESC;

-- Result of a view
SELECT * from country_to_album;

SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));  
/********************************************************
* NAME:-This script creates the procedure named test.
* USE:- It is to check vip eligibility of all customers based on the
	   average amount that they have spent in previous month.
       and display with their name and id.
*********************************************************/

-- Drop stored procedure if exists
DROP PROCEDURE IF EXISTS test;

-- Creates Stored Procedure

DELIMITER //
CREATE PROCEDURE test()
BEGIN
	DECLARE messege VARCHAR(255);
    DECLARE avg_amount INT;
    
    SET avg_amount = (SELECT AVG(order_Amount) FROM orders);

    SELECT o.customer_id,c.customer_name,
		CASE WHEN order_amount >= avg_amount THEN 
			'You are eligible to become VIP member'
		ELSE
			'You are not eligible to become VIP member'
		END AS vip_eligibility
	FROM orders o
		JOIN customers c
			ON o.customer_id = c.customer_id
	WHERE order_date >= '2021-10-01' AND order_date <= '2021-10-31'
    GROUP BY o.customer_id
    ORDER BY o.customer_id;
 
END //

-- calling a stored procedure
CALL test();


/********************************************************
* NAME:-This script creates the function named get_customer_details_by_name.
* USE:- It is to bring details of customers by their names.
*********************************************************/
-- Drop function if exists
DROP FUNCTION IF EXISTS get_customer_details_by_name;

-- Creates Function
DELIMITER //
CREATE FUNCTION get_customer_details_by_name
(
	customer_name_param VARCHAR(255)
)
RETURNS INT
DETERMINISTIC READS SQL DATA
BEGIN
	DECLARE customer_id_var INT;
    
    SELECT customer_id
		INTO customer_id_var
		FROM customers
        WHERE customer_name = customer_name_param;
	
    RETURN(customer_id_var);
END //

-- Executes function
SELECT *
	FROM customers
    WHERE customer_id = get_customer_details_by_name('Niah');



