{% include 'misc/header.py' %}
"""Pytest fixtures and plugins for the API application."""

import pytest
from invenio_app.factory import create_api


@pytest.fixture(scope='module')
def app_config(app_config):
    """Get app config."""
    app_config['CELERY_ALWAYS_EAGER'] = True
    return app_config


@pytest.fixture(scope='module')
def create_app():
    """Create test app."""
    return create_api
