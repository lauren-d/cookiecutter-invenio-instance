{% include 'misc/header.py' %}
"""Records Templates Elasticsearch."""


def list_es_templates():
    """Elasticsearch templates path."""
    return [
        '{{ cookiecutter.package_name }}.es_templates'
    ]