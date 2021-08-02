import argparse


default_illegal_characters = set(("$", "#", "%", "&", "{", "}", "\\", "<", ">", "*", "?", "/", ' ', "!", "'", '"', ":", "@", "+", "`", "|", "="))

print(default_illegal_characters)

def get_new_filename(old_filename: str) -> str:

    name_lower_case = old_filename.lower()
    new_name = ""

    for c in name_lower_case:
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
