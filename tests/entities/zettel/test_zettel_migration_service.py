from typing import Any, Dict

from doogat.core.domain.entities.zettel.services.migration.zettel_migration_service import (
    ZettelMigrationService,
)
from doogat.core.domain.value_objects.zettel_data import ZettelData


def test_migrate() -> None:
    # Arrange
    zettel_data: ZettelData = ZettelData()
    zettel_data.metadata = {
        "zkn-id": "123",
        "tag": "test_tag",
        "type": "note",
        "other_field": "value",
    }

    # Act
    ZettelMigrationService.migrate(zettel_data)

    # Assert
    expected_data: Dict[str, Any] = {
        "id": "123",
        "tags": ["test_tag"],
        "type": "note",
        "other_field": "value",
    }
    assert zettel_data.metadata == expected_data


def test_migrate_no_zkn_id() -> None:
    # Arrange
    zettel_data: ZettelData = ZettelData()
    zettel_data.metadata = {"tag": "test_tag", "type": "note", "other_field": "value"}

    # Act
    ZettelMigrationService.migrate(zettel_data)

    # Assert
    expected_data: Dict[str, Any] = {
        "tags": ["test_tag"],
        "type": "note",
        "other_field": "value",
    }
    assert zettel_data.metadata == expected_data


def test_migrate_no_tag() -> None:
    # Arrange
    zettel_data: ZettelData = ZettelData()
    zettel_data.metadata = {"zkn-id": "123", "type": "note", "other_field": "value"}

    # Act
    ZettelMigrationService.migrate(zettel_data)

    # Assert
    expected_data: Dict[str, Any] = {
        "id": "123",
        "type": "note",
        "other_field": "value",
    }
    assert zettel_data.metadata == expected_data
