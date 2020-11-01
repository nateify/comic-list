comic-list.py - Output a list of owned/missing issues of a comic book series in a single folder

# Installation
    pip install comic-list

# Description
comic-list.py will print a list of owned and missing issue numbers given a folder which contains comic book files with issue number in the file name.

Default supported extensions are: CBZ, CBR, CB7, CBA, CBT

When run no arguments it will use the following defaults:
- Get file names from current directory matching supported extensions
- Get the issue number immediately succeeding the `#` symbol
- Use the first and last issue numbers in the directory as the total range


     python comic-list

# Options     

You can view the arguments by running `python comic-list --help`

```
positional arguments:
  dir                   Input folder

optional arguments:
  -h, --help            show this help message and exit
  --start START, -s START
                        Starting number
  --end END, -e END     Ending number
  --digit-group [DIGIT_GROUP], -d [DIGIT_GROUP]
                        Nth digit group in file name that contains issue
                        number
  --filetype FILETYPE, -f FILETYPE
                        Custom file extension to check for
```

### Starting and ending number

By default the script will use the lowest and highest issue number from the files in the folder as the starting and ending points for the range. If the folder is missing the first and last issue in a series, manually specify these numbers.

### Digit group

By default the script will use regex to get the issue number from a file name immediately succeeding the `#` symbol.

If your file names do not contain the `#` symbol, you can call `--digit-group` with no arguments to grab the first set of digits in the file name as the issue number.

If the first set of digits in the file name is not the issue number, for example if the year preceeds the issue number in the file name, you can supply a number to `--digit-group` to specify which Nth group of digits in the file name is the issue number.

# [Examples](https://github.com/nateify/comic-list/tree/master/examples)
View the [examples](https://github.com/nateify/comic-list/tree/master/examples) folder for example output for each argument type