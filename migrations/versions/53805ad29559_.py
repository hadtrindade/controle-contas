"""empty message

Revision ID: 53805ad29559
Revises: 9bf983604b82
Create Date: 2021-11-06 21:09:30.948201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53805ad29559'
down_revision = '9bf983604b82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('detailed_invoice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('value', sa.Numeric(), nullable=True),
    sa.Column('revenue', sa.Boolean(), nullable=True),
    sa.Column('id_invoice', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_invoice'], ['invoice.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('detailed_invoice')
    # ### end Alembic commands ###
