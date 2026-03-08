import os
from pymongo import MongoClient
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

# Build the connection string
MONGO_USER = "digambarchalkapure_db_user"
MONGO_PASS = urllib.parse.quote_plus("Chalkapure@2000") # Important: URL encode special characters 
DEFAULT_DB_URL = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@developertracker.txx5bky.mongodb.net/?retryWrites=true&w=majority&appName=DeveloperTracker"

DATABASE_URL = os.getenv("MONGO_URI", DEFAULT_DB_URL)

# Initialize Sync MongoDB Client
client = MongoClient(DATABASE_URL)
# The database to use
db = client.developertracker

def get_db():
    """Dependency to provide the MongoDB database instance."""
    yield db
