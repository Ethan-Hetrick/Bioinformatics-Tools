# Bioinformatics-Tools
Miscellaneous bioinformatics tools to make things more convenient :D.


#fasterq-dump-auto.py

Program versions: Python 3.7.0 and "fasterq-dump" version 2.11.3
Python modules: subprocess and argparse

Lets you add a list of SRR accessions to the sratoolkit fasterq-dump command. Takes a text file with SRRs on different lines. 
Runs the command $ fasterq-dump --split-files -e 16 -O <output directory> <SRR>
To change the options, change the "cmd" variable in the Python script.

usage: fasterq-dump.py [-h] [-i INPUT] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to SRR list text file.
  -o OUTPUT, --output OUTPUT
                        Path to output.
