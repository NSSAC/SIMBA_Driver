# BEGIN: Copyright 
# Copyright (C) 2024 Rector and Visitors of the University of Virginia 
# All rights reserved 
# END: Copyright 

# BEGIN: License 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
#   http://www.apache.org/licenses/LICENSE-2.0 
# END: License 

from pathlib import Path
from subprocess import run

from simbadriver.module import Module

class LocalModule(Module):
    def _init(self, data):
        return True

    def execute(self, stdout, stderr):
        run(args=self.command + ' ' + self.config, shell=True, stdout=open(stdout, 'w'), stderr=open(stderr, 'w'))
        return  
      
    def _start(self, currentDirectory, startTick, startTime):
        stdout = str(currentDirectory.joinpath('stdout_{}'.format(self.index)))
        stderr = str(currentDirectory.joinpath('stderr_{}'.format(self.index)))
                   
        self.execute(stdout, stderr)
        return True

        
    def _step(self, currentDirectory, lastRunTick, lastRunTime, currentTick, currentTime, targetTick, targetTime):
        stdout = str(currentDirectory.joinpath('stdout_{}'.format(self.index)))
        stderr = str(currentDirectory.joinpath('stderr_{}'.format(self.index)))
                   
        self.execute(stdout, stderr)
        return True
        
    def _end(self, currentDirectory, lastRunTick, lastRunTime, endTick, endTime):
        stdout = str(currentDirectory.joinpath('stdout_{}'.format(self.index)))
        stderr = str(currentDirectory.joinpath('stderr_{}'.format(self.index)))
                   
        self.execute(stdout, stderr)
        return True
