SIMBA Module API
================
**Contents:**

* |simba-module-introduction-synopsis|_
* |simba-module-specification-synopsis|_
* :ref:`simba-module-examples`

.. |simba-module-introduction-synopsis| replace:: SIMBA module API is the interface the SIMBA driver calls and interacts with the modules executable.
.. _`simba-module-introduction-synopsis`: `simba-module-introduction`_

.. _simba-module-introduction:

Introduction
------------

.. admonition:: Synopsis

   |simba-module-introduction-synopsis|

The :doc:`driver` calls each module at the ``start`` and ``end`` of the simulation as well as for each ``step``, for which the module is scheduled. A module is expected to be an executable callable from the command line. The module is called with just one positional argument, which is the path to a JSON formatted config file. Each module is expected provide a :ref:`module-status` file returning the modules success state. It may also provide information back to the driver. This information comprises module specific data and common data. The later is shared with all modules but only trusted modules may update it. The returned information must be provided in a JSON files alongside the config file.

.. |simba-module-specification-synopsis| replace:: Specification: The API for a modules comprising configuration and return status. 
.. _`simba-module-specification-synopsis`: `simba-module-specification`_

.. _simba-module-specification:

Specification
-------------

.. admonition:: Synopsis

   |simba-module-specification-synopsis|

The API for a SIMBA module comprises two files the configuration and return status files. The JSON configuration file may contain 3 sections, which are: :ref:`driver-provided-data`, :ref:`common-data`, and :ref:`module-specific-data`.  In case the module updates common or module specific data this must be done in a file alongside the configuration file, i.e., in the same directory. The file should contain the JSON objects ``commonData``, ``moduleData``, or both. 

.. _driver-provided-data:

Driver provided Data
....................

This data provides information about the situation in which the module is called by the driver. The module will be called with 3 modes which are: ``start``, ``step``, and ``end``. The normative JSON schema can be found at:  :doc:`Module Config Schema </schema/module>` 


**start:** The module is expected to initialize itself and the state of the system for the given `currentTick` and `currentTime`

.. list-table:: Start Information. 
  :name: module-mode-start
  :header-rows: 1

  * - | Name
    - | Type 
    - | Description
  * - | mode
    - | const ``start`` 
    - | The modules is called in mode start.
  * - | statusFile
    - | string 
    - | The file containing status, updated common, and module data.
  * - | currentTick
    - | integer
    - | The current (initial) tick
  * - | currentTime
    - | string
    - | The current (initial) time (ISO data time format)

**step:** The module is expected to progress the systems state from the `lastRunTime` to the `targetTime`. The `currentTime` is provided since the time increments may not be uniform (see: :doc:`driver`)

.. list-table:: Step Information. 
  :name: module-mode-step
  :header-rows: 1

  * - | Name
    - | Type 
    - | Description
  * - | mode
    - | const ``step`` 
    - | The modules is called in mode step.
  * - | statusFile
    - | string 
    - | The file containing status, updated common, and module data.
  * - | lastRunTick
    - | integer
    - | The tick the module was last executed
  * - | lastRunTime
    - | string
    - | The time the module was last executed (ISO data time format)
  * - | currentTick
    - | integer
    - | The current tick
  * - | currentTime
    - | string
    - | The current time (ISO data time format)
  * - | targetTick
    - | integer
    - | The target tick
  * - | targetTime
    - | string
    - | The target time (ISO data time format)

**end:** The module is expected to progress the systems state from the `lastRunTime` to the `currentTime` if that is appropriate. Furthermore, it is expected that it does complete all required shutdown procedures

.. list-table:: End Information. 
  :name: module-mode-end
  :header-rows: 1

  * - | Name
    - | Type 
    - | Description
  * - | mode
    - | const ``end`` 
    - | The modules is called in mode end.
  * - | statusFile
    - | string 
    - | The file containing status, updated common, and module data.
  * - | lastRunTick
    - | integer
    - | The tick the module was last executed
  * - | lastRunTime
    - | string
    - | The time the module was last executed (ISO data time format)
  * - | currentTick
    - | integer
    - | The current tick
  * - | currentTime
    - | string
    - | The current time (ISO data time format)


.. _common-data:

Common Data
...........

Common data, e.g., database connection information is provided to all modules. Since the host on which the database may not be know before the start of the driver it is necessary that the module providing the database returns the information to the driver and all modules. The attributes of the common data or provided as part of the :doc:`schedule`. No further information will be made available the modules.

.. list-table:: Module Common Data. 
  :name: module-common-data
  :header-rows: 1

  * - | Name
    - | Type 
    - | Description
  * - | commonData
    - | object 
    - | Common data provided to all modules.

As an example if the following is provided in the schedule file:

.. code-block:: JSON

   "commonData": {
    "dbHost": null
  }

The following should be contained in the status file from the module providing the database host:

.. code-block:: JSON

   "commonData": {
    "dbHost": "128.1.1.223"
  }


.. _module-specific-data:

Module Specific Data
....................

A module may require additional configuration options beyond the driver provided information and common data. The module specific data object is providing the means to define and modify it.

.. list-table:: Module Specific Data. 
  :name: table-module-specific-data
  :header-rows: 1

  * - | Name
    - | Type 
    - | Description
  * - | moduleData
    - | object 
    - | Module specific data.

.. _module-status:

Module Status
.............

As a minimum the status file contains the return status: ``success`` or ``fail``. In case the module updates common or module specific data the file should also contain the JSON objects ``commonData``, ``moduleData``, or both. The normative JSON schema can be found at:  :doc:`Module Status Schema </schema/status>` 

.. list-table:: Module Status. 
  :name: table-module-status
  :header-rows: 1

  * - | Name
    - | Type 
    - | Description
  * - | status
    - | string 
    - | The return status: ``success`` or ``fail``.
  * - | commonData
    - | object 
    - | Updated common data provided to all modules.
  * - | moduleData
    - | object
    - | Updated module specific data.

.. _simba-module-examples:

Examples
--------

Please see :doc:`Examples </examples/example>` 