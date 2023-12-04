def read_lines_from_file(file_path):
    """
    Reads lines from a file, trims whitespace, and ignores empty lines.

    Args:
    file_path (str): The path to the file to be read.

    Returns:
    list of str: The lines from the file.
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]


def read_lines_from_file(file_path, delimiter=None):
    """
    Reads lines from a file, trims whitespace, and optionally splits each line by a delimiter.

    Args:
    file_path (str): The path to the file to be read.
    delimiter (str, optional): The delimiter to split each line. Default is None.

    Returns:
    list of str or list of list of str: The lines from the file, optionally split by the delimiter.
    """
    with open(file_path, 'r') as file:
        if delimiter:
            return [line.strip().split(delimiter) for line in file if line.strip()]
        else:
            return [line.strip() for line in file if line.strip()]
