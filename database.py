from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db" local

#engine = create_engine(
#    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
#)

SQLALCHEMY_DATABASE_URL = "postgresql://default:Nj7eJ9uVLHUf@ep-steep-river-a464nbch.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db" local

engine = create_engine(
    SQLALCHEMY_DATABASE_URL #remove connections thing check thread thing
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()