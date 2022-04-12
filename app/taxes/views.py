from flask import Blueprint, render_template


taxes = Blueprint('taxes', __name__)


@taxes.route('/taxes')
@taxes.route('/taxes/index.html')
def taxes_home():
    return render_template('/taxes/index.html')