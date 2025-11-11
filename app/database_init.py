from app.database import engine
from app.models.user import Base

# Creates all tables defined by models
def init_db():
    Base.metadata.create_all(bind=engine)

# Deletes all tables
def drop_db():
    Base.metadata.drop_all(bind=engine)

if __name__ == "__main__":
    init_db() # pragma: no cover