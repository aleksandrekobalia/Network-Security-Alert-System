import scapy.all as scapy
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Simple patterns for detecting SQL Injection and brute force attempts
SQLI_PATTERNS = [r"select.*from", r"union.*select", r"drop.*table", r"or.*1=1"]
BRUTE_FORCE_PATTERNS = r"Failed login"

# Email alert function
def send_alert(subject, body):
    sender_email = "your_email@example.com"  # Replace with your email
    receiver_email = "receiver_email@example.com"  # Replace with the recipient's email
    password = "your_email_password"  # Replace with your email password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)  # Login to your email account
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)  # Send the email
        server.quit()
        print(f"Alert sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send alert: {e}")

# Packet sniffing callback function
def packet_callback(packet):
    # Check for SQLi patterns in HTTP requests
    if packet.haslayer(scapy.IP) and packet.haslayer(scapy.TCP):
        payload = str(packet.payload)  # Extract payload of the packet
        for pattern in SQLI_PATTERNS:
            if re.search(pattern, payload, re.IGNORECASE):  # Check if the pattern matches the payload
                print("SQL Injection attempt detected!")
                send_alert("SQL Injection Attempt", f"Potential SQL Injection detected in packet:\n{payload}")
                break  # If one pattern is matched, stop further checks for this packet

        # Check for brute force attempts in HTTP request payloads
        if BRUTE_FORCE_PATTERNS in payload:
            print("Brute force attempt detected!")
            send_alert("Brute Force Attempt", f"Potential brute force attempt detected:\n{payload}")

# Start sniffing network traffic
def start_sniffing():
    print("Starting to sniff network traffic for security threats...")
    scapy.sniff(prn=packet_callback, store=0)  # Captures packets and calls packet_callback for each packet

if __name__ == "__main__":  # Corrected this line
    start_sniffing()  # Call the sniffing function to start monitoring network traffic
