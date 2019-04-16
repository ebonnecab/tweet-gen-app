from flask import Flask, render_template
from generator import sentence_gen

HTML="""<html><head><title>My App</title></head>
        <body><h2>{}</h2></body>"""
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/words')
def tweet_gen():
    sentence = sentence_gen()
    return render_template('tweet_gen.html', quote = sentence)

#implementation where user can generate as many words as they want
# @app.route('/words/<int:num>')
# def tweet_gen2(num):
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
