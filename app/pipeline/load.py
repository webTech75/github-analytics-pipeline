from sqlalchemy.orm import Session

from app.bigquery.extract import get_top_languages
from app.database.connection import engine
from app.database.models import GithubData


def load_languages():

    rows = get_top_languages()

    with Session(engine) as session:

        # Remove previous snapshot
        session.query(GithubData).delete()

        for row in rows:
            data = GithubData(
                language=row.language, repository_count=row.repository_count
            )

            session.add(data)

        session.commit()

    print("Data loaded successfully")


if __name__ == "__main__":
    load_languages()
