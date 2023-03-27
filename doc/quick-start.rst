Quick Start
===========


.. note::
   **miniconda disclaimer**

   This documentations assumes you use `miniconda <https://docs.conda.io/en/latest/miniconda.html>`_
   to setup and manage virtual environments. You obviously don't have to use it, but in the interest
   of brevity, this doc will assume you do.



Only reproduce research results
-------------------------------

If you only want to reproduce our `research results <research-results.html>`_, you don't even need to
``git clone`` our `repository <https://github.com/master-ai-batch5/M05-mp-decaillet>`_:

#. Setup a python v3.11:   

   .. code:: bash

      conda create -n run-m05-mp-decaillet python=3.11
      conda activate run-m05-mp-decaillet

#. Install package from `test pypi <https://test.pypi.org/project/decm05/>`_:

   .. code:: bash

      pip install --extra-index-url https://test.pypi.org/simple decm05

#. Run the package:

   .. code:: bash

      run_decm05         # reproduce research results
      run_decm05 --help  # show help menu

Note that you won't be able to examine/modify our code, [run automated tests](automated-tests.rst),
as well as a few other things.

If you want to dive deeper, please keep reading.



Full installation
-----------------

#. Clone our `repository <https://github.com/master-ai-batch5/M05-mp-decaillet>`_:
   
   .. code:: bash

      git clone https://github.com/master-ai-batch5/M05-mp-decaillet.git
      cd M05-mp-decaillet

#. Create a virtual environment:

   .. code:: bash

      conda env create -f environment.yml

#. Activate your virtual environment:

   .. code:: bash

      conda activate m05-mp-decaillet

#. Run **main.py**

   .. code:: bash

      python main.py         # reproduce research results
      python main.py --help  # show help menu

#. (optional) Install the package as editable, to define alias ``run_decm05``

   .. code:: bash

      pip install -e .   # install the package as editable
      run_decm05         # use the new alias
      run_decm05 --help  # show help menu
