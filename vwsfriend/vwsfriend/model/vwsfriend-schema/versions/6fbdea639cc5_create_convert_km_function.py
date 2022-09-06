"""create convert_km function

Revision ID: 6fbdea639cc5
Revises: f917fc564c1d
Create Date: 2022-09-02 20:49:51.707701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fbdea639cc5'
down_revision = 'f917fc564c1d'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE FUNCTION convert_km(n double precision, unit text) RETURNS double precision AS $$ SELECT CASE WHEN $2 = 'km' THEN $1 WHEN $2 = 'mi' THEN $1 / 1.60934 END; $$ LANGUAGE SQL IMMUTABLE RETURNS NULL ON NULL INPUT;")

def downgrade():
    op.execute("DROP FUNCTION convert_km;")
