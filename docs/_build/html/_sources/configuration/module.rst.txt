SIMBA Module
============
**Contents:**

* |simba-module-introduction-synopsis|_
* |simba-module-specification-synopsis|_
* :ref:`simba-module-examples`

.. |simba-module-introduction-synopsis| replace:: SIMBA module runtime configuration.
.. _`simba-module-introduction-synopsis`: `simba-module-introduction`_

.. _simba-module-introduction:

Introduction
------------

.. admonition:: Synopsis

   |simba-module-introduction-synopsis|

The SIMBA module configuration specifies the configuration file provided to each module at run time

.. |simba-module-specification-synopsis| replace:: Specification: run time configuration file for a module. 
.. _`simba-module-specification-synopsis`: `simba-module-specification`_

.. _simba-module-specification:

Specification
-------------

.. admonition:: Synopsis

   |simba-module-specification-synopsis|

The normative JSON schema can be found at:  :doc:`Module Schema </schema/module>` 

.. _simba-module-examples:

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
        "timePerTick" :  "PT600S"
      },
      {
        "endTick" : 100,
        "timePerTick" :  "PT1800S"
      },
      {
        "timePerTick" :  "PT3600S"
      }
    ]
  }

