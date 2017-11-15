import subprocess
import os
import tempfile
import shutil

def run(wrapper, cmd):
    origdir = os.getcwd()
    with tempfile.TemporaryDirectory() as d:
        dst = os.path.join(d, "master", wrapper)
        os.makedirs(dst, exist_ok=True)
        copy = lambda src: shutil.copy(os.path.join(wrapper, src), dst)
        copy("wrapper.py")
        copy("environment.yaml")
        testdir = os.path.join(wrapper, ".test")
        os.chdir(testdir)
        if os.path.exists(".snakemake"):
            shutil.rmtree(".snakemake")
        cmd = cmd + ["--wrapper-prefix", "file://{}/".format(d)]
        subprocess.check_call(["snakemake", "--version"])
        try:
            subprocess.check_call(cmd)
        finally:
            os.chdir(origdir)
            for d, _, files in os.walk(os.path.join(testdir, "logs")):
                for f in files:
                    path = os.path.join(d, f)
                    with open(path) as f:
                        msg = "###### Logfile: " + path + " ######"
                        print(msg, "\n")
                        print(f.read())
                        print("#" * len(msg))


def test_queryname_sort():
    run("bio/sort/queryname",
        ["snakemake", "a.queryname_sorted.bam", "--verbose", "--use-conda", "-F"])

def test_coordinate_sort():
    run("bio/sort/coordinate",
        ["snakemake", "a.coordinate_sorted.bam", "--verbose", "--use-conda", "-F"])

# Need to add dependencies to run this
#def test_amplicon_mapping():
#    run("bio/amplicon_mapping",
#        ["snakemake", "a.amplicon_mapped.bed", "a.amplicon_mapped.bam", "--verbose", "--use-conda", "-F"])
