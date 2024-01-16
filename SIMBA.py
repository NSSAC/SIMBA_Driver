#!/usr/bin/env python

import argparse
from simbadriver.simbadriver import SIMBA

parser = argparse.ArgumentParser(description="SIMBA multi-scale simulation framework.")
parser.add_argument("directory", nargs=1, help='The directory where configuration files are located.')

arguments = parser.parse_args()
SIMBA(arguments.directory[0]).run()

exit
