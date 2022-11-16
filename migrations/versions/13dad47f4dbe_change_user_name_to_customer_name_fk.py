"""change user_name to customer_name FK

Revision ID: 13dad47f4dbe
Revises: cd7188e63e10
Create Date: 2022-11-16 16:51:48.486084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13dad47f4dbe'
down_revision = 'cd7188e63e10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('test_bills_ibfk_2', 'test_bills', type_='foreignkey')
    op.create_foreign_key(None, 'test_bills', 'test_customers', ['customer_name'], ['fullname'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'test_bills', type_='foreignkey')
    op.create_foreign_key('test_bills_ibfk_2', 'test_bills', 'test_users', ['user_name'], ['fullname'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###
