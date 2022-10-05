import os

BOOKS_FOLDER = "./books/"

def get_textfile_names() -> list:
    """
    Looks for .txt files in the folder ./books/ 
    Returns a list of strings containing 0...n filenames (.txt files only)
    """

    txt_list = []
    for row in os.listdir(BOOKS_FOLDER):
        if row.endswith(".txt"):
            txt_list.append(BOOKS_FOLDER + row)
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

    return len(text.split(sep=None))


def count_characters(text: str) -> list:
    """
    Counts the appearance of single characters inside a text.
    Input: text (string)
    Returns character count (list of lists)
    """

    text = text.lower()
    charcount = {}
    for char in text:
        if char in charcount:
            charcount[char] += 1
        elif char.isalpha():
            charcount[char] = 1
    charcount = list(zip(charcount.keys(), charcount.values())) 
    charcount.sort(reverse=True, key=lambda x: x[1])
    return charcount


def assemble_report(verbose_filename: str, wordcount: int, charcount: list) -> str:
    """
    Assembles a report on a textfile.
    Input: verbose_filename (str), wordcount (int), charcount(list)
    Returns: Report (str)
    """
    report = f"---Reporting on {verbose_filename}.---\n"
    report += f"{wordcount} word(s) found in the document.\n"
    for char in charcount:
        report += f"\nCharacter '{char[0]} was found {char[1]} time(s)."
    return report


def main():
    txt_files = get_textfile_names()
    opened_text = read_single_txt(txt_files[0])
    report = assemble_report(
        txt_files[0],
        count_words(opened_text),
        count_characters(opened_text)
        )
    print(report)

main()