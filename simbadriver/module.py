from pathlib import Path
from abc import ABCMeta, abstractmethod

class Module():
    __metaclass__ = ABCMeta
    
    def __init__(self, SIMBA, scheduler, data):
        self.SIMBA = SIMBA
        self.scheduler = scheduler
        
        self.data = {}
        self.name = data['name']
        self.index = data['index']
        self.command = self.SIMBA.getConfiguration().resolveCmd(data['command'])
        
        if 'updateCommonData' in data:
            self.updateCommonData = data['updateCommonData']
        else:
            self.updateCommonData = False
            
        if "moduleData" in data:
            self.moduleData = data['moduleData']
        else :
            self.moduleData = None

        self.__lastRunTick = None
        self.__lastRunTime = None
    
        self._init(data)
        
    @abstractmethod   
    def _init(self, data):
        return False
    
    def start(self, startTick, startTime):
        self.__lastRunTick = startTick
        self.__lastRunTime = startTime
        self.config = Path.cwd().joinpath('start', 'module_' + str(self.index) + '.json')
        
        
        moduleConfig = self.scheduler.initConfigData()
        moduleConfig['mode'] = 'start'
        moduleConfig['targetTick'] = startTick
        moduleConfig['targetTime'] = startTime.isoformat()
        
        if self.moduleData != None:
            moduleConfig['moduleData'] = self.moduleData

        self.SIMBA.getConfiguration().writeJsonFile(self.config, moduleConfig)
        success = self._start(startTick, startTime)
        if success:
            self.updateData()
        
        return success
        
    @abstractmethod   
    def _start(self, startTick, startTime):
        return False
        
    def step(self, currentTick, currentTime, deltaTick, deltaTime, skipExecution):
        success = True
        self.config = Path.cwd().joinpath(str(currentTick), 'module_' + str(self.index) + '.json')
        
        moduleConfig = self.scheduler.initConfigData()
        moduleConfig['mode'] = 'step'
        moduleConfig['lastRunTick'] = self.__lastRunTick
        moduleConfig['lastRunTime'] = self.__lastRunTime.isoformat()
        moduleConfig['currentTick'] = currentTick
        moduleConfig['currentTime'] = currentTime.isoformat()
        moduleConfig['targetTick'] = currentTick + deltaTick
        moduleConfig['targetTime'] = (currentTime + deltaTime).isoformat()
        
        if self.moduleData != None:
            moduleConfig['moduleData'] = self.moduleData

        self.SIMBA.getConfiguration().writeJsonFile(self.config, moduleConfig)
        
        if not skipExecution:
            success = self._step(self.__lastRunTick, self.__lastRunTime, currentTick, currentTime, currentTick + deltaTick, currentTime + deltaTime)
            if success:
                self.updateData()
        
        self.__lastRunTick = currentTick
        self.__lastRunTime = currentTime
        
        return success 

    @abstractmethod   
    def _step(self, lastRunTick, lastRunTime, currentTick, currentTime, targetTick, targetTime):
        return False
        
    def end(self, endTick, endTime):
        self.config = Path.cwd().joinpath('end', 'module_' + str(self.index) + '.json')
        
        moduleConfig = self.scheduler.initConfigData()
        moduleConfig['mode'] = 'end'
        moduleConfig['targetTick'] = endTick
        moduleConfig['targetTime'] = endTime.isoformat()
        
        if self.moduleData != None:
            moduleConfig['moduleData'] = self.moduleData

        self.SIMBA.getConfiguration().writeJsonFile(self.config, moduleConfig)
        
        success = self._end(self.__lastRunTick, self.__lastRunTime, endTick, endTime)
        
        if success:
            self.updateData()

        self.__lastRunTick = None
        self.__lastRunTime = None
        
        return success 

    @abstractmethod   
    def _end(self, lastRunTick, lastRunTime, endTick, endTime):
        return False

    def updateData(self):
        config = self.SIMBA.getConfiguration().loadJsonFile(self.config)
        
        if 'moduleData' in config:
            self.moduleData = config['moduleData']
            
        if self.updateCommonData and 'commonData' in config:
            self.scheduler.updateCommonData(config['commonData'])