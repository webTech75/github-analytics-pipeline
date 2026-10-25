from app.database.connection import test_connection
from app.pipeline.load import load_languages
from app.analytics.analysis import analyze_data


def main():

    print("Starting Analytics Pipeline")
    print("==========================")

    test_connection()

    load_languages()

    analyze_data()


if __name__ == "__main__":
    main()
