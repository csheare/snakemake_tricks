

snakemake -p --use-conda  \
	--cluster-config cluster.o2.json \
	--jobs 100 \
	--cluster 'sbatch -p {cluster.queue} -n {cluster.n} -t {cluster.time} --mem={cluster.memory}'
