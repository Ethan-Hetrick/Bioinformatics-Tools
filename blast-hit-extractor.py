import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--blast-output", type=str, help="Path to blast output")
parser.add_argument("-a", "--assembly", type=str, help="Path to assembly")
parser.add_argument("-n", "--nuc", type=str, help="Number of flanking nucleotides")
args = parser.parse_args()

def blast_output_parser(blast_output):
    file = open(blast_output, "r")
    blast_output=file.read()
    file.close()
    blast_output_split=(blast_output.splitlines())
    hit_list = []
    for line in blast_output_split:
        qseqid,sseqid,pident,length,mismatch,gapopen,qstart,qend,sstart,send,evalue,bitscore = line.split("\t")
        hit_list.append([qseqid, int(qstart), int(qend), pident, length, int(sstart), int(send)])
    return(hit_list)
        
def hit_extractor(assembly, hit_list, flanking_nucl):
    file = open(assembly, "r")
    assembly = file.read()
    file.close()
    contig_list = assembly.split(">")
    for hit in hit_list:
        if hit[5] < hit[6]:
            orientation = "Forward"
        elif hit[5] > hit[6]:
            orientation = "Reverse"
        hit_start = min(hit[1], hit[2])-(1 + int(flanking_nucl))
        hit_end = max(hit[1], hit[2])+(1 + int(flanking_nucl))
        if hit_start < 0:
            hit_start = 0
        for contig in contig_list:
            if hit[0] in contig:
                sequence = (contig.strip(hit[0]))
                print(">"+hit[0]+"_Extracted_hit_pid_"+hit[3]+"_len_"+hit[4]+"_"+orientation)
                if hit_end > len(sequence):
                    hit_end = len(sequence)
                print((sequence[hit_start:hit_end]).strip("\n"))

hit_list = blast_output_parser(args.blast_output)
hit_extractor(args.assembly, hit_list, args.nuc)