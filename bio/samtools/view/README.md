# Wrapper for samtools view.

## Example:

```
rule samtools_view:
    input:
        "{sample}.sam"
    output:
        "{sample}.bam"
    params:
        "-b" # optional params string
    wrapper:
        "0.6.0/bio/samtools/view"
```