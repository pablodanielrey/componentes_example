#!/bin/bash

python3 -m venv env
source env/bin/activate

pip install pepe_models/.
pip install pepe_infra/.
pip install pepe_c1/.
pip install pepe_c2/.

python3 -m dv_pepe.infra