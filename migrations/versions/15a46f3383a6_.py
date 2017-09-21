"""empty message

Revision ID: 15a46f3383a6
Revises: 8dfda4598cb
Create Date: 2017-09-15 17:53:29.311000

"""

# revision identifiers, used by Alembic.
revision = '15a46f3383a6'
down_revision = '8dfda4598cb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'tbl_interested_id_item_fkey', 'tbl_interested', type_='foreignkey')
    op.drop_constraint(u'tbl_interested_userid_fkey', 'tbl_interested', type_='foreignkey')
    op.drop_column('tbl_interested', 'id_item')
    op.drop_column('tbl_interested', 'userid')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tbl_interested', sa.Column('userid', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('tbl_interested', sa.Column('id_item', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key(u'tbl_interested_userid_fkey', 'tbl_interested', 'tbl_users', ['userid'], ['id'])
    op.create_foreign_key(u'tbl_interested_id_item_fkey', 'tbl_interested', 'tbl_item', ['id_item'], ['id'])
    ### end Alembic commands ###
