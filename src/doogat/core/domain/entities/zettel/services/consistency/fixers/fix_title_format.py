"""
This module provides functionality to format the title of a ZettelData object.

Imports:
- :class:`StringOperator` from the `buvis.pybase.formatting` module, used for text manipulation.
- :class:`ZettelData` from the `doogat.core.domain.value_objects.zettel_data` module, representing the data structure for zettel information.
"""

from buvis.pybase.formatting import StringOperator
from doogat.core.domain.value_objects.zettel_data import ZettelData


def fix_title_format(zettel_data: ZettelData) -> None:
    """
    Format the title of the given :class:`ZettelData` object by replacing abbreviations.

    This function modifies the 'title' field of the :class:`ZettelData` metadata dictionary in place,
    using the :class:`StringOperator` to replace abbreviations at a specified level.

    :param zettel_data: The ZettelData object whose title is to be formatted.
    :type zettel_data: :class:`ZettelData`
    :return: None. The function modifies the `zettel_data` in place.
    """
    zettel_data.metadata["title"] = StringOperator.replace_abbreviations(
        text=zettel_data.metadata["title"],
        level=0,
    )
