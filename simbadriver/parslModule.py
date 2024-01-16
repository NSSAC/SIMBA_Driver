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

class ParslModule(Module):
    def _init(self, data):
        launcher = {
            'debug': True,
            'overrides': ''
            }

        if 'launcher' in data:
            if 'debug' in data['launcher']:
                launcher['debug'] = data['launcher']['debug']
            if 'overrides' in data['launcher']:
                launcher['overrides'] = data['launcher']['overrides']

        self.launcher = SrunLauncher(
            debug = launcher['debug'], 
            overrides = launcher['overrides']
            )

        provider = {
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
                provider['partition'] = data['provider']['partition']
            if 'account' in data['provider']:
                provider['account'] = data['provider']['account']
            if 'qos' in data['provider']:
                provider['qos'] = data['provider']['qos']
            if 'constraint' in data['provider']:
                provider['constraint'] = data['provider']['constraint']
            if 'channel' in data['provider']:
                provider['channel'] = data['provider']['channel']
            if 'nodes_per_block' in data['provider']:
                provider['nodes_per_block'] = data['provider']['nodes_per_block']
            if 'cores_per_node' in data['provider']:
                provider['cores_per_node'] = data['provider']['cores_per_node']
            if 'mem_per_node' in data['provider']:
                provider['mem_per_node'] = data['provider']['mem_per_node']
            if 'init_blocks' in data['provider']:
                provider['init_blocks'] = data['provider']['init_blocks']
            if 'min_blocks' in data['provider']:
                provider['min_blocks'] = data['provider']['min_blocks']
            if 'max_blocks' in data['provider']:
                provider['max_blocks'] = data['provider']['max_blocks']
            if 'parallelism' in data['provider']:
                provider['parallelism'] = data['provider']['parallelism']
            if 'walltime' in data['provider']:
                provider['walltime'] = data['provider']['walltime']
            if 'scheduler_options' in data['provider']:
                provider['scheduler_options'] = data['provider']['scheduler_options']
            if 'regex_job_id' in data['provider']:
                provider['regex_job_id'] = data['provider']['regex_job_id']
            if 'worker_init' in data['provider']:
                provider['worker_init'] = data['provider']['worker_init']
            if 'exclusive' in data['provider']:
                provider['exclusive'] = data['provider']['exclusive']
            if 'move_files' in data['provider']:
                provider['move_files'] = data['provider']['move_files']

        self.provider = SlurmProvider(
            partition = provider['partition'],
            account = provider['account'],
            qos = provider['qos'],
            constraint = provider['constraint'],
            channel = provider['channel'],
            nodes_per_block = provider['nodes_per_block'],
            cores_per_node = provider['cores_per_node'],
            mem_per_node = provider['mem_per_node'],
            init_blocks = provider['init_blocks'],
            min_blocks = provider['min_blocks'],
            max_blocks = provider['max_blocks'],
            parallelism = provider['parallelism'],
            walltime = provider['walltime'],
            scheduler_options = provider['scheduler_options'],
            regex_job_id = provider['regex_job_id'],
            worker_init = provider['worker_init'],
            exclusive = provider['exclusive'],
            move_files = provider['move_files'],
            launcher = self.launcher
            )

        executor = {
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
                executor['label'] = data['executor']['label']
            if 'launch_cmd' in data['executor']:
                executor['launch_cmd'] = data['executor']['launch_cmd']
            if 'address' in data['executor']:
                executor['address'] = data['executor']['address']
            if 'worker_ports' in data['executor']:
                executor['worker_ports'] = data['executor']['worker_ports']
            if 'worker_port_range' in data['executor']:
                executor['worker_port_range'] = (data['executor']['worker_port_range'][0], data['executor']['worker_port_range'][1])
            if 'interchange_port_range' in data['executor']:
                executor['interchange_port_range'] = (data['executor']['interchange_port_range'][0], data['executor']['interchange_port_range'][1])
            if 'storage_access' in data['executor']:
                executor['storage_access'] = data['executor']['storage_access']
            if 'working_dir' in data['executor']:
                executor['working_dir'] = data['executor']['working_dir']
            if 'worker_debug' in data['executor']:
                executor['worker_debug'] = data['executor']['worker_debug']
            if 'cores_per_worker' in data['executor']:
                executor['cores_per_worker'] = data['executor']['cores_per_worker']
            if 'mem_per_worker' in data['executor']:
                executor['mem_per_worker'] = data['executor']['mem_per_worker']
            if 'max_workers' in data['executor']:
                executor['max_workers'] = data['executor']['max_workers']
            if 'cpu_affinity' in data['executor']:
                executor['cpu_affinity'] = data['executor']['cpu_affinity']
            if 'available_accelerators' in data['executor']:
                executor['available_accelerators'] = data['executor']['available_accelerators']
            if 'prefetch_capacity' in data['executor']:
                executor['prefetch_capacity'] = data['executor']['prefetch_capacity']
            if 'heartbeat_threshold' in data['executor']:
                executor['heartbeat_threshold'] = data['executor']['heartbeat_threshold']
            if 'heartbeat_period' in data['executor']:
                executor['heartbeat_period'] = data['executor']['heartbeat_period']
            if 'poll_period' in data['executor']:
                executor['poll_period'] = data['executor']['poll_period']
            if 'address_probe_timeout' in data['executor']:
                executor['address_probe_timeout'] = data['executor']['address_probe_timeout']
            if 'worker_logdir_root' in data['executor']:
                executor['worker_logdir_root'] = data['executor']['worker_logdir_root']
            
            
        self.executor = HighThroughputExecutor(
            label = executor['label'],
            launch_cmd = executor['launch_cmd'],
            address = executor['address'],
            worker_ports = executor['worker_ports'],
            worker_port_range = executor['worker_port_range'],
            interchange_port_range = executor['interchange_port_range'],
            storage_access = executor['storage_access'],
            working_dir = executor['working_dir'],
            worker_debug = executor['worker_debug'],
            cores_per_worker = executor['cores_per_worker'],
            mem_per_worker = executor['mem_per_worker'],
            max_workers = executor['max_workers'],
            cpu_affinity = executor['cpu_affinity'],
            available_accelerators = executor['available_accelerators'],
            prefetch_capacity = executor['prefetch_capacity'],
            heartbeat_threshold = executor['heartbeat_threshold'],
            heartbeat_period = executor['heartbeat_period'],
            poll_period = executor['poll_period'],
            address_probe_timeout = executor['address_probe_timeout'],
            worker_logdir_root = executor['worker_logdir_root'],
            provider = self.provider
            )

        return

    @bash_app
    def srunCommand(self, config, stdout = 'module.stdout', stderr = 'module.stderr'):
        return self.command + ' ' + self.config
    
    def execute(self):
        parsl.load(Config(executors = [self.executor]))
        self.srunCommand().result()
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
