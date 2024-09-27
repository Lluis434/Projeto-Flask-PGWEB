from settings import db

class Formulario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    campos = db.relationship('Campo', backref='formulario', lazy=True)

class Campo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo_campo = db.Column(db.String(500), nullable=False)
    tipo_campo = db.Column(db.String(50), nullable=False)
    formulario_id = db.Column(db.Integer, db.ForeignKey('formulario.id'), nullable=False)
    opcoes = db.relationship('Opcoes', backref='campo', lazy=True)

    def get_tipo_resposta(self):
        tipos = {
            'resposta_curta': 'Resposta Curta',
            'resposta_longa': 'Resposta Longa',
            'multi_escolha': 'Múltipla Escolha',
            'caixa_selecao': 'Caixa de Seleção'
        }
        return tipos.get(self.tipo_campo, 'Tipo Desconhecido')

    def multi_escolha(self):
        return self.tipo_campo == "multi_escolha"
    
    def caixa_selecao(self):
        return self.tipo_campo == "caixa_selecao"
    
class Opcoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo_alternativa = db.Column(db.String(200), nullable=False)
    campo_id = db.Column(db.Integer, db.ForeignKey('campo.id'), nullable=False)

