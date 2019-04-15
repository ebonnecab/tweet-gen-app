from flask import Flask, render_template
from histogram import histogram
from histogram import histogram
from histogram import get_words
# from histogram import get_tokens
from histogram import listogram
from sample import sample
from rearrange import sentence_maker

HTML="""<html><head><title>My App</title></head>
        <body><h2>{}</h2></body>"""
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/words')
def tweet_gen():
    histo_text = get_words('siddhartha.txt')
    # clean_text = get_tokens(histo_text)
    histo = histogram(histo_text)
    random_word = sample(histo)
    random_words = []
    for i in range(7):
        random_words.append(sample(histo))
    random_sentence = sentence_maker(random_words)
    return HTML.format(random_sentence)

#implementation where user can generate as many words as they want
# @app.route('/words/<int:num>')
# def tweet_gen(num):
#     histo_text = get_words('siddhartha.txt')
#     clean_text = get_tokens(histo_text)
#     histo = histogram(clean_text)
#     random_word = sample(histo)
#     random_words = []
#     for i in range(num):
#         random_words.append(sample(histo))
#     random_sentence = sentence_maker(random_words)
#     return HTML.format(random_sentence)


if __name__ == '__main__':
    app.run(debug=True)
