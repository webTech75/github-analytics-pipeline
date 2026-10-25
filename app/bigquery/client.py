from pathlib import Path
from dotenv import load_dotenv
import os
from google.cloud import bigquery
from google.oauth2 import service_account

load_dotenv()
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
BASE_DIR = Path(__file__).resolve().parents[2]

KEY_PATH = BASE_DIR / GOOGLE_APPLICATION_CREDENTIALS


credentials = service_account.Credentials.from_service_account_file(KEY_PATH)

client = bigquery.Client(
    credentials=credentials,
    project=credentials.project_id,
)
