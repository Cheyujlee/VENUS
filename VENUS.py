import argparse

usage = """Usage: %prog[-h] -r1 cDNA.read.fastq [-r2 barcode.read.fastq, default: None]
                  -index Index Directory -scBarcodeWhitelist Whitelist file
                  -o Output File Name Prefix [-t Number of Threads, default: 8]
                  -scCBstart 1 -scCBlen 16 -scUMIstart 17 -scUMIlen 10"""

def main():
    parser = argparse.ArgumentParser(description='VENUS')

    parser.add_argument('-r1', '--fq1',  required = True, metavar = 'read1.fastq', type = str, help ='The read 1 of the paired end RNA-seq')
 
    parser.add_argument('-r2', '--fq2',  required = False, metavar = 'read2.fastq', type = str, help ='The read 2 of the paired end RNA-seq')

    parser.add_argument('-o', '--out',  required = True, metavar = 'The output name for alignement', type = str, help ='Define the output directory to be stored the alignement results')

    parser.add_argument('-index', '--index_dir',  required = True, metavar = 'index files', type = str, help ='The directory of index files with hg38 prefix of the fasta file i.e,. index_files_directory/hg38')
   
    parser.add_argument('-d', '--distance', required = True, metavar = 'continuous_distance', type = int, help ='Define the continuous mapping distance of mapping reads to virus genome')

    parser.add_argument('-t', '--n_thread', required = False, metavar = 'Number of threads, default: 8', default = '8', type = str, help ='Number of threads') 

    return None


if __name__ == '__main__':
    main()