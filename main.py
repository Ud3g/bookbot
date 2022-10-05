import os

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


def read_single_txt(verbose_filename: str) -> str:
    """
    Reads a single text file.
    Input: verbose_filename (string), a combination of path and filename.
    Returns a large string containing the text file content.
    """
    
    with open(verbose_filename) as f:
        file_content = f.read()
    return file_content


def count_words(text: str) -> int:
    """
    Counts words of a text.
    Input: text (string)
    Returns wordcount (integer)
    """

    return text.split(sep=None, maxsplit=None)


def count_letters(text: str) -> dict:
    """
    Counts the appearance of single characters inside a text.
    Input: text (string)
    Returns character count (dict)
    """

    text = text.lower()
    charcount = {}
    for char in text:
        if char in charcount:
            charcount[char] += 1
        elif char.isalpha():
            charcount[char] = 1
    charcount = sorted(charcount, reverse=True)
    return charcount


def assemble_report() -> str:
    """
    Assembles a report on a textfile.
    Input: verbose_filename (str), wourdcount (int), charcount(dict)
    Returns: Report (str)
    """
    pass


def main():
    pass

main()