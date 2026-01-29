import pytest
from validation.event_schema_validation import (
    get_expected_event_schema,
    validate_event_schema,
)


@pytest.fixture
def expected_schema():
    return get_expected_event_schema()


@pytest.fixture
def valid_event():
    return {
        "event": "purchase",
        "user_name": "Ama",
        "product": "Laptop",
        "price": 2500.50,
        "event_time": "2026-01-28 20:00:00",
    }



def test_valid_event_schema_passes(valid_event, expected_schema):
    result = validate_event_schema(valid_event, expected_schema)
    assert result is True



def test_missing_field_fails_validation(valid_event, expected_schema):
    valid_event.pop("price")

    result = validate_event_schema(valid_event, expected_schema)
    assert result is False


def test_extra_field_fails_validation(valid_event, expected_schema):
    valid_event["currency"] = "USD"

    result = validate_event_schema(valid_event, expected_schema)
    assert result is False


def test_wrong_type_fails_validation(valid_event, expected_schema):
    valid_event["price"] = "2500"  # should be float

    result = validate_event_schema(valid_event, expected_schema)
    assert result is False
