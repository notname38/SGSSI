# SGSSI 2021

This is a repository for the subject SGSSI 2021. Be sure to read the following to properly use the programs here.

## Installation

Be sure you have python 3 installed, alongside it's standart programming libraries.


## Usage

### File checker 

How to use the file checker:

```bash
python3 fileChecker.py
```
You will be prompted to input two files. These files must be in the same folder as the program.

Example 

```bash
python3 fileChecker.py

"Whats the original file?"
test.txt

"Whats the file to be checked? "
testHash.txt

File is correct.
```

### Miner 

How to use the miner:

```bash
python3 miner.py
```
You will be prompted to fill several inputs. All of them must be filled except for the extra filler question. 
If no extra filler is required, just press enter.

Example 

```bash
python3 miner.py

"How long should the filler be?"
8                               # Must be a positive integer.

"Should any extra string be added to the filler?"
aeiou                           # If empty just press enter.

"How many minutes shall the program run?"
5                               # Must be a positive integer.

"Please type the file to be mined (must be in the same folder)"
test.txt

```

Output will be provided on an output file.

## MD5 of each python file

>fileChecker.py: e2a84ca7aaac99ea3d02fdb5d50e4188

>miner.py: 9e09b65f5ac15566e7e5546eabd40ead

## License
[MIT](https://choosealicense.com/licenses/mit/)