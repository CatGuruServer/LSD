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

### Installing Ansible on Your Local Machine

Before deploying the CatguruServer stack, ensure that Ansible is installed on your local machine. Follow these steps to install Ansible:

1. **Update the package list:**

   ```bash
   sudo apt update
   ```

2. **Install required dependencies:**

   ```bash
   sudo apt install software-properties-common
   ```

3. **Add the Ansible PPA repository:**

   ```bash
   sudo add-apt-repository --yes --update ppa:ansible/ansible
   ```

4. **Install Ansible:**

   ```bash
   sudo apt install ansible
   ```

Once Ansible is installed, you can proceed with the deployment steps outlined below.

---

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sirbac/LSD.git
   cd CatguruServer
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
