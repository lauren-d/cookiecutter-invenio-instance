{% include 'misc/header.rst' %}
Requirements
============

We strongly recommend the use of nvm (Node Version Manager).

First install these tools on your operating system:

* `poetry <https://python-poetry.org/>`_
* npm
* node
* docker and docker-compose

Working version

.. table::

    +--------+---------+
    |  Tools | Version |
    +========+=========+
    | poetry |  1.7.0  |
    +--------+---------+
    |  node  | 14.21.3 |
    +--------+---------+
    |   npm  | 6.14.18 |
    +--------+---------+

The virtual environment creation for the project in order to sandbox our Python
environment, as well as manage the dependency installation, among other things.

How to update Node version with nvm

.. code-block:: console

    # First check you node version
    node --version # here, 10.16.3
    nvm install 14.21.3
    nvm use 14.21.3

Installation
============

Start all dependent services using docker-compose (this will start {{cookiecutter.database[:-3].title() + cookiecutter.database[-3:].upper()}},
Elasticsearch {{cookiecutter.elasticsearch}}, RabbitMQ and Redis):

.. code-block:: console

    $ docker-compose up -d

.. note::

    Make sure you have `enough virtual memory
    <https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-cli-run-prod-mode>`_
    for Elasticsearch in Docker:

    .. code-block:: shell

        # Linux
        $ sysctl -w vm.max_map_count=262144

        # macOS
        $ screen ~/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/tty
        <enter>
        linut00001:~# sysctl -w vm.max_map_count=262144


Next, bootstrap the instance (this will install all Python dependencies and
build all static assets):

.. code-block:: console

    $ poetry run ./scripts/bootstrap

Next, create database tables, search indexes and message queues:

.. code-block:: console

    $ poetry run ./scripts/setup

Running
-------
Start the webserver and the celery worker:

.. code-block:: console

    $ poetry run ./scripts/server

At this time you can visit "https://127.0.0.1:5000"

Start a Python shell:

.. code-block:: console

    $ poetry run ./scripts/console

Upgrading
---------
In order to upgrade an existing instance simply run:

.. code-block:: console

    $ poetry run ./scripts/update

Testing
-------
Run the test suite via the provided script:

.. code-block:: console

    $ poetry run ./run-tests.sh

By default, end-to-end tests are skipped. You can include the E2E tests like
this:

.. code-block:: console

    $ env E2E=yes ./run-tests.sh

For more information about end-to-end testing see `pytest-invenio
<https://pytest-invenio.readthedocs.io/en/latest/usage.html#running-e2e-tests>`_

Documentation
-------------
You can build the documentation with:

.. code-block:: console

    $ poetry run build_sphinx

Production environment
----------------------
You can use simulate a full production environment using the
``docker-compose.full.yml``. You can start it like this:

.. code-block:: console

    $ ./docker/build-images.sh
    $ docker-compose -f docker-compose.full.yml up -d
    $ ./docker/wait-for-services.sh --full

Remember to create database tables, search indexes and message queues if not
already done:

.. code-block:: console

    $ docker-compose -f docker-compose.full.yml run --rm web-ui ./scripts/setup

In addition to the normal ``docker-compose.yml``, this one will start:

- HAProxy (load balancer) -- https://127.0.0.1 and http://127.0.0.1:8080
- Nginx (web frontend)
- UWSGI (application container)
- Celery (background task worker)
- Flower (Celery monitoring) -- http://127.0.0.1:5555
- Kibana (Elasticsearch inspection) -- http://127.0.0.1:5601
- RabbitMQ (message queue) -- http://guest:guest@127.0.0.1:15672
