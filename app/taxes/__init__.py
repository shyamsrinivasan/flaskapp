from flask import Blueprint


taxes_bp = Blueprint('taxes', __name__, template_folder='templates')
from . import views
