# Bioinformatics-Tools
Miscellaneous bioinformatics tools to make life more convenient :D.

---

### *fasterq-dump-auto.py*

Works with: Python 3.7.0 and "fasterq-dump" version 2.11.3
Python modules: subprocess and argparse

Lets you add a list of SRR accessions to the sratoolkit fasterq-dump command. Takes a line-separated text file of SRR IDs. 
Runs the command $ fasterq-dump --split-files -e 16 -O <output directory> <SRR>
To change the options, change the "cmd" variable in the Python script.

Usage: fasterq-dump.py [-h] [-i list.txt] [-o path/to/directory]

---
  
### *WGS_to_SRR.py*

Works with: Python 3.7.0
Python modules: BioPython, time, and argparse

Converts a list of WGS IDs (ex. PNUSAS IDs) and looks up the SRR IDs. Takes a line-separated list of WGS IDs and outputs a text 
  file in CSV format with the WGS ID and SRR ID. Can also be
used to validate a list of SRR IDs. This used the BioPython module Entrez import to essentially web-scrape the SRR IDs.

**NCBI limits number of requests for this, so it is essential to go in the Python script and set these two variables:**
  
- Entrez.api_key = "ENTER NCBI API KEY HERE"
- Entrez.email = "ENTER EMAIL HERE"

Usage: fasterq-dump.py [-h] [-i list.txt] [-o set output file name]
  
  ---
