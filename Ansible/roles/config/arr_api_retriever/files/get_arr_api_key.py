#!/usr/bin/env python3
import os  # For working with environment variables and file paths
import requests  # For making HTTP requests to the *arr services

# List of *arr apps with their default ports
# These are the services we want to retrieve API keys from, along with their default ports
ARR_APPS = {
    "radarr": 7878,  # Radarr runs on port 7878 by default
    "sonarr": 8989,  # Sonarr runs on port 8989 by default
    "lidarr": 8686,  # Lidarr runs on port 8686 by default
    "readarr": 8787,  # Readarr runs on port 8787 by default
}

# Directory where the API keys will be saved
CENTRAL_KEY_DIR = "/opt/central-api-keys"

# Function to retrieve the API key for a specific *arr app
def get_api_key(app_name, app_url, key_output_path):
    """
    Fetches the API key for a given *arr app and saves it to a file.

    :param app_name: Name of the app (e.g., radarr, sonarr)
    :param app_url: URL of the app (e.g., http://localhost:7878)
    :param key_output_path: Path to save the API key file
    """
    try:
        # Make a GET request to the app's system status endpoint
        response = requests.get(f"{app_url}/api/v3/system/status", timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract the API key from the response
            api_key = data.get("apiKey", "NOT_FOUND")
            
            # If the API key is found, save it to the specified file
            if api_key != "NOT_FOUND":
                # Ensure the directory for the file exists
                os.makedirs(os.path.dirname(key_output_path), exist_ok=True)
                # Write the API key to the file
                with open(key_output_path, "w") as f:
                    f.write(api_key)
                print(f"[{app_name}] API key saved to {key_output_path}")
            else:
                # If the API key is not found in the response
                print(f"[{app_name}] API key not found in response.")
        else:
            # If the server returns an error status code
            print(f"[{app_name}] Failed to fetch API key: {response.status_code}")
    except requests.exceptions.ConnectionError:
        # Handle the case where the app is unreachable
        print(f"[{app_name}] Service is unreachable at {app_url}. Skipping...")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"[{app_name}] Error retrieving API key: {e}")

# Main function to process all *arr apps
def main():
    """
    Iterates through all *arr apps, retrieves their API keys, and saves them to files.
    """
    for app_name, default_port in ARR_APPS.items():
        # Get the app's URL from environment variables or use the default localhost URL
        app_url = os.environ.get(f"{app_name.upper()}_URL", f"http://localhost:{default_port}")
        # Get the output path for the API key file from environment variables or use the default path
        key_output_path = os.environ.get(
            f"{app_name.upper()}_KEY_OUTPUT_PATH", f"{CENTRAL_KEY_DIR}/{app_name}_api.key"
        )
        # Log the app being processed
        print(f"Processing {app_name} at {app_url}...")
        # Call the function to retrieve and save the API key
        get_api_key(app_name, app_url, key_output_path)

# Entry point of the script
if __name__ == "__main__":
    # Run the main function
    main()
