import os
import string

def get_textfile_names() -> list:
    """
    Looks for .txt files in the folder ./books/ 
    Returns a list of strings containing 0...n filenames (.txt files only)
    """

    txt_list = []
    for row in os.listdir("./books/"):
        if row.endswith(".txt"):
            txt_list.append(row)
    return txt_list


def read_single_txt(verbose_filename: string) -> string:
    """
    Reads a single text file.
    Parameter: verbose_filename (string), a combination of path and filename.
    Returns a large string containing the text file content.
    """
    
    with open(verbose_filename) as f:
        file_content = f.read()
    return file_content


def count_words(text: string) -> int:
    """
    Counts words of a text.
    Parameter: text (string)
    Returns wordcount (integer)
    """

    return text.split(sep=None, maxsplit=None)


def count_letters(text: string) -> dict:
    """
    Counts the appearance of single letters inside a text.
    Parameter: text (string)
    Returns lettercount (dict)
    """

    