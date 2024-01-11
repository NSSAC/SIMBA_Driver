from parsl.config import Config
from parsl.launchers import SrunLauncher
from parsl.providers import SlurmProvider
from parsl.executors import HighThroughputExecutor
from parsl.addresses import address_by_hostname
from parsl.data_provider.globus import GlobusStaging

from simbadriver.module import Module

class ParslModule(Module):
    
    def _init(self, data):
        launcher_debug = True
        launcher_override = ''

        if 'launcher' in data:
            if 'debug' in data['launcher']:
                launcher_debug = data['launcher']['debug']
            if 'override' in data['launcher']:
                launcher_override = data['launcher']['override']

        self.launcher = SrunLauncher(debug=launcher_debug, overrides=launcher_override)

        if not 'provider' in data:
            self.provider = SlurmProvider(launcher=self.launcher)
        else:
            pass

        if not 'executor' in data:
            self.executor = HighThroughputExecutor(provider=self.provider)
        else:
            pass

        return
        
    def _start(self, startTick, startTime):
        return True
        
    def _step(self, lastRunTick, lastRunTime, currentTick, currentTime, targetTick, targetTime):
        return True
        
    def _end(self, lastRunTick, lastRunTime, endTick, endTime):
        return True
        