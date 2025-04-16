import os
import secrets
import sys

def generate_api_key():
    """Generate a random 32-character API key."""
    return secrets.token_hex(16)

def save_api_key(app_name, key_dir):
    """
    Generate and save an API key for the given app.

    :param app_name: Name of the app (e.g., radarr, sonarr)
    :param key_dir: Directory where the API key file will be saved
    """
    api_key = generate_api_key()
    key_path = os.path.join(key_dir, f"{app_name}_api.key")
    os.makedirs(key_dir, exist_ok=True)
    with open(key_path, "w") as f:
        f.write(api_key)
    print(f"[{app_name}] API key saved to {key_path}")
    return api_key

if __name__ == "__main__":
    # Check if the required arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python generate_api_key.py <service_name> <key_dir>")
        sys.exit(1)

    # Get the app name and key directory from the command-line arguments
    app_name = sys.argv[1]
    key_dir = sys.argv[2]

    # Generate and save the API key
    save_api_key(app_name, key_dir)