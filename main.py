from flask import Flask
from contacts import contacts  # import directo porque están al mismo nivel

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Registro del Blueprint
app.register_blueprint(contacts)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
