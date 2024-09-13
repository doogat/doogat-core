from doogat.core.domain.entities.zettel.services.migration.upgrades.move_tag_to_tags import (
    move_tag_to_tags,
)
from doogat.core.domain.entities.zettel.services.migration.upgrades.move_zkn_id_to_id import (
    move_zkn_id_to_id,
)
from doogat.core.domain.entities.zettel.services.migration.upgrades.normalize_type import (
    normalize_type,
)
from doogat.core.domain.value_objects.zettel_data import ZettelData


class ZettelMigrationService:
    @staticmethod
    def migrate(zettel_data: ZettelData) -> None:
        move_zkn_id_to_id(zettel_data)
        move_tag_to_tags(zettel_data)
        normalize_type(zettel_data)
