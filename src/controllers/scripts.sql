-- Create the database and tables for the RRHH system
CREATE DATABASE IF NOT EXISTS Binarq_RRHH;

USE Binarq_RRHH;

-- Table for personal data
CREATE TABLE personal_data (
    id_empleado INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    dpi VARCHAR(20),
    nit VARCHAR(15),
    phone VARCHAR(15),
    email VARCHAR(100),
    age INT,
    gender ENUM('male', 'female')
);

-- Table for complementary data
CREATE TABLE complementary_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_empleado INT,
    nationality VARCHAR(50),
    department VARCHAR(50),
    municipio VARCHAR(50),
    address VARCHAR(255),
    civil_status ENUM('single', 'married', 'divorced', 'widowed'),
    birth_date DATE,
    FOREIGN KEY (id_empleado) REFERENCES personal_data(id_empleado)
);

-- Table for family data
CREATE TABLE family_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_empleado INT,
    sos_name1 VARCHAR(50),
    sos_contact1 VARCHAR(15),
    sos_name2 VARCHAR(50),
    sos_contact2 VARCHAR(15),
    FOREIGN KEY (id_empleado) REFERENCES personal_data(id_empleado)
);

-- Table for employee photos
CREATE TABLE employee_photos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_empleado INT,
    photoBase64 TEXT,
    FOREIGN KEY (id_empleado) REFERENCES personal_data(id_empleado)
);

-- Table for work data
CREATE TABLE work_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_empleado INT,
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
    FOREIGN KEY (id_empleado) REFERENCES personal_data(id_empleado)
);
