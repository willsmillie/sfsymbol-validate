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
parser.add_argument('filename', type=argparse.FileType('r'))
# arg for file to output the report to
parser.add_argument("-r", "--report", type=argparse.FileType('w'),
                    help="Generate a report and output to a file your choice")

# begin parsing the provided args
args = parser.parse_args()

# read the contents of the file provided
# then close the file
text = args.filename.read()
args.filename.close()

# parse the input text; outputs an array of formatted strings, and an emoji pass or fail report
results, report = symbols.parse(text)

# format the parsed results
formatted_report = '\n'.join(report)
formatted_results = ', '.join('"{0}"'.format(w) for w in results)

# Prints the output of the program
print(formatted_report)
print("\nYou may copy and paste the following, all of which should work:\n\n")
print(formatted_results)

# write the report to the file
if args.report is not None:
    # write the results to the file
    # then close the file
    args.report.write(formatted_report)
    args.report.close()
