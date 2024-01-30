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

The SIMBA driver executes each simulation step based on the given information. Required information comprises: ``initialTime``, ``endTime``, and a ``schedule`` containing at least one interval.


.. list-table:: Driver Specification. 
  :name: driver-specification
  :header-rows: 1

  * - | Name
    - | Type 
    - | Description
  * - | runId
    - | string 
    - | A unique ID identifying the run to be executed.
  * - | cellId
    - | string 
    - | A ID identifying the currently running experimental setup.
  * - | initialTick
    - | integer
    - | The initial tick. Default: 0
  * - | initialTime
    - | string
    - | The initial time (ISO data time format)
  * - | endTime
    - | string
    - | The simulation stops once ``initialTime`` plus all accumulated 
      | durations (``tickDuration``) exceeds the endTime
  * - | continueFromTick
    - | string
    - | This attribute allows to continue a previously executed simulation 
      | at the given tick
  * - | scheduleIntervals
    - | array
    - | The intervals are executed in the listed order and must not overlap. 
      | At least one interval must be defined.


The intervals in the schedule are executed in order. This implies that the ``endTick`` attributes must be increasing. The only required attribute is ``tickDuration``.

.. list-table:: Schedule Interval. 
  :name: driver-schedule-interval
  :header-rows: 1

  * - | Name
    - | Type 
    - | Description
  * - | startTick
    - | integer 
    - | Start tick of the interval. Default: ``initialTick`` or previous ``endTick + 1``
  * - | endTick
    - | string 
    - | End tick of the interval. Default: infinity
  * - | tickDuration
    - | string
    - | Time duration per tick of the interval (ISO duration format rfc3339)

The normative JSON schema can be found at:  :doc:`Driver Schema </schema/driver>` 

.. _simba-driver-examples:

Examples
--------

Example using a 3 intervals with different simulation duration times.

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

