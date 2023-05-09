This is a workflow for processing and quanitifying tRNA-seq reads.

Setup:

1. Put files containing raw reads in FASTQ format in the 'fastq' directory. Make sure their extensions are '.fastq.gz', as all other types will be ignored.
2. Put correct bowtie2 index files in the 'references/bowtie2_index' directory.
3. Put correct salmon index folder in the 'references/salmon_index' directory.
4. Put "xxxx-mature-tRNAs.fa" file form gtRNA-db in the 'tRNA' directory
5. In the snakefile, set:
  - BOWTIE_INDEX to 'references/bowtie2_index/{name_of_your_bowtie2_index}' – don't include file extensions, just the name of your index
  - SALMON_INDEX to 'references/salmon_index/{name_of_your_salmon_index}' – again, just the folder name
  - TRNA_FASTA to '/references/trna/{your_mature-trna.fa}'

Running pipeline:

First run:
```
snakemake -n
```

to verify if you've set everything up properly. If it doesn't throw up any errors, you're good to go.

To run full pipeline:
```
snakemake -p --use-conda --cores
```
