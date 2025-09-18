from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'troque-por-uma-chave-secreta-aqui'

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    name = None

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        if not name:
            error = '☛ Preencha este campo'
        else:
            return render_template('index.html', name=name)

    return render_template('index.html', name=None, error=error)

if __name__ == '__main__':
    app.run(debug=True)
