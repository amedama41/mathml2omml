math2omml
=========

Pure Python library to convert MathML to OMML (Office Math Markup Language).

Usage:

.. code:: python

   import mathml2omml

   mathml = '<math><mi>x</mi><mo>+</mo><mi>y</mi></math>'
   omml = math2omml.convert(mathml)

