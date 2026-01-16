-- ============================================================
-- Database initialization script
-- Creates tables required for the streaming pipeline
-- ============================================================

CREATE TABLE IF NOT EXISTS ecommerce_events (
    id INTEGER,
    event VARCHAR(50),
    user_name VARCHAR(50),
    product VARCHAR(50),
    price DOUBLE PRECISION,
    event_time TIMESTAMP
);
