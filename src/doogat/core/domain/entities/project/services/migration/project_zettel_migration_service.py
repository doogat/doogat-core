from doogat.core.domain.entities.project.services.migration.upgrades.migrate_loop_log import (
    migrate_loop_log,
)
from doogat.core.domain.value_objects.zettel_data import ZettelData


class ProjectZettelMigrationService:
    @staticmethod
    def migrate(zettel_data: ZettelData) -> None:
        migrate_loop_log(zettel_data)
