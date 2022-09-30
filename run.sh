#!/bin/bash

python3 -m venv env
source env/bin/activate

pip install -e pepe_models/.
pip install -e pepe_infra/.
pip install -e pepe_c1/.
pip install -e pepe_c2/.

python3 -m dv_pepe.infra
