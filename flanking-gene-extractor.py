import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--annotation", type=str, help="Path to annotation file in fasta format.")
parser.add_argument("-g", "--genbank", type=str, help="Path to Genbank file.")
parser.add_argument("-q", "--query", type=str, help="Path to query sequence file in fasta format.")
parser.add_argument("-o", "--output", type=str, help="Path to output file name.")
args = parser.parse_args()

def blast_cmd(query, subject, output_path):
    subject_name = ((subject.split("/"))[-1]).strip(".fasta")
    cmd = ("blastn -query " + query + " -subject " + subject + " -outfmt 6 -out " + output_path)
    sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sp.wait()
    out, err = sp.communicate()
    if err != b'':
        print(err.decode())
    elif out != b'':
        print(out.decode())
    return subject_name

def blast_output_parser(blast_output):
    file = open(blast_output, "r")
    blast_output=file.read()
    file.close()
    blast_output_split=(blast_output.splitlines())
    hit_list=[]
    for line in blast_output_split:
        if ((line.split("\t"))[1]) not in hit_list:
            hit = ((line.split("\t"))[1])
            identity = ((line.split("\t"))[2])
            hit_list.append(hit)
            print("Hit: " + hit)
            print("Identity: " + identity + "%")
    return(hit_list)

def gene_orientation(path, hit_list):
    hit_orientation_dict = {}
    with open(path, 'r') as f:
        x = 0
        gbk_file = f.readlines()
        f.close()
        for line in gbk_file:
            for hit in hit_list:
                if hit in line:
                    if 'complement' in (gbk_file[x-1]) or 'complement' in (gbk_file[x-2]):
                        hit_orientation_dict.update({hit:'complement'})
                        break
                    else:
                        if hit not in hit_orientation_dict:
                            hit_orientation_dict.update({hit: 'template'})
                            break
            x += 1
        return(hit_orientation_dict)

def find_flanking(dict, subject_name, hit_list, query):
    file = open(query, "r")
    ffn = file.read()
    file.close()
    genes = ffn.split(">")
    for gene in genes:
        for hit in hit_list:
            hit_position = (hit.split("_")[1])
            hit_above = str(int(hit_position) - 1).zfill(5)
            hit_below = str(int(hit_position) + 1).zfill(5)
            if hit_above in gene and dict[hit] == 'complement':
                with open("flanking-genes.fasta", 'w') as f:
                    if subject_name not in gene:
                        f.write(">" + path + "_" + gene)
                    else:
                        f.write(">" + gene)
            elif hit_below in gene and dict[hit] == 'template':
                with open('flanking-genes.fasta', 'w') as f:
                    if subject_name not in gene:
                        f.write(">" + path + "_" + gene)
                    else:
                        f.write(">" + gene)

def run():
    subject = blast_cmd(args.query, args.annotation, args.output)
    hits = blast_output_parser(args.output)
    orientation_dict = gene_orientation(args.genbank, hits)
    find_flanking(orientation_dict, subject, hits, args.query)

run()