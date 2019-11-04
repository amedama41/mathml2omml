math2omml
=========

Pure Python library to convert MathML to OMML (Office Math Markup Language).

Installation
------------

Use pip:

.. code:: sh

   pip install mathml2omml

or, use setup.py:

.. code:: sh

   python3 setup.py install

Usage
-----

Mathml2omml takes a MathML as string, and outputs an OMML as string:

.. code:: python

   import mathml2omml

   mathml = '<math><mi>x</mi><mo>+</mo><mi>y</mi></math>'
   omml = math2omml.convert(mathml)

By default, mathml2omml recognises only entities defined in MathML specification.
If the input includes other entities, pass the entity information
as a dictionary to the second argument:

.. code:: python

   mathml = '<math><msubsup><mo>&int;</mo><mn>1</mn><mi>x</mi></msubsup></math>'
   omml = math2omml.convert(mathml, {'int': '&#x222B;'})
