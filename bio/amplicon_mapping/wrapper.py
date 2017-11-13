__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2017, Patrik Smeds"
__email__ = "patrik.smeds@scilifelab.uu.se"
__license__ = "MIT"

from snakemake.shell import shell

path_gatk = snakemake.params.get("gatk_with_amplicon_mapping")

if path_jsnpmania is None:
    raise ValueError("path to jsnpmania cannot be empty")

genome_ref = snakemake.params.get("genome_ref")

if genome_ref is None:
    raise ValueError("A genome reference must be provided")

design_file = snakemake.params.get("design_file")

if design_file is None:
    raise ValueError("A design file, contain amplicon in bed format, must be provded")

shell(
 "samtools view -h -b -F 0x100 {snakemake.input} | " +
 "samtools sort -n -@ 3 /dev/stdin /dev/stdout | " +
 "java -jar " + path_gatk + " " +
 "-T MapReadToAmpliconsIlluminaReadPair " +
 "-R " + genome_ref + " " +
 "-I /dev/stdin " +
 "-o {snakemake.outout.bed} " +
 "-fragments " design_file + " " +
 "-ampAnReads /dev/stdout " +
 "-U ALL -nonunique -allowPotentiallyMisencodedQuals --downsample_to_coverage 90000 -molBarCode 0 | " +
 "samtool sort -@ 3 /dev/stdin {snakemake.output.bam}")
