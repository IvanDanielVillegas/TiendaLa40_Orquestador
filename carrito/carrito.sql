CREATE TABLE carrito(
    id INTEGER NOT NULL,
	status_carrito VARCHAR(100),
    date_carrito Date,
    customer_id_fk INTEGER NOT NULL,
	PRIMARY KEY (id)
    --FOREIGN KEY (customer_id_fk) REFERENCES cliente
);
