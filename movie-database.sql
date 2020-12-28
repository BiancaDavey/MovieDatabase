-- Database tables for the movie sales business.

CREATE TABLE Customers (
customer_id INT NOT NULL,
last_name VARCHAR(50) NOT NULL,
first_name VARCHAR(50) NOT NULL,
address VARCHAR(200),
city VARCHAR(50),
state VARCHAR(3) CHECK(state IN ('NSW', 'QLD', 'VIC', 'ACT', 'TAS', 'NT', 'SA', 'WA')), 
postcode VARCHAR(8),
PRIMARY KEY (customer_id)
);

CREATE TABLE Movies (
movie_id INT NOT NULL,
movie_title VARCHAR(100) NOT NULL,
director_last_name VARCHAR(50) NOT NULL,
director_first_name VARCHAR(50) NOT NULL,
genre VARCHAR(20) CHECK(genre IN ('Action', 'Adventure', 'Comedy', 'Romance', 'Science Fiction', 'Documentary', 'Drama', 'Horror')),
media_type VARCHAR(20) CHECK(media_type IN ('DVD', 'Blu-Ray')),
release_date DATE,
studio_name VARCHAR(50),
retail_price REAL CHECK(retail_price > 0),
current_stock INT CHECK(current_stock >= 0),
PRIMARY KEY (movie_id)
);

CREATE TABLE Shipments (
shipment_id INT NOT NULL,
customer_id INT NOT NULL,
movie_id INT NOT NULL,
shipment_date DATE,
PRIMARY KEY(shipment_id),
FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)
	ON UPDATE CASCADE,
FOREIGN KEY(movie_id) REFERENCES Movies(movie_id)
	ON UPDATE CASCADE
);
