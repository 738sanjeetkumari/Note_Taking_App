from flask import render_template, redirect, url_for, flash
from app import app, db
from models import Note
from forms import NoteForm

@app.route('/')
def home():
    notes = Note.query.order_by(Note.created_at.desc()).all()
    return render_template('home.html', notes=notes)

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    form = NoteForm()
    if form.validate_on_submit():
        new_note = Note(title=form.title.data, content=form.content.data)
        db.session.add(new_note)
        db.session.commit()
        flash('Note added successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('add_note.html', form=form)

@app.route('/delete/<int:id>')
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    flash('Note deleted successfully!', 'danger')
    return redirect(url_for('home'))
