"""mail verification

Revision ID: 812065fb9960
Revises: d904721fa870
Create Date: 2023-04-14 09:06:44.802938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '812065fb9960'
down_revision = 'd904721fa870'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Email_Verification',
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('otp', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    op.create_index(op.f('ix_Email_Verification_email'), 'Email_Verification', ['email'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Email_Verification_email'), table_name='Email_Verification')
    op.drop_table('Email_Verification')
    # ### end Alembic commands ###
