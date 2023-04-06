Architecture
============

In this mini-project, we will build an extensible and fully reproducible system
to analyze multiple datasets, with various Machine Learning techniques.


Functional Overview
-------------------
The system is a straightforward machine learning pipeline: it takes a dataset,
trains a model and evaluates its `Mean Absolute Error (MAE) <https://en.wikipedia.org/wiki/Mean_absolute_error>`_.

.. image:: img/functional-overview.png   
   :alt: functional overview


Evaluator
---------
The `Evaluator <apidoc/decm05.evaluator.html#decm05.evaluator.Evaluator>`_
is an orchestrator that takes
a `Preparator <apidoc/decm05.preparator.contract.html#decm05.preparator.contract.Preparator>`_,
a `Preprocessor <apidoc/decm05.preprocessing.contract.html#decm05.preprocessing.contract.Preprocessor>`_
and an `Estimator <apidoc/decm05.estimating.contract.html#decm05.estimating.contract.Estimator>`_
and returns their `MAE <https://en.wikipedia.org/wiki/Mean_absolute_error>`_.

.. image:: img/evaluator.png   
   :alt: evaluator

It has the advantage of being easily customizable, as the `injected dependencies <https://en.wikipedia.org/wiki/Dependency_injection>`_
(aka the "blue blocks") can be easily swapped.
However, it can be somewhat complex to initialize.

Service
-------

To help with the initialization of the `Evaluator`, we provide a `Service <apidoc/decm05.service.html#decm05.service.Service>`_, that is
extremely easy to use (``Service().run()``) and can be used as an entry point.

Behind the scenes, `Service <apidoc/decm05.service.html#decm05.service.Service>`_ ensures the initialization of
an  `Evaluator <apidoc/decm05.evaluator.html#decm05.evaluator.Evaluator>`_, via `factories <https://en.wikipedia.org/wiki/Factory_method_pattern>`_ 

.. image:: img/service.png   
   :alt: service

NB: the above diagram shows the interactions of the following classes:

- `ArgParser <apidoc/decm05.arg_parser.html#decm05.arg_parser.ArgParser>`_
- `PreparatorFactory <apidoc/decm05.preparator.factory.html#decm05.preparator.factory.PreparatorFactory>`_
- `EstimatorFactory <apidoc/decm05.estimating.factory.html#decm05.estimating.factory.EstimatorFactory>`_
- `PreprocessorFactory <apidoc/decm05.preprocessing.factory.html#decm05.preprocessing.factory.PreprocessorFactory>`_
