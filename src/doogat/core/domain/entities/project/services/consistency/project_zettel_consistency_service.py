"""
Module providing services for maintaining consistency in project zettels.

This module contains the `ProjectZettelConsistencyService` class, which offers
methods to ensure consistency in zettel data.
"""

from doogat.core.domain.entities.project.services.consistency.fixers.fix_lists_bullets import (
    fix_lists_bullets,
)
from doogat.core.domain.entities.project.services.consistency.fixers.normalize_sections_order import (
    normalize_sections_order,
)
from doogat.core.domain.value_objects.zettel_data import ZettelData


class ProjectZettelConsistencyService:
    """
    Service class responsible for maintaining consistency in project zettels.

    This class provides static methods to perform various consistency checks and
    fixes on zettel data.
    """

    @staticmethod
    def ensure_consistency(zettel_data: ZettelData) -> None:
        """
        Ensure consistency in the given zettel data.

        This method applies multiple consistency fixes to the provided zettel data,
        including fixing list bullets and normalizing section order.

        :param zettel_data: The :class:`ZettelData` object to ensure consistency for.
        :return: None
        """
        fix_lists_bullets(zettel_data)
        normalize_sections_order(zettel_data)
