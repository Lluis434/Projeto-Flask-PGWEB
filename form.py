from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, FieldList, FormField, SubmitField
from wtforms.validators import DataRequired, Length

class CampoForm(FlaskForm):
    titulo_campo = StringField('Título do Campo', validators=[DataRequired(), Length(max=500)])
    tipo_resposta = SelectField(
        'Tipo de Resposta',
        choices=[('resposta_curta', 'Resposta Curta'),
                 ('resposta_longa', 'Resposta Longa'),
                 ('multi_escolha', 'Múltipla Escolha'),
                 ('caixa_selecao', 'Caixa de Seleção')],
        validators=[DataRequired()]
    )

class FormularioForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired(), Length(max=200)])
    descricao = TextAreaField('Descrição', validators=[DataRequired()])
    campos = FieldList(FormField(CampoForm), min_entries=1)
    submit = SubmitField('Criar Formulário')
