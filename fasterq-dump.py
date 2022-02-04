import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, help='Path to SRR list text file.')
parser.add_argument("-o", "--output", type=str, help='Path to output.')
args = parser.parse_args()


def fasterqdump(txt, path):
    with open(txt) as f:
        SRRIDs = f.readlines()
        for line in SRRIDs:
            SRR = line.strip("\n")
            print("Reading: " + SRR)
            cmd = ('fasterq-dump --split-files -e 16 -O ' + path + ' ' + SRR)
            sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            sp.wait()
            out, err = sp.communicate()
            if err != b'':
                print(err.decode())
                continue

fasterqdump(args.input, args.output)