from doogat.core.domain.value_objects.zettel_data import ZettelData

TYPE_MIGRATIONS = {
    "loop": "project",
    "wiki-article": "note",
    "zettel": "note",
}


def normalize_type(zettel_data: ZettelData) -> None:
    zettel_data.metadata["type"] = TYPE_MIGRATIONS.get(
        zettel_data.metadata["type"],
        zettel_data.metadata["type"],
    )
