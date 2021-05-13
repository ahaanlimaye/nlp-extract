# Imports
import stanza, os, re, argparse
from stanza.server import CoreNLPClient
from pathlib import Path
from pprint import pprint

# Main function
def main():
    parser = argparse.ArgumentParser(description="Summarize TXT file")
    parser.add_argument("filepath", type=dir_path, nargs="+", help="Filepath for TXT file")

    args = parser.parse_args()
    filepath = args.filepath[0]
    extract(filepath)

# Filepath datatype
def dir_path(path):
    if Path(path) and path[-4 : ] == '.txt':
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")  

# Extract function
def extract(txt):

    # Reads TXT file
    path = Path(txt)
    f = open(path, "r")
    text = f.read()
    f.close()

    # Initializes lists for extraction
    sentences = []
    emails = []
    phone_numbers = []
    kbp_triples = []

    # Phone and Emial regular expressions
    phone_regex = re.compile(r'''(
        (\d{3}|\(\d{3}\))? # area code
        (\s|-|\.)? # separator
        (\d{3}) # first 3 digits
        (\s|-|\.) # separator
        (\d{4}) # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
        )''', re.VERBOSE)
    email_regex = re.compile(r'''(
        [a-zA-Z0-9._%+-] + #username
        @                   # @symbole
        [a-zA-Z0-9.-] +     # domain
        (\.[a-zA-Z]{2,4})   # dot-something
        )''', re.VERBOSE)

    # Finds Phone and Emails in text and adds to respective lists
    for groups in phone_regex.findall(text):
        phone_num = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phone_num += ' x' + groups[8]
        phone_numbers.append(phone_num)
    for groups in email_regex.findall(text):
        emails.append(groups[0])

    # NLP Doc for text
    nlp = stanza.Pipeline(lang='en')
    doc = nlp(text)

    # Sets Environment Variable for Stanford CoreNLP
    corenlp_dir = './corenlp'
    os.environ['CORENLP_HOME'] = corenlp_dir

    # Opens CoreNLP Client and annotates text
    with CoreNLPClient(properties='./corenlp_server.props') as client:
        ann = client.annotate(text)

    # Iterates through sentences in annotated text and records sentiment, entities, and kbp triple in respective lists
    for i, sentence in enumerate(ann.sentence):
        sentence_obj = {}
        sentence_obj['text'] = doc.sentences[i].text
        sentence_obj['sentiment'] = sentence.sentiment
        sentence_obj['entities'] = [{'text': entity.entityMentionText, 'entity': entity.entityType} for entity in sentence.mentions]
        sentences.append(sentence_obj)
        if hasattr(sentence, 'kbpTriple'):
            for kbp in sentence.kbpTriple:
                kbp_triples.append({'subject': kbp.subject, 'relation': kbp.relation, 'object': kbp.object})

    # Writes extract to new file with "_extracted" suffix
    new_path = Path(str(path.parent) + "/" + str(path.stem) + "_extracted.txt")
    f = open(new_path, "w+")
    f.seek(0)
    for i, sentence in enumerate(sentences):
        f.write(f'Sentence #{i+1}: {sentence["text"]}\n')
        f.write(f'  Sentiment: {sentence["sentiment"]}\n')
        f.write('  Entities:\n')
        for e in sentence["entities"]:
            f.write(f'    - {e["entity"]} ({e["text"]})\n')
        f.write('\n')
    f.write('Emails\n')
    for email in emails:
        f.write(f'  - {email}\n')
    f.write('\n')
    f.write('Phone Numbers\n')
    for phone_number in phone_numbers:
        f.write(f'  - {phone_number}\n')
    f.write('\n')
    f.write('KBP Relations\n')
    for kbp in kbp_triples:
        f.write(f'  - Subject: {kbp["subject"]}, Relation: {kbp["relation"]}, Object: {kbp["object"]}\n')
    f.truncate()
    f.close()

    print(f'\nSuccessfully Extracted {path.name} in new file: {new_path.name}')

# Runs Main function
if __name__ == '__main__':
    main()