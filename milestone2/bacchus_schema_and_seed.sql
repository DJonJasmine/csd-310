CREATE DATABASE IF NOT EXISTS project_bacchus;
USE project_bacchus;

/* =========================
   DEPARTMENT TABLE
   ========================= */
CREATE TABLE department (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL
);

/* =========================
   EMPLOYEE TABLE
   ========================= */
CREATE TABLE employee (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_id INT NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    position VARCHAR(50),
    supervisor_id INT NULL,
    hire_date DATE,
    FOREIGN KEY (dept_id) REFERENCES department(dept_id),
    FOREIGN KEY (supervisor_id) REFERENCES employee(employee_id)
);

/* =========================
   EMPLOYEE HOURS TABLE
   ========================= */
CREATE TABLE employee_hours (
    hours_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    quarter VARCHAR(10),
    year INT,
    hours_worked DECIMAL(6,2),
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
);

/* =========================
   SUPPLIER TABLE
   ========================= */
CREATE TABLE supplier (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(100),
    item_supplied VARCHAR(100),
    contact_info VARCHAR(100)
);

/* =========================
   DISTRIBUTOR TABLE
   ========================= */
CREATE TABLE distributor (
    distributor_id INT AUTO_INCREMENT PRIMARY KEY,
    distributor_name VARCHAR(100),
    region VARCHAR(100),
    contact_info VARCHAR(100)
);

/* =========================
   PRODUCT TABLE
   ========================= */
CREATE TABLE product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    wine_type VARCHAR(50),
    wine_year INT,
    quantity_produced INT,
    unit_price DECIMAL(10,2)
);

/* =========================
   INVENTORY TABLE
   ========================= */
CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity_on_hand INT,
    last_updated DATE,
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

/* =========================
   SHIPMENT TABLE
   ========================= */
CREATE TABLE shipment (
    shipment_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_id INT NOT NULL,
    distributor_id INT NOT NULL,
    shipment_date DATE,
    expected_delivery DATE,
    actual_delivery_date DATE,
    delivery_status VARCHAR(50),
    FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id),
    FOREIGN KEY (distributor_id) REFERENCES distributor(distributor_id)
);

/* =========================
   SHIPMENT DETAIL TABLE
   ========================= */
CREATE TABLE shipment_detail (
    shipment_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    shipment_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT,
    unit_price DECIMAL(10,2),
    subtotal DECIMAL(10,2),
    FOREIGN KEY (shipment_id) REFERENCES shipment(shipment_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

/* =====================================
   INSERT SEED DATA
   ===================================== */

/* DEPARTMENT */
INSERT INTO department (dept_name) VALUES
('Production'),
('Sales'),
('Tasting Room'),
('Distribution');

/* EMPLOYEE */
INSERT INTO employee (dept_id, first_name, last_name, position, supervisor_id, hire_date) VALUES
(1, 'Stan', 'Bacchus', 'Owner', NULL, '2010-03-01'),
(1, 'Davis', 'Bacchus', 'Winemaker', 1, '2012-06-15'),
(2, 'Claire', 'Monroe', 'Sales Manager', 1, '2018-09-10'),
(3, 'Emily', 'Hart', 'Tasting Lead', 3, '2021-05-21'),
(4, 'Marcus', 'Reed', 'Distribution Coordinator', 1, '2019-04-14'),
(4, 'Lana', 'Chen', 'Logistics Assistant', 5, '2022-11-01');

/* EMPLOYEE HOURS */
INSERT INTO employee_hours (employee_id, quarter, year, hours_worked) VALUES
(1, 'Q1', 2025, 520),
(2, 'Q1', 2025, 480),
(3, 'Q1', 2025, 450),
(4, 'Q1', 2025, 400),
(5, 'Q1', 2025, 430),
(6, 'Q1', 2025, 395);

/* SUPPLIER */
INSERT INTO supplier (supplier_name, item_supplied, contact_info) VALUES
('Valley Oak Barrels', 'Wine Barrels', 'oak@valley.com'),
('Napa Glassworks', 'Bottles', 'glass@napa.com'),
('Harvest Labels Co', 'Labels', 'labels@harvest.com');

/* DISTRIBUTOR */
INSERT INTO distributor (distributor_name, region, contact_info) VALUES
('Golden State Distributing', 'California', 'ca@goldstate.com'),
('Northwest Wine Co', 'Oregon Washington', 'nw@wineco.com'),
('Coastal Beverages', 'East Coast', 'coastal@bev.com');

/* PRODUCT */
INSERT INTO product (product_name, wine_type, wine_year, quantity_produced, unit_price) VALUES
('Cabernet Reserve', 'Red', 2022, 850, 55.00),
('Chardonnay Estate', 'White', 2023, 900, 35.00),
('Rosé Summer Blend', 'Rosé', 2023, 700, 27.50);

/* INVENTORY */
INSERT INTO inventory (product_id, quantity_on_hand, last_updated) VALUES
(1, 600, '2025-01-15'),
(2, 720, '2025-01-15'),
(3, 500, '2025-01-15');

/* SHIPMENT */
INSERT INTO shipment (supplier_id, distributor_id, shipment_date, expected_delivery, actual_delivery_date, delivery_status) VALUES
(1, 1, '2025-01-10', '2025-01-20', '2025-01-19', 'Delivered'),
(2, 2, '2025-01-12', '2025-01-22', '2025-01-23', 'Delayed');

/* SHIPMENT DETAIL */
INSERT INTO shipment_detail (shipment_id, product_id, quantity, unit_price, subtotal) VALUES
(1, 1, 120, 55.00, 6600.00),
(1, 2, 150, 35.00, 5250.00),
(2, 3, 200, 27.50, 5500.00);
