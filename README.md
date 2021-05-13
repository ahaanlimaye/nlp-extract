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
Sentence #0: John lives in California.
	Sentiment: Neutral
	Entities:
		- entity: PERSON (John)
		- entity: STATE_OR_PROVINCE (California)

Sentence #1: His email is johndoe@gmail.com and his number is 592-483-4942.
	Sentiment: Neutral
	Entities:
		- entity: EMAIL (johndoe@gmail.com)
		- entity: NUMBER (592-483-4942)
		- entity: PERSON (His)
		- entity: PERSON (his)

Sentence #2: John loves to go swimming!
	Sentiment: Neutral
	Entities:
		- entity: PERSON (John)

Sentence #3: Peter lives in New York.
	Sentiment: Neutral
	Entities:
		- entity: PERSON (Peter)
		- entity: STATE_OR_PROVINCE (New York)

Sentence #4: His email is peter@outlook.com and his number is 394-548-4392.
	Sentiment: Neutral
	Entities:
		- entity: EMAIL (peter@outlook.com)
		- entity: NUMBER (394-548-4392)
		- entity: PERSON (His)
		- entity: PERSON (his)

Sentence #5: Peter loves to go fishing!
	Sentiment: Positive
	Entities:
		- entity: PERSON (Peter)

Emails
	- johndoe@gmail.com
	- peter@outlook.com

Phone Numbers
	- 592-483-4942
	- 394-548-4392

KBP Relations
	- Object: California, Relation: per:statesorprovinces_of_residence, Subject: John
	- Object: New York, Relation: per:statesorprovinces_of_residence, Subject: Peter
```
