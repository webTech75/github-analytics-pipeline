from sqlalchemy import text

from app.database.connection import engine


def analyze_data():

    with engine.connect() as connection:

        total = connection.execute(text("""
                SELECT SUM(repository_count)
                FROM github_data;
            """)).scalar()

        top_language = connection.execute(text("""
                SELECT language, repository_count
                FROM github_data
                ORDER BY repository_count DESC
                LIMIT 1;
            """)).fetchone()

        average = connection.execute(text("""
                SELECT AVG(repository_count)
                FROM github_data;
            """)).scalar()

    print("Analytics Result")
    print("----------------")
    print(f"Total repositories: {total}")
    print(f"Top language: {top_language[0]} ({top_language[1]})")
    print(f"Average repositories: {average}")


if __name__ == "__main__":
    analyze_data()
