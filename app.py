from flask import Flask
from models import db
from controllers.pacientes_controller import pacientes_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Registrar blueprint
app.register_blueprint(pacientes_bp, url_prefix='/pacientes')

# Criar tabelas dentro do contexto da aplicação
with app.app_context():
    db.create_all()
    print("Banco criado com sucesso!")

if __name__ == '__main__':
    app.run(debug=True)
