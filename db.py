import os
import urllib.parse
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# If MONGO_URI env var is set (production), use it directly
# The password MUST be URL-encoded in the env var (e.g. @ -> %40)
RAW_MONGO_URI = os.getenv("MONGO_URI")

if RAW_MONGO_URI:
    DATABASE_URL = RAW_MONGO_URI
else:
    # Local fallback: build the URL with URL-encoded credentials
    MONGO_USER = "digambarchalkapure_db_user"
    MONGO_PASS = urllib.parse.quote_plus("Chalkapure@2000")
    DATABASE_URL = (
        f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}"
        f"@developertracker.txx5bky.mongodb.net/"
        f"?retryWrites=true&w=majority&appName=DeveloperTracker"
    )

# Initialize Sync MongoDB Client
client = MongoClient(DATABASE_URL)
db = client.developertracker

def get_db():
    """Dependency to provide the MongoDB database instance."""
    yield db
