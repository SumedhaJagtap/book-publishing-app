from flask import Blueprint

catalog_bp = Blueprint('catalog_bp',__name__,template_folder='templates')

from app.catalog import routes