from __future__ import annotations

from doogat.core.domain.value_objects.zettel_data import ZettelData


def normalize_sections_order(zettel_data: ZettelData) -> None:
    """
    Reorders the sections of a ZettelData object based on predefined criteria.

    The function reorders sections so that the first section starting with '# ' is placed first,
    followed by sections titled '## Description', '## Log', and '## Actions buffer'.
    All other sections are appended in their original order after these prioritized sections.

    :param zettel_data: The ZettelData object containing sections to be reordered.
    :type zettel_data: ZettelData
    :raises TypeError: If the input is not an instance of ZettelData.
    :return: None. The function modifies the zettel_data object in place.
    """
    if not isinstance(zettel_data, ZettelData):
        raise TypeError("Expected zettel_data to be of type ZettelData")

    # Initialize list for the four expected sections plus other sections
    reordered_sections = [("", "")] * 4
    other_sections = []

    # Mapping of specific section titles to their desired order
    order_map = {"## Description": 1, "## Log": 2, "## Actions buffer": 3}

    for section in zettel_data.sections:
        title, content = section
        if title.startswith("# ") and reordered_sections[0] == ("", ""):
            reordered_sections[0] = (title, content)
        elif title in order_map:
            index = order_map[title]
            reordered_sections[index] = (title, content)
        else:
            other_sections.append((title, content))

    # Remove empty sections and add other sections
    zettel_data.sections = [
        sec for sec in reordered_sections if sec[0] != ""
    ] + other_sections
