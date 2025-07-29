from flask import Blueprint, request, render_template, redirect, url_for, flash
from db import get_connection  # sin prefijos ni puntos

contacts = Blueprint('contacts', __name__, template_folder='templates')

@contacts.route('/')
def Index():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM Usuario')
        data = cur.fetchall()
    return render_template('index.html', contacts=data)

@contacts.route('/add_contact', methods=['POST'])
def add_contact():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    correo = request.form['correo']
    try:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Usuario (nombre, telefono, correo) VALUES (?, ?, ?)",
                (nombre, telefono, correo)
            )
            conn.commit()
            flash('Contacto agregado exitosamente')
    except Exception as e:
        flash(f'Error al agregar contacto: {e}')
    return redirect(url_for('contacts.Index'))

@contacts.route('/edit/<id>')
def get_contact(id):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM Usuario WHERE id = ?', (id,))
        data = cur.fetchone()
    return render_template('edit-contact.html', contact=data)

@contacts.route('/update/<id>', methods=['POST'])
def update_contact(id):
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    correo = request.form['correo']
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            UPDATE Usuario
            SET nombre = ?, correo = ?, telefono = ?
            WHERE id = ?
        """, (nombre, correo, telefono, id))
        conn.commit()
        flash('Contacto actualizado correctamente')
    return redirect(url_for('contacts.Index'))

@contacts.route('/delete/<string:id>')
def delete_contact(id):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute('DELETE FROM Usuario WHERE id = ?', (id,))
        conn.commit()
        flash('Contacto eliminado correctamente')
    return redirect(url_for('contacts.Index'))
