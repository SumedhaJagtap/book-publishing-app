from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required

from app import db
from app.catalog import catalog_bp
from app.catalog.models import Book, Publication
from app.catalog.forms import EditBookForm,CreateBookForm


@catalog_bp.route('/')
def display_books():
    books = Book.query.all()
    return render_template('home.html', books=books)


@catalog_bp.route('/publisher/<publisher_id>')
def display_publisher(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_books = Book.query.filter_by(pub_id=publisher.id).all()
    return render_template('publisher.html', publisher=publisher, publisher_books=publisher_books)


# DELETE will be not allowed from web
@catalog_bp.route('/book/<int:book_id>', methods=['GET', 'POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash('book deleted successfully')
        return redirect(url_for('catalog_bp.display_books'))
    return render_template('delete_book.html', book=book, book_id=book_id)


# DELETE will be not allowed from web
@catalog_bp.route('/book/edit/<int:book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    book = Book.query.get(book_id)

    form = EditBookForm()
    if form.validate_on_submit():
        book.title = form.title.data
        book.format = form.format.data
        book.num_pages = form.num_pages.data
        db.session.add(book)
        db.session.commit()
        flash('Book edited successfully')
        return redirect(url_for('catalog_bp.display_books'))
    return render_template('edit_book.html', form=form)


@catalog_bp.route('/create/book', methods=['GET', 'POST'])
@login_required
def create_book():
    form = CreateBookForm()
    
    if form.validate_on_submit():
        book = Book(title=form.title.data,
                    author=form.author.data,
                    avg_rating=form.avg_rating.data,
                    format=form.format.data,
                    image=form.img_url.data,
                    num_pages=form.num_pages.data,
                    pub_id=form.pub_id.data)
        db.session.add(book)
        db.session.commit()
        flash('Book added successfully')
        return redirect(url_for('catalog_bp.display_books'))
    return render_template('create_book.html', form=form)
