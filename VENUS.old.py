import argparse
import os
import sys

usage = """Usage: %prog[-h] -r1 read1.fastq [-r2 read2.fastq, default: None]
                  [-o Output file name prefix, default: cwd] [-sc Single cell option, default: False]
                  [-scBarcodeWhitelist Whitelist file, default: Unspecified]
                  [-scCBstart Cell barcode start, default: Unspecified] [-scCBlen Cell barcode length, default: Unspecified] 
                  [-scUMIstart UMI start, default: Unspecified] [-scUMIlen UMI length, default: Unspecified]
                  [-t Number of Threads, default: 8] [-gtfTrueFalse ] [-qc True]"""

def main():
    parser = argparse.ArgumentParser(description='VENUS')

    parser.add_argument('-r1', '--read1', required = True, metavar = 'read1.fastq', type = str, help = 'Read 1 of the paired end/single end bulk seq OR cDNA read of single-cell seq')
 
    parser.add_argument('-r2', '--read2', required = False, metavar = 'read2.fastq', type = str, default = '', help = 'Read 2 of the paired end bulk seq OR Barcode read of single-cell seq')

    parser.add_argument('-o', '--outFileNamePrefix', required = False, metavar = 'Output file name prefix, default: cwd', type = str, default = '', help = 'Output directory to store the alignement results')

    parser.add_argument('-sc', '--solo', required = False, metavar = 'Single cell option, default: False', type = str, default = 'False', help = 'Single cell option switch')

    # parser.add_argument('-scBarcodeWhitelist ', '--solo', required = False, metavar = 'Single cell option, default: False', type = str, default = 'False', help = 'Single cell option switch')

    parser.add_argument('-scCBstart', '--soloCBstart', required = False, metavar = 'Cell barcode start, default: Unspecified', type = str, default = '', help = 'Cell barcode start position in barcode read of single-cell seq')

    parser.add_argument('-scCBlen', '--soloCBlen', required = False, metavar = 'Cell barcode length, default: Unspecified', type = str, default = '', help = 'Cell barcode length in barcode read of single-cell seq')

    parser.add_argument('-scUMIstart', '--soloUMIstart', required = False, metavar = 'UMI start, default: Unspecified', type = str, default = '', help = 'UMI start position in barcode read of single-cell seq')

    parser.add_argument('-scUMIlen', '--soloUMIlen', required = False, metavar = 'UMI length, default: Unspecified', type = str, default = '', help = 'UMI length in barcode read of single-cell seq')
    
    parser.add_argument('-t', '--runThreadN', required = False, metavar = 'Number of threads, default: 8', default = '8', type = str, help = 'Number of threads')

    
    args = parser.parse_args()

    fq1 = os.path.abspath(args.fq1)

    try:
        os.path.isfile(fq1)
        open(fq1, 'r')
    except IOError:
        print('Error: There was no Read 1 FASTQ file!')
        sys.exit()

    
    fq2 = os.path.abspath(args.fq2)

    if fq2 != os.getcwd():
        try:
            os.path.isfile(fq2)
            open(fq2, 'r')
        except IOError:
            print('Error: There was no Read 2 FASTQ file!')
            sys.exit()
    

    outFileNamePrefix = os.path.abspath(args.outFileNamePrefix)

    
    solo = args.solo

    if solo == 'True':
        print('Opted in for single cell option')
    elif solo == 'False':
        print('Opted out of single cell option')
    else:
        print('Error: Please type only True or False when specifying single cell option.')
        sys.exit()
    
    
    soloCBstart = args.soloCBstart

    soloCBlen = args.soloCBlen

    soloUMIstart = args.soloUMIstart

    soloUMIlen = args.soloUMIlen

    if solo == 'True':
        if soloCBstart == '':
            print('Error: Please specify a cell barcode start position.')
        elif soloCBlen == '':
            print('Error: Please specify a cell barcode length.')
        elif soloUMIstart == '':
            print('Error: Please specify an UMI start position.')
        elif soloUMIlen == '':
            print('Error: Please specify an UMI length.')


    runThreadN = args.runThreadN
    
    return None


if __name__ == '__main__':
    main()