#!/bin/bash
#SBATCH --job-name=tstVenus
#SBATCH --nodes=1
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=4G
#SBATCH --time=24:00:00
#SBATCH --partition=zhanglab.p
#SBATCH --output=/srv/disk00/cheyul1/Venus/06-25-21/run4/run4.log

python3 /srv/disk00/cheyul1/Venus/Venus.py \
--read1 /srv/disk00/cheyul1/Venus/bulk_data/single-end.fastq \
--outDir /srv/disk00/cheyul1/Venus/06-25-21/run4/