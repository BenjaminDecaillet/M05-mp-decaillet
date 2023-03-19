Automated tests
===============

This project features the following automated testings mechanisms.

`GitHub actions <https://github.com/master-ai-batch5/M05-mp-decaillet/actions/workflows/main.yml>`_ will ensure that the tests pass.

Unit tests
----------

Unit tests are located in folder  **unit_tests**

Run unit-tests as follows:

.. code:: bash

    workon m05-mp-decaillet  # activate your virtualenv if necessary
    python -m unittest discover -v

Coverage
~~~~~~~~

Run unit tests, run coverage and display coverage report:

.. code:: bash

    workon m05-mp-decaillet  # activate your virtualenv if necessary
    coverage run --source=src -m unittest -v
    coverage report -m


`GitHub actions <https://github.com/master-ai-batch5/M05-mp-decaillet/actions/workflows/main.yml>`_ will enforce unit-test coverage of 100%.


e2e tests
---------

e2e tests located in file **.github/workflows/e2e.sh**

Run e2e tests as follows:

.. code:: bash

    workon m05-mp-decaillet  # activate your virtualenv if necessary
    .github/workflows/e2e.sh

