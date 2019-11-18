{% include 'misc/header.py' %}
"""Default configuration."""

from __future__ import absolute_import, print_function

from invenio_indexer.api import RecordIndexer
from invenio_records_rest.facets import terms_filter
from invenio_records_rest.utils import allow_all, check_elasticsearch
from invenio_search import RecordsSearch

from {{ cookiecutter.package_name }}.records.api import Record


def _(x):
    """Identity function for string extraction."""
    return x

RECORDS_REST_ENDPOINTS = {
    'recid': dict(
        pid_type='recid',
        pid_minter='recid',
        pid_fetcher='recid',
        default_endpoint_prefix=True,
        record_class=Record,
        search_class=RecordsSearch,
        indexer_class=RecordIndexer,
        search_index='records',
        search_type=None,
        record_serializers={
            'application/json': ('{{ cookiecutter.package_name }}.records.serializers'
                                 ':json_v1_response'),
        },
        search_serializers={
            'application/json': ('{{ cookiecutter.package_name }}.records.serializers'
                                 ':json_v1_search'),
        },
        record_loaders={
            'application/json': ('{{ cookiecutter.package_name }}.records.loaders'
                                 ':json_v1'),
        },
        list_route='/records/',
        item_route='/records/<pid(recid,'
                   'record_class="{{ cookiecutter.package_name }}.records.api.Record")'
                   ':pid_value>',
        default_media_type='application/json',
        max_result_window=10000,
        error_handlers=dict(),
        create_permission_factory_imp=allow_all,
        read_permission_factory_imp=check_elasticsearch,
        update_permission_factory_imp=allow_all,
        delete_permission_factory_imp=allow_all,
        list_permission_factory_imp=allow_all,
        links_factory_imp='invenio_records_files.'
                          'links:default_record_files_links_factory',
    ),
}
"""REST API for {{cookiecutter.project_shortname}}."""

RECORDS_UI_ENDPOINTS = dict(
    recid=dict(
        pid_type='recid',
        route='/records/<pid_value>',
        template='records/record.html',
        record_class='invenio_records_files.api:Record',
    ),
    recid_preview=dict(
        pid_type='recid',
        route='/records/<pid_value>/preview/<path:filename>',
        view_imp='invenio_previewer.views.preview',
        record_class='invenio_records_files.api:Record',
    ),
    recid_files=dict(
        pid_type='recid',
        route='/records/<pid_value>/files/<path:filename>',
        view_imp='invenio_records_files.utils.file_download_ui',
        record_class='invenio_records_files.api:Record',
    ),
)
"""Records UI for {{cookiecutter.project_shortname}}."""

SEARCH_UI_JSTEMPLATE_RESULTS = 'templates/records/results.html'
"""Result list template."""

PIDSTORE_RECID_FIELD = '{{ cookiecutter.datamodel_pid_name }}'

{{ cookiecutter.package_name | upper }}_ENDPOINTS_ENABLED = True
"""Enable/disable automatic endpoint registration."""


RECORDS_REST_FACETS = dict(
    records=dict(
        aggs=dict(
            type=dict(terms=dict(field='type')),
            keywords=dict(terms=dict(field='keywords'))
        ),
        post_filters=dict(
            type=terms_filter('type'),
            keywords=terms_filter('keywords'),
        )
    )
)
"""Introduce searching facets."""


RECORDS_REST_SORT_OPTIONS = dict(
    records=dict(
        bestmatch=dict(
            title=_('Best match'),
            fields=['_score'],
            default_order='desc',
            order=1,
        ),
        mostrecent=dict(
            title=_('Most recent'),
            fields=['-_created'],
            default_order='asc',
            order=2,
        ),
    )
)
"""Setup sorting options."""


RECORDS_REST_DEFAULT_SORT = dict(
    records=dict(
        query='bestmatch',
        noquery='mostrecent',
    )
)
"""Set default sorting options."""

RECORDS_FILES_REST_ENDPOINTS = {
    'RECORDS_REST_ENDPOINTS': {
        'recid': '/files'
    },
}
"""Records files integration."""

FILES_REST_PERMISSION_FACTORY = \
    '{{ cookiecutter.package_name }}.records.permissions:files_permission_factory'
"""Files-REST permissions factory."""

PREVIEWER_PREFERENCE = [
    'csv_dthreejs',
    'iiif_image',
    'simple_image',
    'json_prismjs',
    'xml_prismjs',
    'mistune',
    'pdfjs',
    'ipynb',
    'zip',
]
"""IIIF previewer preferences."""
