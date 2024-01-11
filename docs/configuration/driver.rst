SIMBA Driver
============
**Contents:**

* |simba-driver-introduction-synopsis|_
* |simba-driver-specification-synopsis|_
* :ref:`simba-driver-examples`

.. |simba-driver-introduction-synopsis| replace:: SIMBA driver configuration.
.. _`simba-driver-introduction-synopsis`: `simba-driver-introduction`_

.. _simba-driver-introduction:

Introduction
------------

.. admonition:: Synopsis

   |simba-driver-introduction-synopsis|

The SIMBA driver configuration specifies the run parameters of a the simulation

.. |simba-driver-specification-synopsis| replace:: Specification: how to specify the simulation parameters. 
.. _`simba-driver-specification-synopsis`: `simba-driver-specification`_

.. _simba-driver-specification:

Specification
-------------

.. admonition:: Synopsis

   |simba-driver-specification-synopsis|

The normative JSON schema can be found at:  :doc:`Driver Schema </schema/driver>` 

.. _simba-driver-examples:

Examples
--------

Example using a different simulation duration time for ticks.

.. code-block:: JSON

  {
    "$schema": "https://raw.githubusercontent.com/NSSAC/SIMBA_driver/schema/driver.json",
    "endTime" : "PT1209600S",
    "scheduleIntervals" : [
      {
        "endTick" : 6,
        "tickDuration" :  "PT600S"
      },
      {
        "endTick" : 100,
        "tickDuration" :  "PT1800S"
      },
      {
        "tickDuration" :  "PT3600S"
      }
    ]
  }

