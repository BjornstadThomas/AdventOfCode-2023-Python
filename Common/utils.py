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

