"""empty message

Revision ID: 8dfda4598cb
Revises: 33ac513415ea
Create Date: 2017-09-11 16:50:18.914000

"""

# revision identifiers, used by Alembic.
revision = '8dfda4598cb'
down_revision = '33ac513415ea'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tbl_category', 'img_category',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('tbl_item', 'img_item',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('tbl_users', 'password',
               existing_type=sa.VARCHAR(length=35),
               nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tbl_users', 'password',
               existing_type=sa.VARCHAR(length=35),
               nullable=False)
    op.alter_column('tbl_item', 'img_item',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('tbl_category', 'img_category',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    ### end Alembic commands ###
