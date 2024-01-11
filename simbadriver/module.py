from abc import ABCMeta, abstractmethod

class Module():
    __metaclass__ = ABCMeta
    
    def __init__(self, SIMBA, data):
        self.SIMBA = SIMBA
        self.data = {}
        self.data['name'] = data['name']
        self.data['command'] = data['command']
        if not "moduleData" in data:
            self.data["moduleData"] = None
        else :
            self.data["moduleData"] = data['moduleData']

        self.__lastRunTick = None
        self.__lastRunTime = None
    
        self._init(data)
        
    @abstractmethod   
    def _init(self, data):
        return False
    
    def start(self, startTick, startTime):
        self.__lastRunTick = startTick
        self.__lastRunTime = startTime
        
        return self._start(startTick, startTime)
        
    @abstractmethod   
    def _start(self, startTick, startTime):
        return False
        
    def step(self, currentTick, currentTime, deltaTick, deltaTime, skipExecution):
        success = True
        
        if not skipExecution:
            success = self._step(self.__lastRunTick, self.__lastRunTime, currentTick, currentTime, currentTick + deltaTick, currentTime + deltaTime)
        
        self.__lastRunTick = currentTick
        self.__lastRunTime = currentTime
        
        return success 

    @abstractmethod   
    def _step(self, lastRunTick, lastRunTime, currentTick, currentTime, targetTick, targetTime):
        return False
        
    def end(self, endTick, endTime):
        
        success = self._end(self.__lastRunTick, self.__lastRunTime, endTick, endTime)
        
        self.__lastRunTick = None
        self.__lastRunTime = None
        
        return success 

    @abstractmethod   
    def _end(self, lastRunTick, lastRunTime, endTick, endTime):
        return False
