#!/bin/bash

# job name
#SBATCH -J <JOB-NAME>

# partition
#SBATCH -p gpu

# ensures all allocated cores are on the same node
#SBATCH -N 1

# cpu cores
#SBATCH --ntasks-per-node=4

# memory per node
#SBATCH --mem=32G

# runtime
#SBATCH -t 96:00:00

# output
#SBATCH -o sbatch_out.out

# error
#SBATCH -e sbatch_err.err

# email notifiaction
# SBATCH --mail-type=ALL

module load miniconda3/23.11.0s
source /oscar/runtime/software/external/miniconda3/23.11.0/etc/profile.d/conda.sh
conda activate gaussian_splatting

python3 train.py -s tandt/train
