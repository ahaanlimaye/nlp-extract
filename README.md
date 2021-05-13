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
- After running, a new extracted TXT file with the suffix "_extracted" will be created in the same directory as the original file
```
python extract.py [TXT_FILEPATH]
```

## Example
```
>>> python extract.py samples/sample.txt
...

Successfully Extracted sample.txt in new file: sample_extracted.txt
```
sample.txt:
```
John lives in California. 
His email is johndoe@gmail.com and his number is 592-483-4942. 
John loves to go swimming! 
Peter lives in New York. 
His email is peter@outlook.com and his number is 394-548-4392. 
Peter loves to go fishing!
```
sample_extracted.txt:
```
Sentence #1: John lives in California.
  Sentiment: Neutral
  Entities:
    - PERSON (John)
    - STATE_OR_PROVINCE (California)

Sentence #2: His email is johndoe@gmail.com and his number is 592-483-4942.
  Sentiment: Neutral
  Entities:
    - EMAIL (johndoe@gmail.com)
    - NUMBER (592-483-4942)
    - PERSON (His)
    - PERSON (his)

Sentence #3: John loves to go swimming!
  Sentiment: Neutral
  Entities:
    - PERSON (John)

Sentence #4: Peter lives in New York.
  Sentiment: Neutral
  Entities:
    - PERSON (Peter)
    - STATE_OR_PROVINCE (New York)

Sentence #5: His email is peter@outlook.com and his number is 394-548-4392.
  Sentiment: Neutral
  Entities:
    - EMAIL (peter@outlook.com)
    - NUMBER (394-548-4392)
    - PERSON (His)
    - PERSON (his)

Sentence #6: Peter loves to go fishing!
  Sentiment: Positive
  Entities:
    - PERSON (Peter)

Emails
  - johndoe@gmail.com
  - peter@outlook.com

Phone Numbers
  - 592-483-4942
  - 394-548-4392

KBP Relations
  - Subject: John, Relation: per:statesorprovinces_of_residence, Object: California
  - Subject: Peter, Relation: per:statesorprovinces_of_residence, Object: New York
```
