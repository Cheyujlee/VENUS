import argparse

usage = """Usage: %prog[-h] -r1 read1.fastq [-r2 read2.fastq, default: None]
                  -o Output file name prefix [-scBarcodeWhitelist Whitelist file, default: None]
                  [-scCBstart Cell barcode start, default: None] [-scCBlen Cell barcode length, default: None] 
                  [-scUMIstart UMI start, default: None] [-scUMIlen UMI length, default: None]
                  [-t Number of Threads, default: 8]"""

def main():
    parser = argparse.ArgumentParser(description='VENUS')

    parser.add_argument('-r1', '--fq1', required = True, metavar = 'read1.fastq', type = str, help = 'Read 1 of the paired end/single end bulk seq OR cDNA read of single-cell seq')
 
    parser.add_argument('-r2', '--fq2', required = False, metavar = 'read2.fastq', type = str, default = None, help = 'Read 2 of the paired end bulk seq OR Barcode read of single-cell seq')

    parser.add_argument('-o', '--outFileNamePrefix', required = True, metavar = 'Output file name prefix', type = str, help = 'Output directory to store the alignement results')

    parser.add_argument('-scCBstart', '--soloCBstart', required = False, metavar = 'Cell barcode start', type = int, default = None, help = 'Cell barcode start position in barcode read of single-cell seq')

    parser.add_argument('-scCBlen', '--soloCBlen', required = False, metavar = 'Cell barcode length', type = int, default = None, help = 'Cell barcode length in barcode read of single-cell seq')

    parser.add_argument('-scUMIstart', '--soloUMIstart', required = False, metavar = 'UMI start', type = int, default = None, help = 'UMI start position in barcode read of single-cell seq')

    parser.add_argument('-scUMIlen', '--soloUMIlen', required = False, metavar = 'UMI length', type = int, default = None, help = 'UMI length in barcode read of single-cell seq')
    
    parser.add_argument('-t', '--runThreadN', required = False, metavar = 'Number of threads, default: 8', default = '8', type = str, help = 'Number of threads')

    return None


if __name__ == '__main__':
    main()