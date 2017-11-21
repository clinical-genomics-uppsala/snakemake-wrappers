__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2017, Patrik Smeds"
__email__ = "patrik.smeds@scilifelab.uu.se"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

path_gatk = snakemake.params.get("path_gatk")

if path_gatk is None:
    raise ValueError("path to gatk cannot be empty")

genome_ref = snakemake.params.get("genome_ref")

if genome_ref is None:
    raise ValueError("A genome reference must be provided")

design_file = snakemake.params.get("design_file")

if design_file is None:
    raise ValueError("A design file, contain amplicon in bed format, must be provded")

shell(
 "java -jar " + path_gatk + " " +
 "-T MapReadToAmpliconsIlluminaReadPair " +
 "-R " + genome_ref + " " +
 "-I {snakemake.input} " +
 "-o {snakemake.output.bed} " +
 "-fragments " + design_file + " " +
 "-ampAnReads {snakemake.output.bam} " +
 "-U ALL " +
 "-nonunique " +
 "-allowPotentiallyMisencodedQuals " +
 "--downsample_to_coverage 90000 " +
 "-molBarCode 0 " +
 "{log}")
