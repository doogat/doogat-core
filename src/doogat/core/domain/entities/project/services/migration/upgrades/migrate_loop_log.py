"""
This module provides functionality to migrate log entries from zettel data sections into a structured log format.

It includes functions to parse log entries from text content and update the zettel data structure accordingly.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from doogat.core.domain.value_objects.zettel_data import ZettelData

import re
from datetime import datetime


def migrate_loop_log(zettel_data: ZettelData) -> None:
    """
    Migrate log entries from the first section of the zettel data to a new log section.

    :param zettel_data: The zettel data to be processed.
    :type zettel_data: :class:`ZettelData`
    :return: None. The function modifies the `zettel_data` in place.
    """
    header, content = zettel_data.sections[0]
    log_entries, remaining_content = extract_log_entries(content)
    formatted_log = format_log_entries(log_entries)

    zettel_data.sections[0] = (header, "\n".join(remaining_content))
    if formatted_log:
        zettel_data.sections.append(("## Log", formatted_log))


def extract_log_entries(
    content: str,
) -> tuple[list[tuple[datetime, str, str]], list[str]]:
    """
    Extract log entries from the provided content string.

    :param content: The content from which to extract log entries.
    :type content: str
    :return: A tuple containing a list of log entries and a list of unmatched lines.
    :rtype: tuple[list[tuple[datetime, str, str]], list[str]]
    """
    log_pattern = r"(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}) - (.*?)(?: => (.*))?$"
    matches = []
    unmatched_lines = []

    for line in content.split("\n"):
        match = re.match(log_pattern, line.strip())
        if match:
            date_str, before, after = match.groups()
            date_obj = datetime.strptime(date_str, "%d.%m.%Y %H:%M").astimezone()
            matches.append((date_obj, before.strip(), after.strip() if after else ""))
        else:
            if line.strip():
                unmatched_lines.append(line.strip())

    return matches, unmatched_lines


def format_log_entries(log_entries: list[tuple[datetime, str, str]]) -> str:
    """
    Format log entries into a structured log string.

    :param log_entries: List of log entries.
    :type log_entries: list[tuple[datetime, str, str]]
    :return: Formatted log string.
    :rtype: str
    """
    log_content = ""
    task_status = " "
    for date, before, after in log_entries:
        if not after:
            log_content += f"- [i] {date.strftime('%Y-%m-%d %H:%M')} - {before}\n"
        else:
            log_content += f"- [{task_status}] {date.strftime('%Y-%m-%d %H:%M')} - {before} => {after}\n"
            task_status = "x"
    return log_content
