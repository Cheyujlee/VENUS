import argparse

usage = """Usage: %prog[-h] -r1 cDNA.read.fastq -r2 barcode.read.fastq
                  -index Index Directory -scBarcodeWhitelist Whitelist file
                  -o Output File Name Prefix -t 16
                  -scCBstart 1 -scCBlen 16 -scUMIstart 17 -scUMIlen 10"""

def main():
    parser = argparse.ArgumentParser(description='VENUS')

    return None


if __name__ == '__main__':
    main()