import doogat.core.domain.entities as doogat_entities
from doogat.core.domain.interfaces.zettel_repository import ZettelRepository
from doogat.core.domain.services.doogat_factory import DoogatFactory


class ReadDoogatUseCase:
    def __init__(self: "ReadDoogatUseCase", repository: ZettelRepository) -> None:
        self.repository = repository

    def execute(
        self: "ReadDoogatUseCase",
        repository_location: str,
    ) -> doogat_entities.Zettel:
        zettel = self.repository.find_by_location(repository_location)
        return DoogatFactory.create(zettel)
