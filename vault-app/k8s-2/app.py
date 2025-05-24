# app.py

import os

def load_secrets_from_file(file_path="/vault/secrets/my-first-secret"):
    """
    Reads key=value pairs from a single file and sets them as environment variables.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Secret file {file_path} does not exist.")

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if "=" in line:
                key, value = line.split("=", 1)
                os.environ[key.strip().upper()] = value.strip()
                print(f"Loaded secret {key.strip().upper()}")

if __name__ == "__main__":
    load_secrets_from_file()

    # Use the secrets
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    print("\n🔐 Secrets from Vault:")
    print(f"Username: {username}")
    print(f"Password: {password}")

