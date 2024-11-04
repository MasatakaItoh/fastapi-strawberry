from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# データベースURL（例: PostgreSQL用のURL）
DATABASE_URL = "postgresql://user:password@db:5432/dbname"

# エンジンの作成
engine = create_engine(DATABASE_URL, echo=True)

# セッションの作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Baseクラスの作成
Base = declarative_base()
