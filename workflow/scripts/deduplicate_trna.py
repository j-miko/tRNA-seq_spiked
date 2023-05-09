import sys
import pandas as pd

# Usage: deduplicate_trna.py <input file> <output filename>

# input mature trna fastsa file (after fasta2tab) from stdin
trna_file = sys.argv[1]
out_filename = sys.argv[2]
df00 = pd.read_csv(trna_file, sep='\t', header=None)
df00 = df00.rename({0:'gene', 1:'seq'}, axis=1)
df00['seq'] = [x.replace('U', 'T') for x in df00['seq'].values]
df00['gene'] = df00['gene'].str.split(' ', expand=True)[0]
ss = df00['gene'].str.split("-", expand=True)
species_prefix = ss[0][0]
df00['anticodon'] = ss.apply(lambda x: '-'.join([x[1], x[2]]), axis=1)
df00['isodecoder'] = ss.apply(lambda x: '-'.join([x[3], x[4]]), axis=1)
# merge duplicate isodecoders into single records
df01 = df00.groupby('seq')['isodecoder'].apply(lambda x: ';'.join(x)).reset_index()
df01 = df01.merge(df00[['seq','anticodon']].drop_duplicates(), on='seq',how='left')
df01['gene'] = df01.apply(lambda x: '_'.join([species_prefix, x['anticodon'], x['isodecoder']]),axis=1)
df01['len'] = df01['seq'].apply(len)
with open(out_filename, 'w') as f:
    for row in range(df01.shape[0]):
        f.write(">" + df01['gene'][row] + " " + str(df01['len'][row]) + '\n')
        f.write(df01['seq'][row] + '\n')