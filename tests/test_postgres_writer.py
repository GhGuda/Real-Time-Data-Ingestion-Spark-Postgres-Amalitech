from unittest.mock import MagicMock
from load.postgres_writer import write_to_postgres


def test_write_to_postgres_uses_jdbc_correctly():
    # -----------------------------
    # Arrange
    # -----------------------------
    mock_df = MagicMock()
    mock_writer = MagicMock()

    # df.write returns writer
    mock_df.write = mock_writer

    url = "jdbc:postgresql://localhost:5432/testdb"
    table = "events"
    user = "postgres"
    password = "postgres"

    # Chainable writer methods
    mock_writer.format.return_value = mock_writer
    mock_writer.option.return_value = mock_writer
    mock_writer.mode.return_value = mock_writer

    # -----------------------------
    # Act
    # -----------------------------
    write_to_postgres(
        df=mock_df,
        url=url,
        table=table,
        user=user,
        password=password,
    )

    # -----------------------------
    # Assert
    # -----------------------------
    mock_writer.format.assert_called_once_with("jdbc")
    mock_writer.mode.assert_called_once_with("append")
    mock_writer.save.assert_called_once()
