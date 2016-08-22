sublime-core-tests
==================

.. image:: https://travis-ci.org/twolfson/sublime-core-tests.svg?branch=master
   :target: https://travis-ci.org/twolfson/sublime-core-tests
   :alt: Build Status

Modest test suite to verify `Sublime Text`_ functionality

This was built to verify API closeness for clones of `Sublime Text`_ (e.g. `suplemon`_)

.. _`Sublime Text`: http://www.sublimetext.com/
.. _`suplemon`: https://github.com/richrd/suplemon

Getting Started
---------------
To run the test suite in a local copy of Sublime Text, run the following:

.. code:: bash

    # Clone our repository
    git clone https://github.com/twolfson/sublime-core-tests
    cd sublime-core-tests

    # Install our repository as a package so UnitTesting can find it
    ln -s "$PWD" ~/.config/sublime-text-3/Packages/sublime-core-tests

    # Launch Sublime Text in the local folder
    subl .

    # By hand: Run our tests via UnitTesting
    #   Command Palette -> UnitTesting: Test Current project

Documentation
-------------
_(Coming soon)_

Contributing
------------
In lieu of a formal styleguide, take care to maintain the existing coding style. Add unit tests for any new or changed functionality. Test via ``nosetests``.

Donating
--------
Support this project and `others by twolfson`_ via `gratipay`_.

.. image:: https://cdn.rawgit.com/gratipay/gratipay-badge/2.x.x/dist/gratipay.svg
   :target: `gratipay`_
   :alt: Support via Gratipay

.. _`others by twolfson`:
.. _gratipay: https://www.gratipay.com/twolfson/

Unlicense
---------
As of Aug 22 2016, Todd Wolfson has released this repository and its contents to the public domain.

It has been released under the `UNLICENSE`_.

.. _UNLICENSE: https://github.com/twolfson/sublime-core-tests/blob/master/UNLICENSE
