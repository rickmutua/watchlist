"""version 1.0.2

Revision ID: 6356556d742b
Revises: 7a0b894257ac
Create Date: 2017-10-24 15:51:22.507931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6356556d742b'
down_revision = '7a0b894257ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
