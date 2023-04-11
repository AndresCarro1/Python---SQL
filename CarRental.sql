CREATE DATABASE CarRental;
USE CarRental;

CREATE TABLE categories (
		cat_id INT NOT NULL AUTO_INCREMENT,
        cat_desc VARCHAR (255),
        cat_label VARCHAR (40),
        PRIMARY KEY (cat_id)
);

CREATE TABLE vehicles (
		plate VARCHAR (7) NOT NULL,
        brand VARCHAR (20),
        model VARCHAR (20),
        color VARCHAR (40),
        man_year YEAR,
        cat_id INT,
        PRIMARY KEY (plate),
        FOREIGN KEY (cat_id) REFERENCES categories (cat_id)
);

CREATE TABLE customers (
		cust_id INT NOT NULL AUTO_INCREMENT,
        first_name VARCHAR (40),
        last_name VARCHAR (40),
        mobile INT (20),
        ssn VARCHAR (20) NOT NULL,
        email VARCHAR (255),
        country VARCHAR (40),
        PRIMARY KEY (cust_id)
);

CREATE TABLE reservations(
		reservation_id INT NOT NULL AUTO_INCREMENT,
        plate VARCHAR (7) NOT NULL,
        cust_id INT NOT NULL,
        pick_date DATE,
        return_date DATE,
        amount DECIMAL (6,2),
        PRIMARY KEY (reservation_id),
        FOREIGN KEY (plate) references vehicles (plate),
        FOREIGN KEY (cust_id) references customers (cust_id)
);

INSERT INTO categories (cat_desc, cat_label) VALUES 
("Sedan", "Sedan 4 doors"), ("Hatchback", "Sedan 5 doors"), 
("Pick up", "Pick up 4 doors"), ("SUV", "urban SUV"), 
("Off road", "4WD SUV or Pick Up"), ("Luxury", "Premium Sedan");

INSERT INTO vehicles (plate, brand, model, color, man_year, cat_id) VALUES
("AB726SY", "Chevrolet", "Cruze", "White", "2017", "1"),
("AD123XY", "Fiat", "Cronos", "Red", "2019", "1"),
("AB321ST", "Fiat", "Argos", "White", "2017", "2"),
("AB111RA", "Volkswagen", "Gol", "Black", "2017", "2"),
("AF626AB", "Ford", "Ranger", "Blue", "2022", "3"),
("AD444MA", "Toyota", "Hilux", "Green", "2019", "3"),
("AB221IT", "Chevrolet", "Tracker", "White", "2017", "4"),
("AC418MT", "Volkswagen", "Taos", "Blue", "2018", "4"),
("AC213AB", "Volkswagen", "Amarok", "Champagne", "2018", "5"),
("AD552ZO", "Jeep", "Renegade", "Black", "2019", "5"),
("AB215AZ", "Toyota", "Land Cruiser", "Black", "2017", "6"),
("AF007DT", "Audi", "A6", "Black", "2022", "6");

INSERT INTO customers (first_name, last_name, mobile, ssn, email, country) VALUES
("Sebastian", "Bach", "01434541942", "43196534", "sbach@hotmail.com", "Austria"),
("Ludwig", "Beethoven", "0423612874", "17124868", "ludwigb@gmail.com", "Germany"),
("Pedro", "Pascal", "0374121920", "29233441", "ppascal@hotmail.com", "Chile"),
("Gal", "Gadot", "0474421351", "92323119", "galwoman@hotmail.com", "Israel"),
("Rocco", "Silfredi", "0584124208", "93488922", "bigrocco@hotmail.com", "Italy"),
("Michal", "Kaleki", "0614884123", "43924821", "ecopole@gmail.com", "Poland");

INSERT INTO reservations (plate, cust_id, pick_date, return_date, amount) VALUES
("AF626AB", "5", "2022-01-03", "2022-01-10", "700"),
("AF007DT", "6", "2023-02-11", "2023-02-12", "250"),
("AD444MA", "1", "2022-11-04", "2022-12-04", "4000"),
("AB111RA", "3", "2023-01-03", "2023-02-03", "4200"),
("AB321ST", "2", "2023-03-03", "2023-03-05", "400"),
("AD123XY", "4", "2022-06-01", "2022-06-12", "2100"),
("AB215AZ", "4", "2022-09-04", "2022-09-18", "3000"),
("AC418MT", "3", "2022-03-01", "2022-05-12", "6000"),
("AB221IT", "1", "2023-02-10", "2023-02-12", "360"),
("AB726SY", "2", "2022-01-01", "2022-01-21", "1800"),
("AD552ZO", "5", "2022-10-05", "2022-10-15", "1200");

