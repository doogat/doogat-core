from unittest.mock import MagicMock, patch

import pytest
from buvis.pybase.formatting import StringOperator

import doogat.core.domain.entities as doogat_entities
from doogat.core.domain.services.doogat_factory import DoogatFactory


@pytest.fixture
def zettel():
    zettel = MagicMock(spec=doogat_entities.Zettel)
    zettel.get_data = MagicMock(return_value={"some": "data"})
    return zettel


def test_create_with_generic_type(zettel):
    zettel.type = ""
    with patch.object(doogat_entities, "Zettel", return_value=zettel):
        result = DoogatFactory.create(zettel)
        assert result is zettel


def test_create_with_invalid_type(zettel):
    zettel.type = "invalid"
    with (
        patch.object(StringOperator, "camelize", return_value="InvalidZettel"),
        patch.object(doogat_entities, "InvalidZettel", None, create=True),
    ):
        result = DoogatFactory.create(zettel)
        assert result is zettel
