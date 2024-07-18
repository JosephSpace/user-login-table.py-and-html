# api.py

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Veritabanı bağlantısını oluştur
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Kullanıcılar tablosunu oluştur
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        department TEXT NOT NULL,
        position TEXT NOT NULL
    )
''')

# Değişiklikleri kaydet ve bağlantıyı kapat
conn.commit()
conn.close()

# Ana sayfa, kullanıcıları gösteren endpoint
@app.route('/')
def index():
    # Veritabanından kullanıcıları al
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    users = cursor.fetchall()
    conn.close()

    return render_template('index.html', users=users)

# Yeni kullanıcı eklemek için endpoint
@app.route('/add_employee', methods=['POST'])
def add_employee():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    department = request.form['department']
    position = request.form['position']

    # Veritabanına kullanıcı ekle
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO employees (first_name, last_name, department, position)
        VALUES (?, ?, ?, ?)
    ''', (first_name, last_name, department, position))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

# Kullanıcıyı silmek için endpoint
@app.route('/delete_employee/<int:user_id>', methods=['POST'])
def delete_employee(user_id):
    # Veritabanından kullanıcıyı sil
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
