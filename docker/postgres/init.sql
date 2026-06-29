CREATE TABLE public.inventory_movements (
    movement_id SERIAL PRIMARY KEY,
    product_sku VARCHAR(50) NOT NULL,
    batch_number VARCHAR(50) NOT NULL,
    from_location VARCHAR(50),
    to_location VARCHAR(50),
    qty DECIMAL(10,2) NOT NULL,
    movement_type VARCHAR(20) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO public.inventory_movements 
(product_sku, batch_number, from_location, to_location, qty, movement_type) 
VALUES 
('APEL-F', 'B-2026-06-12', 'RECEIVING', 'ZONE-A1', 500.00, 'PUTAWAY');