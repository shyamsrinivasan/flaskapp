from flask import Blueprint, render_template


admin = Blueprint('admin', __name__)


@admin.route('/admin')
@admin.route('/admin/index.html')
def admin_home():
    return render_template('/admin/index.html')


# @admin.route('/admin/clients')
# @admin.route('/admin/clients/index.html')
# def admin_clients():
#     return render_template('/admin/clients')