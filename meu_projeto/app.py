from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

# Configuração do banco de dados
db = pymysql.connect(
    host="italo.mysql.uhserver.com",
    user="logica2024",
    password="@Aluno2024",
    database="italo"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    choice = request.form['choice']
    
    # Inserir escolha no banco de dados
    cursor = db.cursor()
    sql = "INSERT INTO escolhas (escolhas) VALUES (%s)"
    cursor.execute(sql, (choice,))
    db.commit()
    
    return f"Você escolheu: {choice}"

if __name__ == '__main__':
    app.run(debug=True)
