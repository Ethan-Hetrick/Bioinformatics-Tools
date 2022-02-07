from Bio import Entrez
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, help="Path to SRR list text file.")
parser.add_argument("-o", "--output", type=str, help="Path to output.")
args = parser.parse_args()


def WGS_IDtoSRR(WGS_ID):
    Entrez.api_key = "31b7d905b897989c39b12f39e77c58884508"
    Entrez.email = "rqu4@cdc.gov"
    handle = Entrez.esearch(db="SRA", term=WGS_ID, idtype="External Id", retmax=40)
    record = Entrez.read(handle)
    SRAID = (record["IdList"][0])
    handle = Entrez.efetch(db="SRA", id=SRAID, retmode="xml")
    for item in handle:
        srrstart = item.find('filename="SRR')
        if srrstart != -1:
            SRRID = (item[srrstart+10:srrstart+21]).strip('"')
            break
    return SRRID

def run(input, output):
    with open(input, "r") as f:
        for wgsid in f.readlines():
            try:
                time.sleep(0.1)
                srr = WGS_IDtoSRR(wgsid)
                with open(output, "a") as out:
                    out.write(wgsid.strip("\n") + "," + srr + "\n")
            except Exception as e:
                print((wgsid.strip("\n") + " had error: " + str(e).strip("\n")))
                print("WGS ID likely invalid or reads were not uploaded.")
                continue

run(args.input, args.output)