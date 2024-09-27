-- Create the database and tables for the RRHH system
CREATE DATABASE IF NOT EXISTS Binarq_RRHH;

USE Binarq_RRHH;

-- Table for personal data
CREATE TABLE personal_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    codigo INT,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    dpi VARCHAR(20),
    nit VARCHAR(15),
    phone VARCHAR(15),
    email VARCHAR(100),
    gender ENUM('male', 'female'),
    age INT,
    birth_date DATE,
    civil_status ENUM('single', 'married', 'divorced', 'widowed')
);

-- Table for complementary data
CREATE TABLE complementary_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    codigo INT,
    nationality VARCHAR(50),
    department VARCHAR(50),
    municipio VARCHAR(50),
    address VARCHAR(255)
    FOREIGN KEY (codigo) REFERENCES personal_data(codigo)
);

-- Table for family data
CREATE TABLE family_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    codigo INT,
    sos_name1 VARCHAR(50),
    sos_contact1 VARCHAR(15),
    sos_name2 VARCHAR(50),
    sos_contact2 VARCHAR(15),
    FOREIGN KEY (codigo) REFERENCES personal_data(codigo)
);

-- Table for employee photos
CREATE TABLE employee_photos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    codigo INT,
    photoBase64 TEXT,
    FOREIGN KEY (codigo) REFERENCES personal_data(codigo)
);

-- Table for work data
CREATE TABLE work_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    codigo INT,
    profession VARCHAR(100),
    occupation VARCHAR(50),
    department VARCHAR(50),
    project VARCHAR(100),
    initial_salary DECIMAL(10, 2),
    salary DECIMAL(10, 2),
    bonus DECIMAL(10, 2),
    other_bonus DECIMAL(10, 2),
    start_date DATE,
    end_date DATE,
    igss VARCHAR(50),
    benefits TEXT,
    FOREIGN KEY (codigo) REFERENCES personal_data(codigo)
);
