from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

# robert = 79
@app.route('/rizz/<int:robert>')
def rizz_calculation(robert):
    return f'Your rizz calculation is {robert}%'

@app.route('/entry/<int:score>')
def entry_pass(score):
    if score > 60:
        return "you can enter the party"
    else:
        return redirect(url_for('rizz_calculation'))

if __name__== '__main__':
    app.run(debug=True)