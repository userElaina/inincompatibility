inincompatibility
=================

A dependency-free, code-less ``socket``-based solution for resolving
(**Python** / **conda**) environment incompatibilities.

Usage Guidelines
----------------

**Installation**:

To install the ``inincompatibility`` package, run:

.. code:: shell

   pip install inincompatibility

**Example: Making Your LLMs Callable Like an API**:

First, make your LLMs callable functions and ``import`` them into a
``.py`` file, like so:

.. code:: python

   # LLM_functions.py
   from your_LLM import your_forward, your_backward

Next, use the ``inincompatibility`` package to run the LLM in its
(**Python** / **conda**) environment and generate the necessary
importable code:

.. code:: shell

   python -m inincompatibility -i LLM_functions.py -o api_for_other.py

Now, you can directly ``import`` the generated code in another
(**Python** / **conda**) environment:

.. code:: python

   # your_other_code.py
   from api_for_other import your_forward, your_backward

**Example: Additional Samples**:

For more usage examples, check out the
`sample1 <https://github.com/userElaina/inincompatibility/tree/main/sample1>`__
directory on
`GitHub <https://github.com/userElaina/inincompatibility>`__.
