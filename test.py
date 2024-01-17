#!/usr/bin/env python3

from parsl.config import Config
from parsl.channels import LocalChannel
from parsl.providers import SlurmProvider
from parsl.executors import HighThroughputExecutor
from parsl.launchers import SrunLauncher
from parsl.app.app import bash_app

import parsl

config = Config(
    executors=[
        HighThroughputExecutor(
            label="rivanna",
            provider=SlurmProvider(
                nodes_per_block=1,
                cores_per_node=1,
                init_blocks=1,
                account='nssac_covid19',
                qos='bii-half',
                partition='bii',
                exclusive=False,
                launcher=SrunLauncher(),
            ),
        )
    ],
)

@bash_app
def submit(command, stdout='hostname.stdout', stderr='hostname.stderr'):
    return command

parsl.load(config)

submit('hostname').result()

with open('hostname.stdout', 'r') as f:
     print(f.read())

parsl.clear()