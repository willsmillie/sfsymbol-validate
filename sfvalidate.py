# sfvalidate.py

import argparse
import symbols
import sys

# Setup SFValidate Parser
parser = argparse.ArgumentParser(
    prog='sfvalidate',
    usage='%(prog)s [options] path',
    description='Format and validate a txt list of SFSymbols (e.g. received via email)')

# arg for file containing an unformatted list of SFSymbols
parser.add_argument(
    'filename',
    type=argparse.FileType('r'))

# arg for file to output the report to
parser.add_argument("-o", "--output", nargs='?', type=argparse.FileType('w'),
                    default=sys.stdout, help="Directs the output to a file your choice")

# begin parsing the provided args
args = parser.parse_args()

# read the contents of the file provided
# then close the file
text = args.filename.read()
args.filename.close()

# parse the input text
results = symbols.parse(text)
report = '\n'.join(results)

if args.output is not None:
    # write the results to the file
    # then close the file
    args.output.write(report)
    args.output.close()
else:
    print(report)
