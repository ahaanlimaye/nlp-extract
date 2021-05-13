# Imports
import stanza, os

# Main function
def main():
    # Sets Environment Variable
    corenlp_dir = './corenlp'
    os.environ['CORENLP_HOME'] = corenlp_dir

    # Installs NLP Models
    stanza.install_corenlp(dir=corenlp_dir)
    stanza.download_corenlp_models(model='english-kbp', version='4.1.0', dir=corenlp_dir)

# Runs Main function
if __name__ == '__main__':
    main()