SIMBA Schedule
==============
**Contents:**

* |simba-schedule-introduction-synopsis|_
* |simba-schedule-specification-synopsis|_
* :ref:`simba-schedule-examples`

.. |simba-schedule-introduction-synopsis| replace:: SIMBA schedule configuration.
.. _`simba-schedule-introduction-synopsis`: `simba-schedule-introduction`_

.. _simba-schedule-introduction:

Introduction
------------

.. admonition:: Synopsis

   |simba-schedule-introduction-synopsis|

The SIMBA schedule comprises modules, which are flexibly scheduled at certain ticks (time points) during a simulation. Furthermore each module has fine grained options on how to execute the module. The later utilizes `parsl <https://parsl.readthedocs.io/en/stable/index.html>`_ allowing SIMBA to execute the modules on different computing resources.

.. |simba-schedule-specification-synopsis| replace:: Specification: how to specify module schedules. 
.. _`simba-schedule-specification-synopsis`: `simba-schedule-specification`_

.. _simba-schedule-specification:

Specification
-------------

.. admonition:: Synopsis

   |simba-schedule-specification-synopsis|

The schedule JSON configuration file has two attributes: ``schedule`` and ``commonData``. 

.. list-table:: Schedule.
  :name: schedule-schedule
  :header-rows: 1

  * - | Name
    - | Type 
    - | Description
  * - | schedule
    - | array 
    - | items consist of all of: 
      | :ref:`schedule-module-details`
      | :ref:`schedule-module-schedule`
      | `Parsl Module. <../schema/schedule.html#parsl-module>`_
  * - | commonData
    - | object 
    - | Common data provided to all modules upon execution (default: none)

.. list-table:: Module Identification and Details.
  :name: schedule-module-details
  :header-rows: 1

  * - | Name
    - | Type 
    - | Description
  * - | name
    - | string 
    - | The name of the module.
  * - | command
    - | string 
    - | The command to execute the module.
  * - | updateCommonData
    - | Boolean
    - | Specifies whether this module may update common data 
      | (default: false)
  * - | moduleData
    - | object
    - | Module specific data provided to the module upon execution 
      | (default: none)

.. list-table:: Module Schedule. 
  :name: schedule-module-schedule
  :header-rows: 1

  * - | Name
    - | Type 
    - | Description
  * - | priority
    - | number 
    - | Priority of Module Execution, higher priority is executed first and  
      | priorities must be unique.
  * - | startTick
    - | string 
    - | The current tick at which the module is executed first
      | (default: -infinity).
  * - | endTick
    - | integer
    - | The targetTick for which the module is executed last
      | (default: infinity).
  * - | tickIncrement
    - | positive integer
    - | The tick increment in which the module is executed (default: 1).


The normative JSON schema can be found at:  :doc:`Schedule Schema </schema/schedule>` 

.. _simba-schedule-examples:

Examples
--------

Please see :doc:`Examples </examples/example>` 