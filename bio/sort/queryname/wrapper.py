__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2017, Patrik Smeds"
__email__ = "patrik.smeds@scilifelab.uu.se"
__license__ = "MIT"

from snakemake.shell import shell

if snakemake.params.get("remove_secondary_alignment",False):
    command = "samtools view -h -b -F 0x100 {snakemake.input} | " + \
              "samtools sort -n -@ 3 /dev/stdin > {snakemake.output.bam}"
else:
    command = "samtools sort -n -@ 3 {snakemake.input} > {snakemake.output.bam}"

shell(command)
