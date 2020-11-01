# Examples

The examples directory in this repo contains dummy files using file names sourced from scene scans of public domain comic books.

This repository does not condone the illicit distribution of copyrighted works.

## No arguments, run in a directory with files with pound symbols

```
$ cd pound
$ comic-list

Have list:
5-7,9,10

Miss List:
8
```

## Supplying folder input

```
$ comic-list examples\pound

Have list:
5-7,9,10

Miss List:
8
```

## Supplying start and end issue numbers

```
$ comic-list examples\pound -s 1 -e 11

Have list:
5-7,9,10

Miss List:
1-4,8,11
```

## When the first digit group in the file name is the issue number

```
$ comic-list examples\second_digit -s 1 -e 6 -d 2

Have list:
5-7,9,10

Miss List:
1-4,8,11
```

## When the second digit group in the file name is the issue number

```
$ comic-list examples\second_digit -s 1 -e 6 -d 2

Have list:
6

Miss List:
1-5
```
