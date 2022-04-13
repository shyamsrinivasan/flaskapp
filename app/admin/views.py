from flask import Blueprint, render_template


admin_bp = Blueprint('admin', __name__, template_folder='templates')


@admin_bp.route('/admin')
@admin_bp.route('/admin/index.html')
def index():
    return render_template('/index.html')


# @admin.route('/admin/clients')
# @admin.route('/admin/clients/index.html')
# def admin_clients():
#     return render_template('/admin/clients')