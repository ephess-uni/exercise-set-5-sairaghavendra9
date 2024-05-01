"""ex_5_1.py"""
try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count

import argparse
def main(infile):
    line_count(infile)

if __name__ == "__main__":
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="This program prints the number of lines in infile.")
    
    # Add a positional argument for the input file (infile)
    parser.add_argument("infile", type=str, help="The input file to count lines in.")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Call main function with the infile argument
    main(args.infile)
