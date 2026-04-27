import os
from google.cloud import storage

# Make sure vertex-key.json exists
key_path = os.path.join("..", "backend", "vertex-key.json")
if os.path.exists(key_path):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path
    client = storage.Client()
    # List buckets
    print([b.name for b in client.list_buckets()])
else:
    print("vertex-key.json not found")
