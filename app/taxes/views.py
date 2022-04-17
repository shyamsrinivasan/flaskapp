from flask import Blueprint, render_template
from . import taxes_bp


@taxes_bp.route('/taxes')
@taxes_bp.route('/taxes/index.html')
def taxes_home():
    return render_template('/index.html')
