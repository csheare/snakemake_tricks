# snakemake_tricks


Ah, yes, what would life be without some annoyances. So, as it turns out to run snakemake on o2, keep the following in mind:

when you run . load_sm.txt the module load command does some things to the environment which essentially cause the python
command to point to the anaconda python (2.7v) instead of the python in your desired environment fed to the Snakemake file.

A current workaround: just use python3 as the command within the Snakemake file. Non ideal, but it works for now. Or until some
person decides to install python3 on the anaconda path for the marks lab. Maybe this can be resolved, ive given up for today.

