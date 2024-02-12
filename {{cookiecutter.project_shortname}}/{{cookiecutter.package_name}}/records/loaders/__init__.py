{% include 'misc/header.py' %}
"""Loaders.

This file contains sample loaders that can be used to deserialize input data in
an application level data structure. The marshmallow_loader() method can be
parameterized with different schemas for the record metadata. In the provided
json_v1 instance, it uses the MetadataSchemaV1, defining the
PersistentIdentifier field.
"""

from invenio_records_rest.loaders.marshmallow import (
    json_patch_loader,
    marshmallow_loader,
)

from ..marshmallow import MetadataSchemaV1

#: JSON loader using Marshmallow for data validation.
json_v1 = marshmallow_loader(MetadataSchemaV1)

__all__ = (
    'json_v1',
)
