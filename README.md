# Network Security Alert System

## Overview
The **Network Security Alert System** is a Python-based tool that monitors network traffic in real-time, looking for suspicious activity such as **SQL Injection**, **Brute Force attempts**, and more. When an attack pattern is detected, it sends an email alert to the configured address.

This project was created by **Aleksandre** to help network administrators and security professionals identify potential threats within network traffic and take appropriate actions.

## Features
- **Real-time Network Traffic Sniffing** using Scapy
- **SQL Injection (SQLi)** Pattern Detection
- **Brute Force** Attempt Detection
- **Email Alerts** for Detected Suspicious Activity

## Prerequisites
- Python 3.x
- **scapy** library

## Setup

### Install Dependencies
1. Clone the repository:
    ```bash
    git clone https://github.com/aleksandrekobalia/Network-Security-Alert-System.git
    cd Network-Security-Alert-System
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Email Configuration
Before running the script, ensure that you modify the `main.py` file with your email credentials. Replace the placeholders in the `send_alert` function:

```python
sender_email = "your_email@example.com"  # Replace with your email
receiver_email = "receiver_email@example.com"  # Replace with the recipient's email
password = "your_email_password"  # Replace with your email password
