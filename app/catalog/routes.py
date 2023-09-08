from flask import render_template

from app.catalog import catalog_bp
from app.catalog.models import Book, Publication

@catalog_bp.route('/')
def display_books():
    books = Book.query.all()
    return render_template('home.html',books=books)


@catalog_bp.route('/publisher/<publisher_id>')
def display_publisher(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_books = Book.query.filter_by(pub_id=publisher.id).all()
    return render_template('publisher.html',publisher= publisher,publisher_books=publisher_books)