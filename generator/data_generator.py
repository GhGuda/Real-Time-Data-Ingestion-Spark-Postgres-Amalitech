"""
Data Generator for Real-Time E-commerce Events

This script simulates real-time user activity on an e-commerce platform.
It continuously generates event-based JSON records (e.g. product views,
add-to-cart actions, and purchases) and writes them to a directory that
Apache Spark Structured Streaming monitors as a data source.
"""

import csv
import logging
import random
import time
from datetime import datetime
import os
from configs.logger_config import setup_logger

# -------------------------------------------------------------------
# Logging
# -------------------------------------------------------------------
setup_logger()
logger = logging.getLogger(__name__)

# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------

OUTPUT_DIR = os.getenv("OUTPUT_DIR", "data/inputs")
SLEEP_INTERVAL = int(os.getenv("SLEEP_INTERVAL", 3))


USERS = [
    "Ama", "Kojo", "Yaw", "Akosua", "Kwame", "Abena",
    "Kofi", "Efua", "Kwesi", "Adjoa", "Yawson", "KojoB",
    "AmaP", "Akua", "NanaYaw", "Naa", "Mensah",
    "Owusu", "Asante", "Boateng", "Appiah",
    "Kobby", "YawK", "Kojo_99", "Ama_gh",
    "KwameDev", "Akos_1", "EfuaX", "Yaw_T"
]

PRODUCTS = ["Laptop", "Phone", "Headphones", "Shoes", "Backpack"]
EVENTS = [
    "product_view",
    "add_to_cart",
    "remove_from_cart",
    "checkout",
    "purchase"
]

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_event(record_id: int) -> dict:
    """
    Generate a single e-commerce event record.

    Args:
        record_id (int): Unique identifier for the event.

    Returns:
        dict: A dictionary representing an e-commerce event.
    """
    return {
        "id": record_id,
        "event": random.choice(EVENTS),
        "user_name": random.choice(USERS),
        "product": random.choice(PRODUCTS),
        "price": round(random.uniform(50, 3000), 2),
        "event_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    


def write_event_to_file(event: dict, timestamp: int) -> None:
    """
    Write an event record to a CSV file.
    
    Write files atomically using a temporary file and rename,
    so Spark Structured Streaming never reads partially written files.

    Args:
        event (dict): The event data to write.
        timestamp (int): Used to create a unique file name.
    """
    
    
    timestamp = int(time.time() * 1000)
    final_path = os.path.join(OUTPUT_DIR, f"event_{timestamp}.csv")
    tmp_path = f"{final_path}.tmp"
    with open(tmp_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=event.keys())

        writer.writeheader()      # write column names
        writer.writerow(event)    # write data

    # Atomic rename: Spark sees file only after this
    os.rename(tmp_path, final_path)
    
    
    
def main() -> None:
    """
    Main loop that continuously generates and writes e-commerce events.
    """
    record_id = 1
    logging.info("Starting e-commerce data generator...")

    while True:
        try:
            timestamp = int(time.time() * 1000)
            
            event = generate_event(record_id)
            write_event_to_file(event, timestamp)

            logging.info(f"Generated event: {event}")

            record_id += 1
            time.sleep(SLEEP_INTERVAL)

        except Exception:
            logging.error("Error while generating or writing event", exc_info=True)
            time.sleep(SLEEP_INTERVAL)


if __name__ == "__main__":
    main()