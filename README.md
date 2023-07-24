This is a workflow for processing and quanitifying tRNA-seq reads with added spike-in.

The snakemake pipeline handles constructing references, read preprocessing and alignment automatically.

Downstream stages happen in the included notebooks

## Setup:

1. Put files containing raw reads in FASTQ format in the '00_raw' directory(make one if it's not there). Make sure their extensions are '.fastq.gz', as all other types will be ignored.
2. Download mature tRNA fastas for both target and spike-in organism and put them into the 'references' directory.
5. In the snakefile, set:
  - TRNA_FASTA_TARGET to "references/<name_of_target_fasta_file>"
  - TRNA_FASTA_SPIKE to "references/<name_of_spike_fasta_file>"

## Running pipeline:

First run:
```
snakemake -n --use-conda --cores [number-of-cores-to-use]
```

to verify if you've set everything up properly. If it doesn't throw up any errors, you're good to go.

To run full pipeline:
```
snakemake --use-conda --cores [number-of-cores-to-use]
```

## Plotting results with included notebooks

There are two notebooks included with the repo. They contain code and instructions for producing a basic set of figures out of the data. Both do the same thing, but one aggregates isodecoder tRNA into isoacceptor (codon) groups.

Both run R code from python and require rpy2 to be installed via pip.
