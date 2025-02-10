# WSL2 Installation Guide for Ubuntu & Debian on Windows

## Prerequisites
- Windows 10 (version 2004 and later) or Windows 11.
- Administrative privileges.
- An active internet connection.

---

## Step 1: Enable WSL and Virtual Machine Platform

### Method 1: Using PowerShell (Recommended)
1. Open **PowerShell as Administrator**.
2. Run the following command to install WSL and set WSL2 as the default version:
   ```powershell
   wsl --install
   ```
   This installs:
   - WSL
   - WSL2
   - The latest Ubuntu distribution

3. **Reboot your system** when prompted.

### Method 2: Manual Installation
If `wsl --install` is unavailable, follow these steps:

1. **Enable WSL**
   ```powershell
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
   ```

2. **Enable Virtual Machine Platform**
   ```powershell
   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   ```

3. **Restart your computer.**

4. **Set WSL2 as Default**
   ```powershell
   wsl --set-default-version 2
   ```

---

## Step 2: Install Ubuntu and Debian

### Method 1: Using Microsoft Store (Easiest)
1. Open the **Microsoft Store**.
2. Search for **Ubuntu** and **Debian**.
3. Click **Get** or **Install** for each distribution.
4. Wait for the installations to complete.

### Method 2: Using PowerShell
Alternatively, install them via PowerShell:
```powershell
wsl --install -d Ubuntu
wsl --install -d Debian
```
This will download and set up both distributions automatically.

---

## Step 3: Launch and Set Up Ubuntu & Debian
1. Open **Ubuntu** or **Debian** from the **Start Menu** or run:
   ```powershell
   wsl -d Ubuntu
   wsl -d Debian
   ```
2. The first time you launch a distribution, it will ask you to **create a user**:
   - Enter a **new username**.
   - Enter a **new password**.
   - Confirm the password.

3. Verify that WSL is running version 2:
   ```powershell
   wsl --list --verbose
   ```
   Output should indicate `VERSION 2` for Ubuntu and Debian.

4. If either distro is set to version 1, upgrade it:
   ```powershell
   wsl --set-version Ubuntu 2
   wsl --set-version Debian 2
   ```

---

## Step 4: Updating and Configuring Ubuntu & Debian
Once inside the WSL terminal, update the system:

### Ubuntu
```bash
sudo apt update && sudo apt upgrade -y
```

### Debian
```bash
sudo apt update && sudo apt full-upgrade -y
```

---

## Step 5: Set Default Linux Distribution (Optional)
If you want Ubuntu or Debian to launch by default when running `wsl`, set it as default:
```powershell
wsl --set-default Ubuntu
```
or
```powershell
wsl --set-default Debian
```

---

## Step 6: Configure WSL Settings (Optional)
You can customize WSL behavior by creating a **`.wslconfig`** file in your Windows user directory.

```powershell
notepad $env:USERPROFILE\.wslconfig
```

Example **`.wslconfig`**:
```ini
[wsl2]
memory=8GB  # Limit WSL2 to 8GB RAM
processors=4  # Limit to 4 CPU cores
swap=2GB  # Set swap size to 2GB
localhostForwarding=true  # Enable localhost forwarding
```

After saving, restart WSL:
```powershell
wsl --shutdown
```

---

## Step 7: Using WSL2
- Open **WSL** from PowerShell or Command Prompt:
  ```powershell
  wsl
  ```
- Open a specific distro:
  ```powershell
  wsl -d Ubuntu
  ```
  or
  ```powershell
  wsl -d Debian
  ```
- Shutdown WSL manually:
  ```powershell
  wsl --shutdown
  ```
- List installed distros:
  ```powershell
  wsl --list --verbose
  ```

---

## Troubleshooting

### Check WSL Version
```powershell
wsl --version
```
Ensure you have **WSL 2** installed.

### Manually Install WSL Kernel
If WSL fails to start, install the WSL2 kernel manually:
1. Download from [Microsoft WSL2 Kernel Update](https://aka.ms/wsl2kernel).
2. Run the installer and restart your computer.

### Fix `wsl.exe not found`
Ensure WSL is enabled in Windows Features:
```powershell
optionalfeatures
```
Check **Windows Subsystem for Linux** and **Virtual Machine Platform**, then reboot.

---

## Conclusion
You've successfully installed **WSL2**, **Ubuntu**, and **Debian** on Windows! 🎉 You can now use a full Linux environment alongside Windows.