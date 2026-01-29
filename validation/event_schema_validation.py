from typing import Dict, Any


def get_expected_event_schema() -> Dict[str, type]:
    """
    Defines the expected schema for a user event.
    """
    return {
        "event": str,
        "user_name": str,
        "product": str,
        "price": float,
        "event_time": str,
    }


def validate_event_schema(
    event: Dict[str, Any],
    expected_schema: Dict[str, type],
) -> bool:
    """
    Validates a single event against the expected schema.

    Returns:
    - True if schema matches
    - False if schema is invalid
    """

    # Check missing or extra fields
    if set(event.keys()) != set(expected_schema.keys()):
        return False

    # Check data types
    for field, expected_type in expected_schema.items():
        if not isinstance(event[field], expected_type):
            return False

    return True


