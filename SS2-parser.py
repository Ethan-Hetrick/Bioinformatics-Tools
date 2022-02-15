import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str, help="Path to SeqSero2 results.")
args = parser.parse_args()

def parse_SS2(input):
    with open(input, 'r') as f:
        output = f.read()
        result_list = output.split("Output_directory:")
        print("Input File\tAntigenic Formula\tSerotype\tError")
        for result in result_list:
            input, antigenic_profile, serotype, note, subspecies = "", "", "", "", ""
            for line in result.split("\n"):
                if "Input files:" in line:
                    input = line.split("files:")[1].strip()
                elif "Predicted antigenic profile:" in line:
                    antigenic_profile = line.split("profile:")[1].strip()
                elif "Predicted subspecies:" in line:
                    subspecies = line.split("subspecies:")[1].strip()
                elif "Predicted serotype:" in line:
                    serotype = line.split("serotype:")[1].strip()
                elif "Note" in line:
                    note = line.split("Note:")[1].strip()
                    note = " ".join(note.split())
            print(input, (subspecies + " " + antigenic_profile), serotype, note, sep="\t")

parse_SS2(args.input)
