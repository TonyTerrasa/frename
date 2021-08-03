import argparse
from urllib.parse import unquote
from copy import copy

default_illegal_characters = set(("$", "#", "%", "&", "{", "}", "\\", "<", ">", "*", "?", "/", ' ', "!", "'", '"', ":", "@", "+", "`", "|", "="))

def get_new_filename(old_filename: str) -> str:

    # unquote converts percent encoding to utf-8
    # convert to lower case
    temp_name = unquote(old_filename)
    temp_name = temp_name.lower()

    # rebuild name, converting illegal characters
    rm_illegal = ""
    for c in temp_name:
        if c in default_illegal_characters:
            rm_illegal += '-'
        else:
            rm_illegal += c

    # remove extra instances of '-'
    new_name = copy(rm_illegal)
    changed = True
    while changed:
        old_string = copy(new_name)
        changed = False
        new_name = ""
        for i, c in enumerate(old_string):
            if c == '-':
                # beginning
                if i == 0: 
                    changed = True
                    continue
                # repeat '-'
                if old_string[i-1] == '-': 
                    changed = True
                    continue
                # at end of entire name 
                if i == len(old_string)-1:
                    changed = True
                    continue
                # at end of name before extension
                if i+1 < len(old_string) and old_string[i+1] == '.': 
                    changed = True
                    continue

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
