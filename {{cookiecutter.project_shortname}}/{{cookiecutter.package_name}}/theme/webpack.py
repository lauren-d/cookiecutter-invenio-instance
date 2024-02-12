{% include 'misc/header.py' %}
"""JS/CSS Webpack bundles for theme."""

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    'assets',
    default='semantic-ui',
    themes={
        'bootstrap3': dict(
            entry={
                '{{ cookiecutter.project_shortname }}-theme': './scss/{{ cookiecutter.package_name }}/theme.scss',
            },
            dependencies={},
            aliases={},
        ),
        'semantic-ui': dict(
            entry={
                # add entries here...
            },
            dependencies={
                # add any additional npm dependencies here...
                "@tinymce/tinymce-react": "^4.3.0",
                "@babel/runtime": "^7.9.0",
                "@ckeditor/ckeditor5-build-classic": "^16.0.0",
                "@ckeditor/ckeditor5-react": "^2.1.0",
                "formik": "^2.1.0",
                "i18next": "^20.3.0",
                "i18next-browser-languagedetector": "^6.1.0",
                "luxon": "^1.23.0",
                "query-string": "^7.0.0",
                "path": "^0.12.7",
                "prop-types": "^15.7.2",
                "react-copy-to-clipboard": "^5.0.0",
                "react-dnd": "^11.1.0",
                "react-dnd-html5-backend": "^11.1.0",
                "react-dropzone": "^11.0.0",
                "react-i18next": "^11.11.0",
                "react-invenio-forms": "^3.0.0",
                "react-searchkit": "^2.0.0",
                "yup": "^0.32.0",
            },
            aliases={
                '../../theme.config$': 'less/{{ cookiecutter.package_name }}/theme.config',
            },
        ),
    }
)
