# frename


## General Goals
We want to convert a variety of mistakes in filenames into more legal, standardized filenames. For example, the program should:
- recognize, replace, and illegal characters


## Specs

### Illegal characters
For this, we want to make sure all filenames are compatible with the "least common demoninator" in terms of what characters are allowed

`
$, #, %, &, {, }, \, <, >, *, ?, /, ' ', !, ', ", :, @, +, `, |, =
`

would love to catch the common ones that are like %20 (space) see [percent encoding](https://en.wikipedia.org/wiki/Percent-encoding) and convert them into '-', might have to be a first pass at the string kind of thing

parenthases could be optional parameter to remove them. in my bash shell, these need to be escaped so I would like to avoid them if at all possible

### Length
 under 30

if over limit, should always prompt for something 


### Examples


| Old                                 | New                                 | Comments                            |
| -----------                         | -----------                         | -----------                         |
| (SealePHYS111) Syllabus Fall 16.doc | seale-phys111-syllabus-fall-16.doc  |                                     |
| Rec+20+WS+solutions.pdf             | rec-20-ws-solution.pdf              |                                     |
| Sweet%20Victory%20-%20Tuba.pdf      | sweet-victory-tuba.pdf              |                                     |
| Template%20%28Yellow%20Card%29%20%  | template-(yellow-card)              |                                     |



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
