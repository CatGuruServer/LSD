# API Keys Storage

This directory is used to store API keys for various services.

## Location
API keys are stored in the following directory on the target machine:
`{{ key_dir }}`

## Purpose
Each service (e.g., Radarr, Sonarr) generates or uses an API key for secure communication. These keys are stored here for easy access and management.

## Notes
- Ensure this directory is secure and only accessible by authorized users.
- Do not share or expose the API keys publicly.
- Keys are automatically generated and managed by the Ansible playbook.