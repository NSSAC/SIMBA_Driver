Examples
========

Before running either of the examples you will have to install :doc:`SIMBA </quickstart/get-started>`.
Both examples use a simple ``bash`` script to demonstrate the functionality.

**application.sh**:

.. literalinclude:: ../../examples/bin/application.sh
   :language: bash


Local Example
-------------

This example can be executed without customization on any computer. To run this example execute:

.. code-block:: bash

  examples/local/SIMBA.sh

It consist of two configuration files:

**driver.json**:

.. literalinclude:: ../../examples/local/driver.json
   :language: JSON

**schedule.json**:

.. literalinclude:: ../../examples/local/schedule.json
   :language: JSON


Slurm Example
-------------

In order to execute this example the slurm ``account``, ``qos``, and ``partition`` must be adjusted in schedule.json and SIMBA.sbatch. After the adjustment please execute the example with:

.. code-block:: bash

  examples/local/SIMBA.sh

**driver.json**:

.. literalinclude:: ../../examples/slurm/driver.json
   :language: JSON

**schedule.json**:

.. literalinclude:: ../../examples/slurm/schedule.json
   :language: JSON

**SIMBA.sbatch**:

.. literalinclude:: ../../examples/slurm/SIMBA.sbatch
   :language: bash


