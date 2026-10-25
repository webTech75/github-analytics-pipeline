from sqlalchemy import Column, Integer, String

from app.database.connection import Base


class GithubData(Base):
    __tablename__ = "github_data"

    id = Column(Integer, primary_key=True)
    language = Column(String, nullable=False)
    repository_count = Column(Integer, nullable=False)
