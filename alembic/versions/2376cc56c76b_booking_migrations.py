"""booking Migrations

Revision ID: 2376cc56c76b
Revises: f5022e6549df
Create Date: 2023-03-12 18:10:11.363047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2376cc56c76b'
down_revision = 'f5022e6549df'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicle_Bookings',
    sa.Column('bookingNumber', sa.String(), nullable=False),
    sa.Column('empId', sa.String(), nullable=True),
    sa.Column('empUsername', sa.String(), nullable=True),
    sa.Column('userDepartment', sa.String(), nullable=True),
    sa.Column('tripDate', sa.DateTime(), nullable=True),
    sa.Column('startLocation', sa.String(), nullable=True),
    sa.Column('destination', sa.String(), nullable=True),
    sa.Column('startTime', sa.String(), nullable=True),
    sa.Column('endTime', sa.String(), nullable=True),
    sa.Column('vehicleAlloted', sa.String(), nullable=True),
    sa.Column('vehicleNumber', sa.String(), nullable=True),
    sa.Column('tripStatus', sa.Boolean(), nullable=True),
    sa.Column('tripCompleted', sa.Boolean(), nullable=True),
    sa.Column('tripCanceled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('bookingNumber')
    )
    op.create_index(op.f('ix_vehicle_Bookings_bookingNumber'), 'vehicle_Bookings', ['bookingNumber'], unique=False)
    op.drop_index('ix_accounts_empId', table_name='accounts')
    op.create_index(op.f('ix_accounts_empId'), 'accounts', ['empId'], unique=True)
    op.drop_index('ix_employeeId_empId', table_name='employeeId')
    op.create_index(op.f('ix_employeeId_empId'), 'employeeId', ['empId'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_employeeId_empId'), table_name='employeeId')
    op.create_index('ix_employeeId_empId', 'employeeId', ['empId'], unique=False)
    op.drop_index(op.f('ix_accounts_empId'), table_name='accounts')
    op.create_index('ix_accounts_empId', 'accounts', ['empId'], unique=False)
    op.drop_index(op.f('ix_vehicle_Bookings_bookingNumber'), table_name='vehicle_Bookings')
    op.drop_table('vehicle_Bookings')
    # ### end Alembic commands ###
