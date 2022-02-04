# Bioinformatics-Tools
Miscellaneous bioinformatics tools to make life more convenient :D.

---

### *fasterq-dump-auto.py*

Works with: Python 3.7.0 and "fasterq-dump" version 2.11.3
Python modules: subprocess and argparse

Lets you add a list of SRR accessions to the sratoolkit fasterq-dump command. Takes a text file with SRRs on separate lines. 
Runs the command $ fasterq-dump --split-files -e 16 -O <output directory> <SRR>
To change the options, change the "cmd" variable in the Python script.

usage: fasterq-dump.py [-h] [-i list.txt] [-o path/to/directory]

---
  
