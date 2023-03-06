import os


def save_markdown_file(markdown_text: str, file_path: str, name: str) -> None:
    """
    Saves the given markdown text to a new file with the given name at the specified file path.

    Args:
        markdown_text (str): The markdown text to save.
        file_path (str): The directory where the new markdown file should be saved.
        name (str): The name to give the new markdown file.

    Returns:
        None
    """
    # Create the full file path by joining the directory and file name
    full_file_path = os.path.join(file_path, name)

    # Write the markdown text to the new file
    with open(full_file_path, "w") as file:
        file.write(markdown_text)
