from flask import Flask, render_template, url_for, redirect, request
from settings import url, db
from models import Formulario, Campo
from form import FormularioForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SECRET_KEY'] = 'chavedesegurancaproprojetoflask100atualizada'
db.init_app(app)
csrf = CSRFProtect(app)

@app.route('/', methods=['GET','POST'])
def criar_form():
   form = FormularioForm()

   if form.validate_on_submit():
        titulo = form.titulo.data
        descricao = form.descricao.data
        novo_formulario = Formulario(titulo=titulo, descricao=descricao)

        db.session.add(novo_formulario)
        db.session.commit()

        print(f"ID do novo formulário: {novo_formulario.id}")

        for campo_form in form.campos:
            titulo_campo = campo_form.titulo_campo.data
            tipo_resposta = campo_form.tipo_resposta.data

            novo_campo = Campo(titulo_campo=titulo_campo, tipo_campo=tipo_resposta, formulario_id=novo_formulario.id)
            db.session.add(novo_campo)

        db.session.commit()
        return redirect(url_for('consultar_form'))
   else:
        print(form.errors)

   return render_template('form.html', form=form)

@app.route('/consul_form/')
def consultar_form():
   formularios = Formulario.query.all()
   return render_template("consul_form.html", formularios=formularios)

   
@app.route('/deletar_form/<int:formulario_id>', methods=['GET'])
def deletar_form(formulario_id):
    formulario = Formulario.query.get_or_404(formulario_id)
    db.session.delete(formulario)
    db.session.commit()
    
    return redirect(url_for('consultar_form'))

@app.route('/editar_form/<int:formulario_id>', methods=['GET', 'POST'])
def editar_form(formulario_id):
   formulario = Formulario.query.get_or_404(formulario_id)
   form = FormularioForm(obj=formulario)

   if form.validate_on_submit():
      formulario.titulo = form.titulo.data
      formulario.descricao = form.descricao.data
      
      db.session.commit()
      return redirect(url_for('consultar_form'))

   return render_template('editar_form.html', form=form, formulario=formulario)

if __name__ == '__main__':
   with app.app_context():
      db.create_all()
   app.run(debug=True)