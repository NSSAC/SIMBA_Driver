[![Documentation Status](https://readthedocs.org/projects/simba-driver/badge/?version=latest)](https://simba-driver.readthedocs.io/en/latest/?badge=latest)

# SIMBA Driver

SIMBA is a framework for performing multi-scale simulations in an HPC environment. Each simulation step can involve multiple modules which update the current state of the system. The order and the frequency in which these modules are executed is handled by a flexible [scheduler](https://simba-driver.readthedocs.io/en/latest/configuration/schedule.html).

## Obtain Code

```
git clone https://github.com/NSSAC/SIMBA_driver.git
```

__Development Mode__: To install all requirements and execute SIMBA directly from the source code. Please execute in the top code directory: 
```
pip install -e .
```

## Install

### Linux and MacOS X
__System wide installation__
``` sh
sudo pip install simbaDriver
```

__User local installation__
``` sh
pip install simbaDriver --user
```

### Windows
__System installation__ [(Instructions on how to run a console as administrator)](https://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-8.1/)
``` sh
pip install simbaDriver
```

__User local installation__ (not recommeded as the script path is not in the search PATH)
``` sh
pip install simbaDriver --user
```

