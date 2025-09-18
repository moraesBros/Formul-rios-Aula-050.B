from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Inicializa valores e erros
    name = ''
    institution = ''
    discipline = ''
    errors = {}

    if request.method == 'POST':
        # Captura e limpa cada campo
        name        = request.form.get('name', '').strip()
        institution = request.form.get('institution', '').strip()
        discipline  = request.form.get('discipline', '').strip()

        # Validação de vazio
        if not name:
            errors['name'] = 'Preencha esse campo'
        if not institution:
            errors['institution'] = 'Preencha esse campo'
        if not discipline:
            errors['discipline'] = 'Preencha esse campo'

    return render_template(
        'index.html',
        name=name,
        institution=institution,
        discipline=discipline,
        errors=errors
    )

if __name__ == '__main__':
    app.run()
