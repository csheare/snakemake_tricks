
## This is an extremely trival way to run snakemake on o2.

Make sure you do the following:

```
module load snakemake
bash run.sh
```

To check that your job is running:

```
sq -j <job_id>
```

You should see the following result:

```
(/n/app/snakemake/6.5.2/snakemake) [csheare@compute-e-16-233 basic_o2_setup]$ bash run.sh
Building DAG of jobs...
Using shell: /usr/bin/bash
Provided cluster nodes: 100
Job stats:
job      count    min threads    max threads
-----  -------  -------------  -------------
test         1              1              1
total        1              1              1

Select jobs to execute...

[Sat Jan 21 12:02:09 2023]
rule test:
    jobid: 0
    resources: tmpdir=/tmp


			python test.py

Submitted job 0 with external jobid 'Submitted batch job 1780954'.
[Sat Jan 21 12:02:49 2023]
Finished job 0.
1 of 1 steps (100%) done
Complete log: /your_path/snakemake_tricks/basic_o2_setup/.snakemake/log/2023-01-21T120204.735493.snakemake.log
```