=======
arctans
=======

arctans is a library for manipulating arctans to generate
[Machin-like formulae](https://machin-like.org) and other formulae involving arctans.

Installing arctans
==================

The latest release of arctans can be installed by running:

    pip3 install arctans

Alternatively, you can install the latest version directly from GitHub with::

    pip3 install git+https://github.com/mscroggs/arctans.git

Using arctans
=============

arctans can be used to represent arctans and sums of arctans symbolically
and generate arctan sums equivalent to a given set of sums.

For example, Machin's formula for pi (:math:`\pi = 16\arctan(1/5) - 4\arctan(1/239)`) can
be created with:

.. code-block:: python
    from arctans import arctan, Rational

    pi = 16 * arctan(Rational(1, 5)) - 4 * arctan(Rational(1, 239))
    print(pi)
    print(float(pi))

Or equivalently:

.. code-block:: python
    from arctans import arccotan

    pi = 16 * arccotan(5) - 4 * arccotan(239)
    print(pi)
    print(float(pi))

As arccotangents of integers commonly appear in formulae for pi, when printing
formulae represented using arctans, the shorthand notation `[n]` will be used
to represent `arccotan(n)`.

Once a formulae is expressed, new formulae that have the same value can be generated
using the `generate` function, for example:

.. code-block:: python
    from arctans import arccotan, generate

    pi = 16 * arccotan(5) - 4 * arccotan(239)

    formulae = generate([pi])

    for f in formulae:
        print(f)

This will print a number of different arctan sum formulae, including
`16*[4] + -16*[21] + -4*[239]` (ie :math:`\pi = 16\arctan(1/4) - 16\arctan(1/21) - 4\arctan(1/239)`).


Documentation index
===================

.. toctree::
   :titlesonly:

   demos/index
   docs/index
