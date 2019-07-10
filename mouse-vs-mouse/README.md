# Mouse vs mouse

## How to run

There is executable module [mouse_vs_mouse](mouse_vs_mouse.py) which requires one position argument - input file and has two optional argument --animal and --computer-mouse for word sets (default are [animal.txt](animal.txt) and [computer-mouse.txt](computer-mouse.txt) from working directory)
e.g.
To run program for please execute:
```commandline
python -m mouse_vs_mouse input00.txt
```

To run program with custom word sets please execute:
```commandline
python -m mouse_vs_mouse input00.txt --animal <animal-set-path> --computer-mouse <computer-mouse-set-path>
```

### Word sets

This programs requires words set that are used for sentence analysis, such word set file should be a text file with words, each in separate line which are typical for given context. This repository contains example of such word sets.
```house
tail
rodent
genome
ears
...
```

Helpful in creation of such file can be [analyse](analyse.py) module which analyse example sentences in input (input00.txt -> input100.txt) and output and count occurrences of words in those sentences.

Example output of analyse module.
```
computer-mouse

13      a
13      mouse
8       the
7       your
6       to
...

animal

22      the
20      mouse
8       a
7       is
5       in
5       of
...
```

## How to run tests

This project use [pytest](https://docs.pytest.org/en/latest/) for testing, to install please execute:
```commandline
pip install -r requirements-dev.txt
```
Then to run all test in this project please execute:
```commandline
python -m pytest
``` 