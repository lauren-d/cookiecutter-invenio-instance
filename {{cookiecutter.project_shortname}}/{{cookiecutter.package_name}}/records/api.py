{% include 'misc/header.py' %}
"""Records API."""

from invenio_records.api import Record as BaseRecord


class Record(BaseRecord):
    """Custom record."""

    _schema = "records/record-v1.0.0.json"
