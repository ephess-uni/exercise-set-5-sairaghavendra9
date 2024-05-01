""" ex_5_2.py
This module contains an entry point that

- loads data from a file `ex_5_2-data.csv` into a numpy array
- shifts and scales the data such that the resulting mean
        is 0 and the standard deviation is 1.
- writes the processed data to a file called `ex_5_2-processed.csv`
"""
import numpy as np

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root


if __name__ == "__main__":

    # Use these predefined input / output files
    root_dir = get_repository_root()
    INFILE = root_dir / "data" / "ex_5_2-data.csv"
    OUTFILE = root_dir / "outputs" / "ex_5_2-processed.csv"

    # Load data from INFILE into a numpy array
    data = np.loadtxt(INFILE, delimiter=',')

    # Process the data: shift mean to 0 and scale standard deviation to 1
    mean_data = np.mean(data, axis=0)  # Compute mean along columns
    std_data = np.std(data, axis=0)    # Compute standard deviation along columns

    processed = (data - mean_data) / std_data  # Normalize the data

    # Save the processed data to OUTFILE using numpy.savetxt
    np.savetxt(OUTFILE, processed, delimiter=',', fmt='%.6f')

    print(f"Processed data saved to {OUTFILE}")
