# ⚠️ Broken: amp-install Branch

This branch (`amp-install`) is currently under development and may not function as expected. Use at your own risk.

---

# LazyServerDeploy

**"We are lazy"** — a self-hosted, containerized media server stack using **Ansible** to set up Docker and manage deployment with Docker Compose.

## 🧰 Included Services

### Services with a UI
| Service               | Description                                               | Port(s) |
|-----------------------|-----------------------------------------------------------|---------|
| [**Radarr**](https://radarr.video/)            | Movie management and automation                           | `7878`  |
| [**Sonarr**](https://sonarr.tv/)              | TV show management and automation                         | `8989`  |
| [**qBittorrentVPN**](https://github.com/qbittorrent/qBittorrent) | Torrent client with VPN support                           | `1239`, `8999` |
| [**Audiobookshelf**](https://www.audiobookshelf.org/)    | Organize and stream audiobooks                            | `13378` |
| [**Prowlarr**](https://prowlarr.com/)          | Indexer manager for Sonarr, Radarr, etc.                  | `9696`  |
| [**Jellyfin**](https://jellyfin.org/)          | Media server for streaming video, music, and more         | `8096`  |
| [**Jellyseerr**](https://github.com/Fallenbagel/jellyseerr)        | Request manager for Jellyfin                              | `5055`  |
| [**Organizr**](https://organizr.app/)          | Homepage/dashboard to manage all your services            | `90`    |
| [**Portainer**](https://www.portainer.io/)         | Docker container management                               | `9000`  |
| [**Bazarr**](https://www.bazarr.media/)            | Subtitle management for Radarr and Sonarr                 | `6767`  |
| [**Speedtest Tracker**](https://github.com/henrywhitaker3/Speedtest-Tracker) | Internet speed monitoring and tracking                    | `8765`  |
| [**Cockpit**](https://cockpit-project.org/)           | Web-based server management                               | `9090`  |
| [**Readarr**](https://readarr.com/)           | Book management and automation                            | `8787`  |
| [**Lidarr**](https://lidarr.audio/)            | Music management and automation                           | `8686`  |

### Services without a UI
| Service               | Description                                               |
|-----------------------|-----------------------------------------------------------|
| [**Node Exporter**](https://prometheus.io/docs/guides/node-exporter/)     | Exposes system metrics for Prometheus                     |
| [**Prometheus**](https://prometheus.io/)        | Monitoring and alerting system                            |
| [**Recyclarr**](https://github.com/recyclarr/recyclarr)         | Synchronizes Radarr/Sonarr settings with custom templates |
| [**Declutarr**](https://github.com/Declutarr/Declutarr)         | Media library cleanup tool                                |
| [**Recommendarr**](https://github.com/l3uddz/Recommendarr)      | Media recommendation engine                               |

These services are deployed using **Docker Compose**, with **Ansible automating the initial Docker setup**.

---

## 🚀 Getting Started

### Prerequisites

- A fresh Linux-based server (Debian/Ubuntu recommended)
- SSH access to the server
- [Ansible](https://docs.ansible.com/) installed on your local machine

---

### New Configuration and Variables

#### Global Variables
The following global variables are used across roles:

- **`keygen_location`**: Directory where the API key generation script is stored (default: `/opt/api_gen`).
- **`key_dir`**: Directory where API keys are stored (default: `/opt/apikeys`).
- **`default_owner`**: Default owner for files and directories (e.g., `catguru`).
- **`default_group`**: Default group for files and directories (e.g., `catguru`).

#### Role-Specific Variables
Each role (e.g., `radarr_deploy`, `sonarr_deploy`) uses the following variables:

- **`radarr_owner`** / **`sonarr_owner`**: Owner for Radarr/Sonarr-related files and directories (inherits from `default_owner`).
- **`radarr_group`** / **`sonarr_group`**: Group for Radarr/Sonarr-related files and directories (inherits from `default_group`).
- **`radarr_compose_dir`** / **`sonarr_compose_dir`**: Directory for Docker Compose files.
- **`radarr_config_dir`** / **`sonarr_config_dir`**: Directory for configuration files.
- **`radarr_api_key`** / **`sonarr_api_key`**: API key for Radarr/Sonarr, dynamically generated and stored in `{{ key_dir }}`.

---

### API Key Management

API keys for services like Radarr and Sonarr are automatically generated and stored securely. The process is as follows:

1. **API Key Generation Script**:
   - The script `generate_api_key.py` is copied to the server (if not already present) and executed to generate a 32-character API key.

2. **Storage**:
   - API keys are stored in the directory specified by `key_dir` (default: `/opt/apikeys`).

3. **Usage**:
   - The API keys are injected into the Docker Compose templates using Ansible's `lookup('file', ...)` function.

---

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sirbac/LSD.git
   cd LSD
   ```

2. **Configure Inventory**

   Use the following boilerplate `inventory.yaml` as a starting point and update it with your server's details. You can choose to authenticate using either an SSH key or a password.

   **Option 1: Using an SSH Key**

   ```yaml
   all:
     hosts:
       your_server_name:
         ansible_host: <your-server-ip>
         ansible_user: <your-ssh-user>
         ansible_ssh_private_key_file: <path-to-your-private-key>
         ansible_become: true
         ansible_become_method: sudo
   ```

   Replace `<your-server-ip>`, `<your-ssh-user>`, and `<path-to-your-private-key>` with your server's actual IP address, SSH username, and the path to your private SSH key (e.g., `~/.ssh/id_rsa`).

   **Option 2: Using a Password**

   ```yaml
   all:
     hosts:
       your_server_name:
         ansible_host: <your-server-ip>
         ansible_user: <your-ssh-user>
         ansible_password: <your-ssh-password>
         ansible_become: true
         ansible_become_method: sudo
   ```

   Replace `<your-server-ip>`, `<your-ssh-user>`, and `<your-ssh-password>` with your server's actual IP address, SSH username, and password.

3. **Run the Ansible Playbook**

   This will:
   - Install Docker and Docker Compose on your server
   - Deploy the media stack
   - Start all services using Docker Compose

   Run the following command:

   ```bash
   ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i inventory.yaml playbook.yaml --ask-vault-pass
   ```

4. **Access the Dashboard**

   Once complete, navigate to the following URLs to access your services:

   - **Organizr**: `http://<your-server-ip>:90`
   - **Jellyfin**: `http://<your-server-ip>:8096`
   - **Radarr**: `http://<your-server-ip>:7878`
   - **Sonarr**: `http://<your-server-ip>:8989`
   - **Bazarr**: `http://<your-server-ip>:6767`
   - **Speedtest Tracker**: `http://<your-server-ip>:8765`
   - **Cockpit**: `http://<your-server-ip>:9090`
   - **Readarr**: `http://<your-server-ip>:8787`
   - **Lidarr**: `http://<your-server-ip>:8686`

---

## ⚙️ Configuration

- **Persistent Storage**: Update volume paths in `docker-compose.yml` or the respective Ansible templates to persist your data.
- **VPN Setup**: Configure VPN credentials for `qBittorrentVPN` in its environment section.
- **Custom Domains**: Integrate with a reverse proxy to use your own domain/subdomains.
- **ARR Apps Configuration**: Use the `config` roles to automate the setup of Sonarr, Radarr, and Bazarr (e.g., adding indexers, download clients, etc.).

---

## 🛠️ Manual Docker Compose Usage

If you already have Docker installed, you can skip the Ansible step and just run:

```bash
docker-compose up -d
```

---

## 🧪 Development

Contributions are welcome! Fork the repo, make changes, and submit a pull request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE.md).
