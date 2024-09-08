class ZettelRepositoryZettelNotFoundError(Exception):
    """Zettel not found in ZettelRepository"""

    def __ini__(
        self: "ZettelRepositoryZettelNotFoundError",
        message: str = "Zettel not found in repository.",
    ) -> None:
        super().__init__(message)
