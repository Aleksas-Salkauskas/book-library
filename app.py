from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-please-change')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    year_published = db.Column(db.Integer)
    isbn = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Book {self.title}>'

# Create tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/search')
def search():
    query = request.args.get('query', '')
    if query:
        books = Book.query.filter(
            (Book.title.contains(query)) | 
            (Book.author.contains(query))
        ).all()
    else:
        books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/genre/<genre>')
def filter_by_genre(genre):
    books = Book.query.filter_by(genre=genre).all()
    return render_template('index.html', books=books)

@app.route('/book/<int:id>')
def book_detail(id):
    book = Book.query.get_or_404(id)
    return render_template('book_detail.html', book=book)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        description = request.form.get('description', '')
        year_published = request.form.get('year_published', type=int)
        isbn = request.form.get('isbn', '')
        
        new_book = Book(
            title=title,
            author=author,
            genre=genre,
            description=description,
            year_published=year_published,
            isbn=isbn
        )
        db.session.add(new_book)
        db.session.commit()
        flash('Book added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_book.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = Book.query.get_or_404(id)
    
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.genre = request.form['genre']
        book.description = request.form.get('description', '')
        book.year_published = request.form.get('year_published', type=int)
        book.isbn = request.form.get('isbn', '')
        
        db.session.commit()
        flash('Book updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit_book.html', book=book)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash('Book deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)