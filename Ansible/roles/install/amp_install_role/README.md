# AMP Install Role

This Ansible role installs CubeCoders AMP using the official install script, automating all interactive prompts using the `expect` module. It also ensures the AMP service is restarted after installation.

## Variables

- `amp_username`: AMP admin username
- `amp_password`: AMP admin password (use Ansible Vault for production)
- `amp_use_docker`: Whether to install AMP in Docker
- `amp_use_https`: Whether to set up HTTPS with Let's Encrypt
- `amp_domain`: Domain name (if using HTTPS)
- `amp_email`: Email for Let's Encrypt (if using HTTPS)
- `amp_minecraft`: Whether to install Java for Minecraft servers
- `amp_steamcmd`: Whether to install 32-bit libs for SteamCMD apps

## Usage

```yaml
- hosts: servers
  become: true
  roles:
    - amp_install_role
```
