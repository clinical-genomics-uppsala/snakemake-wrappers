__author__ = "Patrik Smeds"
__copyright__ = "Copyright 2017, Patrik Smeds"
__email__ = "patrik.smeds@scilifelab.uu.se"
__license__ = "MIT"

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

path_jsnpmania = snakemake.params.get("path_jsnpmania")

if path_jsnpmania is None:
    raise ValueError("path to jsnpmania cannot be empty")

path_jsnpmania_header = snakemake.params.get("path_jsnpmania_header")

if path_jsnpmania_header is None:
    raise ValueError("path to jsnpmania header cannot be empty")

shell(
 "samtools reheader " + path_jsnpmania_header + " {snakemake.input} | " +
 "samtools view /dev/stdin | " +
 path_jsnpmania + " jSNPMania.sh -i /dev/stdin " +
    "-o {snakemake.output.variations} " +
    "-oi {snakemake.output.insertions} " +
    "-od {snakemake.output.deletions} " +
    "-r {snakemake.params.ref_file} " +
    " {snakemake.params.flags} " +
    "{log}"
)
