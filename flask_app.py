from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    institution = None
    discipline = None

    if request.method == 'POST':
        if request.form.get('name'):
            name = request.form.get('name').strip()
        if request.form.get('institution'):
            institution = request.form.get('institution').strip()
        if request.form.get('discipline'):
            discipline = request.form.get('discipline').strip()

    return render_template(
        'index.html',
        name=name,
        institution=institution,
        discipline=discipline
    )

if __name__ == '__main__':
    app.run()
