*****************************
ABR Spatial Semantic Pointers
*****************************

This repository contains code of implementing spatial semantic pointers, or 
semantic pointers comprised of roles and fillers defined over continuous
spaces.

As the project as undergoing lots of development, things are currently organized
in a first-pass, preliminary fashion. Right now, ``maps.py`` is written to 
implement SSP classes for different kinds of metric spaces (currently only 2D
spaces are supported). The idea here is that while SSPs are semantic pointers,
the ``SemanticPointer`` class in ``nengo-spa`` doesn't really support the kinds of
queries and use cases this project is focused on. Having everything
encapsulated in classes for different types of spaces might not be the best 
design choice, so refactoring is welcome.

More generally, things are designed to enfore a fairly clear conceptual 
separation between SSP representations and the environments or spaces they
represent. Hence, there are methods for update SSPs from CoppeliaSim or from abstract
collections of environment objects. 


**Installation**
~~~~~~~~~~~~~~~~

More information coming soon. See ``setup.py`` for current requirements.

.. code-block:: bash
 
 conda create -n ssp python=3.7 numpy scipy
 conda activate ssp
 pip install -e .
 pip install git+https://github.com/nengo/nengo-spa.git@ssp


**Developer Notes**
~~~~~~~~~~~~~~~~~~~

Run ``pip install -e .[tests]`` to install the optional dependencies for
testing. Unit tests are invoked via ``py.test``.
