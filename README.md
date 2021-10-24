# SGSSI 2021

This is a repository for the subject SGSSI 2021. Be sure to read the following to properly use the programs here.

## Installation

Be sure you have python 3 installed, alongside it's standart programming libraries.


## Usage

### File checker 1
These file checker makes sure that both files start with the same content, and the second file contains the following extra:

> Last line must contain the SHA256 of the first file.

How to use the file checker:

```bash
python3 fileChecker_1.py
```
You will be prompted to input two files. These files must be in the same folder as the program.

Example 

```bash
python3 fileChecker_1.py

"Whats the original file?"
test.txt

"Whats the file to be checked? "
testHash.txt

File is correct.
```

### File checker 2
These file checker makes sure that both files start with the same content, and the second file contains the following extra:

> Last line must contain 8 hex characters followed by a blank and the group id.

How to use the file checker 2:

```bash
python3 fileChecker_2.py
```
You will be prompted to input two files. These files must be in the same folder as the program.

Example 

```bash
python3 fileChecker_2.py

"Whats the original file?"
testFiller.txt

"Whats the file to be checked? "
test2Filler.txt

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

>fileChecker_1.py: 37d2effce4e51e7dccafcffe6fea8cdd

>fileChecker_2.py: d86c27d08a6f70edcf631f5af9c36b3c

>miner.py: 0553f81fe39dc6000949b563b09b9e28

## License
[MIT](https://choosealicense.com/licenses/mit/)