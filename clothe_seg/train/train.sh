#!/bin/bash

module load anaconda/2021.05
module load cuda/11.1
module load gcc/7.3

source activate mmclassification

export PYTHONBUFFERED=1

python train.py main_config.py --work-dir out_dir