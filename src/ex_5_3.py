""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
import argparse
def process_data(infile, outfile):
    """
    Process the data from the input file `infile`, scale it to have a mean of 0 and standard deviation of 1,
    and write the processed data to the output file `outfile`.
    
    Args:
        infile (str): Input filename for the data file to be processed.
        outfile (str): Output filename to write the processed data.
    """
    # Load data from the input file into a numpy array
    data = np.loadtxt(infile, delimiter=',')

    # Process the data: shift mean to 0 and scale standard deviation to 1
    mean_data = np.mean(data, axis=0)  # Compute mean along columns
    std_data = np.std(data, axis=0)    # Compute standard deviation along columns

    processed = (data - mean_data) / std_data  # Normalize the data

    # Save the processed data to the output file using numpy.savetxt
    np.savetxt(outfile, processed, delimiter=',', fmt='%.6f')
    print(f"Processed data saved to {outfile}")

if __name__ == "__main__":
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="This program applies a standard scale transform to the data in infile and writes it to outfile.")
    
    # Add positional arguments for infile and outfile
    parser.add_argument("infile", type=str, help="Input filename for the data file to be processed.")
    parser.add_argument("outfile", type=str, help="Output filename to write the processed data.")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Call process_data function with the provided input and output filenames
    process_data(args.infile, args.outfile)
