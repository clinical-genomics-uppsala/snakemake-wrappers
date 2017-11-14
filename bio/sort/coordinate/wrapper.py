__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2017, Patrik Smeds"
__email__ = "patrik.smeds@scilifelab.uu.se"
__license__ = "MIT"

from snakemake.shell import shell

command = "samtools sort {snakemake.input} > {snakemake.output.bam}"

shell(command)
