import argparse
from urllib.parse import unquote

default_illegal_characters = set(("$", "#", "%", "&", "{", "}", "\\", "<", ">", "*", "?", "/", ' ', "!", "'", '"', ":", "@", "+", "`", "|", "="))

print(default_illegal_characters)

def get_new_filename(old_filename: str) -> str:

    # unquote converts percent encoding to utf-8
    # convert to lower case
    temp_name = unquote(old_filename)
    temp_name = temp_name.lower()

    # rebuild name, converting illegal characters
    new_name = ""
    for c in temp_name:
        if c in default_illegal_characters:
            new_name += '-'
        else:
            new_name += c

    return new_name

if __name__ == "__main__":


    my_parser = argparse.ArgumentParser(description="Rename files to a given format")

    my_parser.add_argument('Path',
            metavar='path',
            type=str,
            help='list to the path')
    
    args = my_parser.parse_args()

    print(args.Path)
