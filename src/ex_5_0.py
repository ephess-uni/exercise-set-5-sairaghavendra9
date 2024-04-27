"""ex_5_0.py"""


def line_count(infile):
    """
    Counts the number of lines in the specified input file and prints the count.
    
    Args:
        infile (Path): The full path to the input file.
    """
    try:
        with open(infile, 'r') as file:
            lines = file.readlines()  # Read all lines into a list
            num_lines = len(lines)     # Count the number of lines
            print(f"Number of lines in '{infile}': {num_lines}")
    except FileNotFoundError:
        print(f"Error: File '{infile}' not found.")

if __name__ == "__main__":
    try:
    # get the utility function for path discovery
        try:
            from src.util import get_repository_root
        except ImportError:
            from util import get_repository_root

    # Test line_count with a file from the data directory
        data_directory = get_repository_root() / "data"
        line_count(data_directory / "ex_5_2-data.csv")
        repository_root = get_repository_root()
        
        # Construct the full path to the data directory and the specific file
        data_directory = repository_root / "data"
        data_file_path = data_directory / "ex_5_2-data.csv"
        
        # Test the line_count function with the specified file
        line_count(data_file_path)
        
    except Exception as e:
        print(f"Error: {e}")
