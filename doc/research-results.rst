Research results
================

.. note::
   This is a toy project to exercise reproducible research; research-wise, these results are pretty boring.


This project will apply various machine learning techniques to the following datasets:

* Wine Quality (see `winequality.names <https://github.com/master-ai-batch5/M05-mp-decaillet/blob/main/data/housing.names>`_)
* Boston House Prices (see `housing.names <https://github.com/master-ai-batch5/M05-mp-decaillet/blob/main/data/housing.names>`_)

The results of the analysis are shown below.

Wine Quality
------------

.. testcode::

   from decm05 import Service
   Service(["--dataset=wines", "--seed=42"]).run()

.. testoutput::

    dataset preprocessor         estimator  evaluation count  MEAN ABSOLUTE ERROR
      wines      min-max linear-regression                 3               0.5695
      wines      min-max     decision-tree                 3               0.5800
      wines     standard linear-regression                 3               0.5729
      wines     standard     decision-tree                 3               0.5850
      wines   polynomial linear-regression                 3               0.5582
      wines   polynomial     decision-tree                 3               0.5790



Boston House Prices
-------------------

.. testcode::

   from decm05 import Service
   Service(["--dataset=boston", "--seed=42"]).run()

.. testoutput::

    dataset preprocessor         estimator  evaluation count  MEAN ABSOLUTE ERROR
     boston      min-max linear-regression                 3               3.4924
     boston      min-max     decision-tree                 3               2.7763
     boston     standard linear-regression                 3               3.4944
     boston     standard     decision-tree                 3               3.1092
     boston   polynomial linear-regression                 3               5.0997
     boston   polynomial     decision-tree                 3               2.9869
