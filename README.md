# frename


## General Goals
Rename filenames to fit within a stardard schema for uniformity, ease of reading, and ease of access on the command line. The currently used schema fits into the guidelines within [File Naming Conventions in Linux](http://www.linfo.org/file_name.html) page of the [Linux Information Project website](http://linfo.org/).

## Specs

The following conventions will be used (checked as implemented):
- [x] all lower-case letters
- [x] removal of spaces and replacement of dashes as word separators
- [x] no repeat dashes

### Illegal characters
The following characters are considered illegal and will be removed from file names. 

```
$, #, %, &, {, }, \, <, >, *, ?, /, ' ', !, ', ", :, @, +, `, |, = 
```

would love to catch the common ones that are like %20 (space) see [percent encoding](https://en.wikipedia.org/wiki/Percent-encoding) and convert them into '-', might have to be a first pass at the string kind of thing. This can be easily accomplished with [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html).

parenthases could be optional parameter to remove them. in my bash shell, these need to be escaped so I would like to avoid them if at all possible

### Length
To account for UTF-8 filenames in Linux, the detail maximum length of a name will be 255 characters.

### Examples

| Old                                 | New                                 | Comments                            |
| -----------                         | -----------                         | -----------                         |
| hello-there-my-name-is-joe.txt      | hello-there-my-name-is-joe.txt      | no changes                          |
| (Foo PHYS111) Syllabus Fall 16.doc  | foo-phys111-syllabus-fall-16.doc    | remove parens and spaces            |
| Rec+20+WS+solutions<<.pdf           | rec-20-ws-solution.pdf              | remove +, <                         |
| Template%20%28Yellow%20Card%29%20%  | template-(yellow-card)              | convert percent encoding            |
| Sweet%20Victory%20-%20Tuba.pdf      | sweet-victory-tuba.pdf              | convert percent encoding, remove repeat `-`                                    |



## Making Corrections

The default behavior:

frename [options] file

```
if file is dir:
    suggest name edit for the directory (give the suggestion and prompt user for y/n to change)
    ask if you'd like to rename files in that directory
        if scanning a directory, provide a report of the proposed changes, then allow for confirm or deny, maybe something like edit with [qmv](http://manpages.org/qmv)
    
if it is a file:
    suggest name edit for the file (give the suggestion and prompt the user for y/n)
        
director
```


## Future Work
- detect abreviations (strings of many upper-case letterswords)
- ability to add your own string of illegal characters
