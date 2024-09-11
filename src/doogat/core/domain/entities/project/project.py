from doogat.core.domain.entities.project.services.consistency.project_zettel_consistency_service import (
    ProjectZettelConsistencyService,
)
from doogat.core.domain.entities.project.services.migration.project_zettel_migration_service import (
    ProjectZettelMigrationService,
)
from doogat.core.domain.entities.zettel.zettel import Zettel


class ProjectZettel(Zettel):
    def __init__(self: "ProjectZettel") -> None:
        super().__init__()

    def _migrate(self: "ProjectZettel") -> None:
        super()._migrate()
        ProjectZettelMigrationService.migrate(self._data)

    def _ensure_consistency(self: "ProjectZettel") -> None:
        super()._ensure_consistency()
        ProjectZettelConsistencyService.ensure_consistency(self._data)

    @property
    def log(self: "ProjectZettel") -> str:
        for section in self._data.sections:
            if section[0] == "## Log":
                return section[1]
        return ""
