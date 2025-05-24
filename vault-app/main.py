import hvac
import os

def get_db_credentials():
    client = hvac.Client(
        url=os.environ['VAULT_ADDR'],
        token=os.environ['VAULT_TOKEN']
    )

    if not client.is_authenticated():
        raise Exception("Vault authentication failed.")

    # Only pass the secret's path — do NOT include /v1/ or /data/
    secret = client.secrets.kv.v2.read_secret_version(
        path='db',
        mount_point='test'
    )

    data = secret['data']['data']
    return data['username'], data['password']

def main():
    try:
        username, password = get_db_credentials()
        print(f"Username: {username}, Password: {password}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()

