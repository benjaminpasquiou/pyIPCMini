.. pyIPCMini documentation master file, created by
   sphinx-quickstart on Sun Jul  7 18:13:28 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyIPCMini's documentation!
=====================================
pyIPCMini is a package to communicate and control via USB/serial the ion pump controller type IPCMini from Agilent.

It has been tested using the RS232 protocol, with the pump's DB9 connector hooked to a USB-serial converter based on FTDI chip.

This is an unofficial package for the `IPCMini <https://www.agilent.com/en/product/vacuum-technologies/ion-pumps-controllers/ion-pump-controllers/ipcmini-ion-pump-controller>`_ and it is not supported by the equipment's vendor.

Installation
------------
You can install this package from PyPI, using the following command:

    pip install pyIPCMini

Alternatively, you can clone the latest version from github:

    git clone ``https://github.com/benjaminpasquiou/pyIPCMini.git``

This package relies on the pyserial package for the actual communication with the hardware. Check it out on `PyPI <https://pypi.org/project/pyserial>`_.

Warning
-------
An ion pump is a sensitive device, and if not used properly it can potentially cause harm to the user, to the device itself, or to other pieces of equipment. This package should only be used by trained operators. Please read Agilent IPCMini's manual and make sure that you can safely operate the pump in manual mode, before using the package for remote control. Please also consult this package documentation before using any of its functionalities.


Examples
========
.. toctree::
    :maxdepth: 2

    notebooks/Examples


Reference manual
================

.. toctree::
   :maxdepth: 4

   pyipcmini



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
