This Python script will extract the canonical, legal, and definitely correct color of any file on your computer!

Rejoice, colorists, for the days of guessing are over! just run `python main.py <path_to_file>` and you will be greeted with the color of your file in no time!


## Installation
1. Question if you *really* need this
2. Make sure you really do need this
3. Clone this repository
4. Run `python main.py <path_to_file>`
5. it really is not that hard

## Usage
`python main.py <path_to_file>`


## Pre-requisites
- A sane version of Python
- A file you want to know the color of
- A computer
- `python main.py <path_to_file>`
- a cat (optional but recommended)

## Acknowledgements
- My mom for always believing in me
- My friends for their unwavering support
- StackOverflow

## Steps to build
Bui- what? Why would you want to build this? It's a Python script. Just run it.

## How it works
Jokes aside, this script fetches the file requested, reads its size in bytes, subtracts its own CRC32 hash from its size, 
then seeks to the resulting position in the file and reads the next 3 bytes. These 3 bytes are then converted to a hexadecimal string, printed, and returned.