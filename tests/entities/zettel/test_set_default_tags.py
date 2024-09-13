from unittest.mock import MagicMock

import pytest
from doogat.core.domain.entities.zettel.services.consistency.fixers.set_default_tags import (
    set_default_tags,
)
from doogat.core.domain.value_objects.zettel_data import ZettelData


def test_set_default_tags():
    mock_zettel_data = MagicMock(spec=ZettelData)
    mock_zettel_data.metadata = {}
    set_default_tags(mock_zettel_data)
    assert "tags" in mock_zettel_data.metadata
    assert mock_zettel_data.metadata["tags"] == []


def test_set_default_tags_no_metadata():
    mock_zettel_data = MagicMock(spec=ZettelData)
    del mock_zettel_data.metadata  # Simulate missing metadata
    with pytest.raises(AttributeError):
        set_default_tags(mock_zettel_data)
