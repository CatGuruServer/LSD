import os  # For working with file paths and directories
import secrets  # For securely generating random API keys
import sys  # For accessing command-line arguments

def generate_api_key():
    """
    Generate a random 32-character API key.

    :return: A securely generated random API key as a hexadecimal string.
    """
    return secrets.token_hex(16)

def save_api_key(app_name, key_dir):
    """
    Generate and save an API key for the given app.

    :param app_name: Name of the app (e.g., radarr, sonarr).
    :param key_dir: Directory where the API key file will be saved.
    :return: The generated API key.
    """
    # Generate a new API key
    api_key = generate_api_key()

    # Construct the full path for the API key file
    key_path = os.path.join(key_dir, f"{app_name}_api.key")

    # Ensure the directory for the API key exists
    os.makedirs(key_dir, exist_ok=True)

    # Write the API key to the file
    with open(key_path, "w") as f:
        f.write(api_key)

    # Print a success message to the console
    print(f"[{app_name}] API key saved to {key_path}")

    # Return the generated API key
    return api_key

if __name__ == "__main__":
    """
    Main entry point of the script. This section handles command-line arguments
    and calls the `save_api_key` function to generate and save the API key.
    """
    # Check if the required arguments are provided
    if len(sys.argv) != 3:
        # Print usage instructions if arguments are missing
        print("Usage: python generate_api_key.py <service_name> <key_dir>")
        sys.exit(1)

    # Get the app name (e.g., radarr, sonarr) from the first argument
    app_name = sys.argv[1]

    # Get the directory where the API key should be saved from the second argument
    key_dir = sys.argv[2]

    # Generate and save the API key
    save_api_key(app_name, key_dir)