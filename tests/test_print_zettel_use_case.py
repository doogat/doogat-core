from unittest.mock import MagicMock

import pytest
from doogat.core.application.use_cases.print_zettel_use_case import PrintZettelUseCase
from doogat.core.domain.interfaces.zettel_formatter import ZettelFormatter
from doogat.core.domain.value_objects.zettel_data import ZettelData


@pytest.fixture()
def mock_zettel_formatter() -> MagicMock:
    return MagicMock(spec=ZettelFormatter)


@pytest.fixture()
def mock_zettel_data() -> MagicMock:
    return MagicMock(spec=ZettelData)


def test_print_doogat_use_case_initialization(mock_zettel_formatter: MagicMock) -> None:
    use_case = PrintZettelUseCase(mock_zettel_formatter)
    assert isinstance(use_case, PrintZettelUseCase)
    assert use_case.formatter == mock_zettel_formatter


def test_print_doogat_use_case_execute(capsys, mock_zettel_formatter, mock_zettel_data):
    formatted_output = "Formatted Zettel Data"
    mock_zettel_formatter.format.return_value = formatted_output

    use_case = PrintZettelUseCase(mock_zettel_formatter)
    use_case.execute(mock_zettel_data)

    captured = capsys.readouterr()
    assert captured.out.strip() == formatted_output
    mock_zettel_formatter.format.assert_called_once_with(mock_zettel_data)
