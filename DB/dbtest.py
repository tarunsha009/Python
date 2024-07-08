from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import psycopg2

# Replace with your actual PostgreSQL credentials
DB_DIALECT = 'postgresql'
DB_HOST = 'localhost'
DB_PORT = 5432
DB_USER = 'postgres'
DB_PASSWORD = 'a'
DB_NAME = 'crickbuzz'

db_connection_uri = f"{DB_DIALECT}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# Create the engine
# engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{hostname}/{database_name}')
engine = create_engine(db_connection_uri)
# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Reflect the existing tables
Base = automap_base()
# Base.prepare(engine, reflect=True)
Base.prepare(autoload_with=engine)

# Access the 'users' table (change 'users' to the name of your table)
User = Base.classes.player

# Query the database
users = session.query(User).all()
for user in users:
    print(user.player_id, user.player_name, user.player_country, user.player_age, user.player_role)

# # Update a user
# user_to_update = session.query(User).filter_by(name='Alice').first()
# if user_to_update:
#     user_to_update.age = 26
#     session.commit()
#
# # Delete a user
# user_to_delete = session.query(User).filter_by(name='Alice').first()
# if user_to_delete:
#     session.delete(user_to_delete)
#     session.commit()
