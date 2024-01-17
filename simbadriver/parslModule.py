from parsl.config import Config
from parsl.launchers import SrunLauncher
from parsl.channels import LocalChannel
from parsl.providers import SlurmProvider
from parsl.executors import HighThroughputExecutor
from parsl.addresses import address_by_hostname
from parsl.data_provider.globus import GlobusStaging
from parsl.app.app import bash_app

import parsl

from simbadriver.module import Module

@bash_app
def srunCommand(command, config, stdout = 'module.stdout', stderr = 'module.stderr'):
    return command + ' ' + config

class ParslModule(Module):
    def _init(self, data):
        self.launcher = {
            'debug': True,
            'overrides': ''
            }

        if 'launcher' in data:
            if 'debug' in data['launcher']:
                self.launcher['debug'] = data['launcher']['debug']
            if 'overrides' in data['launcher']:
                self.launcher['overrides'] = data['launcher']['overrides']

        self.provider = {
            'partition': None,
            'account': None,
            'qos': None,
            'constraint': None,
            'channel': LocalChannel(),
            'nodes_per_block': 1,
            'cores_per_node': None,
            'mem_per_node': None,
            'init_blocks': 1 ,
            'min_blocks': 0,
            'max_blocks': 1,
            'parallelism': 1.0,
            'walltime': '00:10:00',
            'scheduler_options': '',
            'regex_job_id': 'Submitted batch job (?P<id>\\S*)',
            'worker_init': '',
            'exclusive': True,
            'move_files': True
            }

        if 'provider' in data:
            if data['provider']['type'] != 'SlurmProvider':
                raise Exception('Unsupported provider: ' + data['provider']['type'])
            
            if 'partition' in data['provider']:
                self.provider['partition'] = data['provider']['partition']
            if 'account' in data['provider']:
                self.provider['account'] = data['provider']['account']
            if 'qos' in data['provider']:
                self.provider['qos'] = data['provider']['qos']
            if 'constraint' in data['provider']:
                self.provider['constraint'] = data['provider']['constraint']
            if 'channel' in data['provider']:
                self.provider['channel'] = data['provider']['channel']
            if 'nodes_per_block' in data['provider']:
                self.provider['nodes_per_block'] = data['provider']['nodes_per_block']
            if 'cores_per_node' in data['provider']:
                self.provider['cores_per_node'] = data['provider']['cores_per_node']
            if 'mem_per_node' in data['provider']:
                self.provider['mem_per_node'] = data['provider']['mem_per_node']
            if 'init_blocks' in data['provider']:
                self.provider['init_blocks'] = data['provider']['init_blocks']
            if 'min_blocks' in data['provider']:
                self.provider['min_blocks'] = data['provider']['min_blocks']
            if 'max_blocks' in data['provider']:
                self.provider['max_blocks'] = data['provider']['max_blocks']
            if 'parallelism' in data['provider']:
                self.provider['parallelism'] = data['provider']['parallelism']
            if 'walltime' in data['provider']:
                self.provider['walltime'] = data['provider']['walltime']
            if 'scheduler_options' in data['provider']:
                self.provider['scheduler_options'] = data['provider']['scheduler_options']
            if 'regex_job_id' in data['provider']:
                self.provider['regex_job_id'] = data['provider']['regex_job_id']
            if 'worker_init' in data['provider']:
                self.provider['worker_init'] = data['provider']['worker_init']
            if 'exclusive' in data['provider']:
                self.provider['exclusive'] = data['provider']['exclusive']
            if 'move_files' in data['provider']:
                self.provider['move_files'] = data['provider']['move_files']

        self.executor = {
            'label': 'HighThroughputExecutor',
            'launch_cmd': None,
            'address': None,
            'worker_ports': None,
            'worker_port_range': (54000, 55000),
            'interchange_port_range': (55000, 56000),
            'storage_access': None,
            'working_dir': None,
            'worker_debug': False,
            'cores_per_worker': 1.0,
            'mem_per_worker': None,
            'max_workers': float('inf'),
            'cpu_affinity': 'none',
            'available_accelerators': [],
            'prefetch_capacity': 0,
            'heartbeat_threshold': 120,
            'heartbeat_period': 30,
            'poll_period': 10,
            'address_probe_timeout': None,
            'worker_logdir_root': None
        }
        
        if 'executor' in data:
            if data['executor']['type'] != 'HighThroughputExecutor':
                raise Exception('Unsupported executor: ' + data['executor']['type'])
            
            if 'label' in data['executor']:
                self.executor['label'] = data['executor']['label']
            if 'launch_cmd' in data['executor']:
                self.executor['launch_cmd'] = data['executor']['launch_cmd']
            if 'address' in data['executor']:
                self.executor['address'] = data['executor']['address']
            if 'worker_ports' in data['executor']:
                self.executor['worker_ports'] = data['executor']['worker_ports']
            if 'worker_port_range' in data['executor']:
                self.executor['worker_port_range'] = (data['executor']['worker_port_range'][0], data['executor']['worker_port_range'][1])
            if 'interchange_port_range' in data['executor']:
                self.executor['interchange_port_range'] = (data['executor']['interchange_port_range'][0], data['executor']['interchange_port_range'][1])
            if 'storage_access' in data['executor']:
                self.executor['storage_access'] = data['executor']['storage_access']
            if 'working_dir' in data['executor']:
                self.executor['working_dir'] = data['executor']['working_dir']
            if 'worker_debug' in data['executor']:
                self.executor['worker_debug'] = data['executor']['worker_debug']
            if 'cores_per_worker' in data['executor']:
                self.executor['cores_per_worker'] = data['executor']['cores_per_worker']
            if 'mem_per_worker' in data['executor']:
                self.executor['mem_per_worker'] = data['executor']['mem_per_worker']
            if 'max_workers' in data['executor']:
                self.executor['max_workers'] = data['executor']['max_workers']
            if 'cpu_affinity' in data['executor']:
                self.executor['cpu_affinity'] = data['executor']['cpu_affinity']
            if 'available_accelerators' in data['executor']:
                self.executor['available_accelerators'] = data['executor']['available_accelerators']
            if 'prefetch_capacity' in data['executor']:
                self.executor['prefetch_capacity'] = data['executor']['prefetch_capacity']
            if 'heartbeat_threshold' in data['executor']:
                self.executor['heartbeat_threshold'] = data['executor']['heartbeat_threshold']
            if 'heartbeat_period' in data['executor']:
                self.executor['heartbeat_period'] = data['executor']['heartbeat_period']
            if 'poll_period' in data['executor']:
                self.executor['poll_period'] = data['executor']['poll_period']
            if 'address_probe_timeout' in data['executor']:
                self.executor['address_probe_timeout'] = data['executor']['address_probe_timeout']
            if 'worker_logdir_root' in data['executor']:
                self.executor['worker_logdir_root'] = data['executor']['worker_logdir_root']

        return

    def execute(self):
        parsl.load(Config(executors = [
            HighThroughputExecutor(
            label = self.executor['label'],
            launch_cmd = self.executor['launch_cmd'],
            address = self.executor['address'],
            worker_ports = self.executor['worker_ports'],
            worker_port_range = self.executor['worker_port_range'],
            interchange_port_range = self.executor['interchange_port_range'],
            storage_access = self.executor['storage_access'],
            working_dir = self.executor['working_dir'],
            worker_debug = self.executor['worker_debug'],
            cores_per_worker = self.executor['cores_per_worker'],
            mem_per_worker = self.executor['mem_per_worker'],
            max_workers = self.executor['max_workers'],
            cpu_affinity = self.executor['cpu_affinity'],
            available_accelerators = self.executor['available_accelerators'],
            prefetch_capacity = self.executor['prefetch_capacity'],
            heartbeat_threshold = self.executor['heartbeat_threshold'],
            heartbeat_period = self.executor['heartbeat_period'],
            poll_period = self.executor['poll_period'],
            address_probe_timeout = self.executor['address_probe_timeout'],
            worker_logdir_root = self.executor['worker_logdir_root'],
            provider =  SlurmProvider(
                partition = self.provider['partition'],
                account = self.provider['account'],
                qos = self.provider['qos'],
                constraint = self.provider['constraint'],
                channel = self.provider['channel'],
                nodes_per_block = self.provider['nodes_per_block'],
                cores_per_node = self.provider['cores_per_node'],
                mem_per_node = self.provider['mem_per_node'],
                init_blocks = self.provider['init_blocks'],
                min_blocks = self.provider['min_blocks'],
                max_blocks = self.provider['max_blocks'],
                parallelism = self.provider['parallelism'],
                walltime = self.provider['walltime'],
                scheduler_options = self.provider['scheduler_options'],
                regex_job_id = self.provider['regex_job_id'],
                worker_init = self.provider['worker_init'],
                exclusive = self.provider['exclusive'],
                move_files = self.provider['move_files'],
                launcher = SrunLauncher(
                    debug = self.launcher['debug'], 
                    overrides = self.launcher['overrides']
                    )
                )
            )
        ]))
                   
        srunCommand(self.data['command'], str(self.config)).result()
        parsl.clear()
    
    def _start(self, startTick, startTime):
        self.execute()
        return True

        
    def _step(self, lastRunTick, lastRunTime, currentTick, currentTime, targetTick, targetTime):
        self.execute()
        return True
        
    def _end(self, lastRunTick, lastRunTime, endTick, endTime):
        self.execute()
        return True
