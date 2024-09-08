from unittest.mock import MagicMock, patch

import pytest
from doogat.core.application.use_cases.read_doogat_use_case import ReadDoogatUseCase
from doogat.core.domain.entities import Zettel
from doogat.core.domain.interfaces.zettel_repository import ZettelRepository
from doogat.core.domain.interfaces.zettel_repository_exceptions import (
    ZettelRepositoryZettelNotFoundError,
)
from doogat.core.domain.services.doogat_factory import DoogatFactory


@pytest.fixture
def mock_zettel_repository():
    return MagicMock(spec=ZettelRepository)


@pytest.fixture
def mock_doogat_factory():
    return MagicMock(spec=DoogatFactory)


@pytest.fixture
def read_doogat_use_case(mock_zettel_repository):
    return ReadDoogatUseCase(mock_zettel_repository)


def test_read_doogat_use_case_init(mock_zettel_repository):
    use_case = ReadDoogatUseCase(mock_zettel_repository)
    assert use_case.repository == mock_zettel_repository


@patch("doogat.core.application.use_cases.read_doogat_use_case.DoogatFactory")
def test_execute_success(mock_doogat_factory, read_doogat_use_case):
    mock_zettel = MagicMock(spec=Zettel)
    read_doogat_use_case.repository.find_by_location.return_value = mock_zettel
    mock_doogat_factory.create.return_value = mock_zettel

    result = read_doogat_use_case.execute("test_location")

    assert result == mock_zettel
    read_doogat_use_case.repository.find_by_location.assert_called_once_with(
        "test_location"
    )
    mock_doogat_factory.create.assert_called_once_with(mock_zettel)


def test_execute_not_found(read_doogat_use_case):
    read_doogat_use_case.repository.find_by_location.return_value = None

    with pytest.raises(ZettelRepositoryZettelNotFoundError):
        read_doogat_use_case.execute("non_existent_location")

    read_doogat_use_case.repository.find_by_location.assert_called_once_with(
        "non_existent_location"
    )
