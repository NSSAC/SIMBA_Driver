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
        return

    def execute(self, stdout, stderr):
        run(args=self.command + ' ' + self.config, shell=True, stdout=open(stdout, 'w'), stderr=open(stderr, 'w'))
        return  
      
    def _start(self, startTick, startTime):
        mode = 'start'
        stdout = str(Path.cwd().joinpath(mode, 'stdout_{}'.format(self.index)))
        stderr = str(Path.cwd().joinpath(mode, 'stderr_{}'.format(self.index)))
                   
        self.execute(stdout, stderr)
        return True

        
    def _step(self, lastRunTick, lastRunTime, currentTick, currentTime, targetTick, targetTime):
        mode = self.SIMBA.formatTick(currentTick)
        stdout = str(Path.cwd().joinpath(mode, 'stdout_{}'.format(self.index)))
        stderr = str(Path.cwd().joinpath(mode, 'stderr_{}'.format(self.index)))
                   
        self.execute(stdout, stderr)
        return True
        
    def _end(self, lastRunTick, lastRunTime, endTick, endTime):
        mode = 'end'
        stdout = str(Path.cwd().joinpath(mode, 'stdout_{}'.format(self.index)))
        stderr = str(Path.cwd().joinpath(mode, 'stderr_{}'.format(self.index)))
                   
        self.execute(stdout, stderr)
        return True
