-- ============================================================
-- Database initialization script
-- Creates tables required for the streaming pipeline
-- ============================================================

CREATE TABLE IF NOT EXISTS ecommerce_events (
    id INTEGER PRIMARY KEY,

    event VARCHAR(50) NOT NULL
        CHECK (
            event IN (
                'product_view',
                'add_to_cart',
                'remove_from_cart',
                'checkout',
                'purchase'
            )
        ),

    user_name VARCHAR(50) NOT NULL,
    product VARCHAR(50),
    price DOUBLE PRECISION,

    event_time TIMESTAMP NOT NULL,

    source_file TEXT,

    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
