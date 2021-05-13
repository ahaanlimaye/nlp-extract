# NLP Exract
Python Script that extracts information from a TXT file using NLP

## Installation
Git Clone this Repository and CD into Repository:
```
git clone https://github.com/ahaanlimaye/nlp_extract
```
```
cd nlp_extract
```
Install Dependencies
```
pip install stanza
```
Run `install.py` to install CoreNLP Models
```
python install.py
```

## Usage
- Run `extract.py` with the filepath to a TXT file as an argument (This can easily be done by dragging and dropping your file into the command line window)
- After running, a new extract TXT file with the suffix "_extracted" will be created in the same directory as the original file
```
python extract.py [TXT_FILEPATH]
```

## Example
```
>>> python extract.py samples/sample.txt
...

Successfully Extracted sample.txt in new file: sample_extracted.txt
```
