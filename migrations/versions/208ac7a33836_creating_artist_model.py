"""Creating Artist Model

Revision ID: 208ac7a33836
Revises: b45bf8478254
Create Date: 2021-12-07 15:19:50.132955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '208ac7a33836'
down_revision = 'b45bf8478254'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.String(length=128), nullable=False),
    sa.Column('artist_name', sa.String(length=128), nullable=False),
    sa.Column('genres', sa.String(length=128), nullable=False),
    sa.Column('artist_url', sa.String(length=128), nullable=False),
    sa.Column('artist_img_url', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('artist_id'),
    sa.UniqueConstraint('artist_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('artists')
    # ### end Alembic commands ###
