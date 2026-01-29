import csv
import os
from generator.data_generator import write_event_to_file


def test_csv_file_generation(tmp_path, monkeypatch):
    # Arrange: fake event
    event = {
        "event": "purchase",
        "user_name": "Ama",
        "product": "Laptop",
        "price": 2500.50,
        "event_time": "2026-01-28 20:00:00",
    }

    # Create temp input directory
    output_dir = tmp_path / "inputs"
    output_dir.mkdir()

    # Monkeypatch OUTPUT_DIR used by the module
    monkeypatch.setattr(
        "generator.data_generator.OUTPUT_DIR",
        str(output_dir),
    )

    timestamp = 123456789

    # Act
    write_event_to_file(event, timestamp)

    # Assert: file exists
    files = list(output_dir.glob("*.csv"))
    assert len(files) == 1

    # Assert: CSV content
    with open(files[0], newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        assert reader.fieldnames == list(event.keys())
        assert len(rows) == 1
        assert rows[0]["event"] == "purchase"
