from blingfire import text_to_sentences
from glob import glob
import os

excluded_sentences = {
    'All right.',
    'All right?',
    'Never mind.',
    'OK.',
    'OK?',
    'Understand?',
}

def transcript_to_article(dir_in) -> str:
    txt_file = glob(os.path.join(dir_in, '*.txt'))[0]
    with open(txt_file) as f:
        s = f.read()
    s = s.replace('\n', ' ')
    return '\n'.join(
        (
            sentence
            for sentence in text_to_sentences(s).split('\n')
            if sentence not in excluded_sentences
        )
    )

if __name__ == '__main__':
    dir_in = 'transcribe-out'
    print(transcript_to_article(dir_in))
