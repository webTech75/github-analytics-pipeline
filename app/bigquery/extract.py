from app.bigquery.client import client


def get_top_languages(limit=10):

    query = f"""
    SELECT
        lang.name AS language,
        COUNT(*) AS repository_count
    FROM
        `bigquery-public-data.github_repos.languages`,
        UNNEST(language) AS lang
    GROUP BY
        language
    ORDER BY
        repository_count DESC
    LIMIT {limit}
    """

    result = client.query(query)

    return result
