import pandas as pd

# Load the authentication dataset
file_path = "data/synthetic_login_activity_dataset.csv"
logs = pd.read_csv(file_path)

print("=== SECURITY LOG ANALYSER ===")
print(f"Total login records: {len(logs)}")

print("\n=== AVAILABLE SECURITY FIELDS ===")
for column in logs.columns:
    print(f"- {column}")
    # Analyse suspicious authentication events
suspicious_events = logs[logs["is_suspicious"] == True]

print("\n=== SUSPICIOUS ACTIVITY ANALYSIS ===")
print(f"Suspicious events detected: {len(suspicious_events)}")

suspicious_percentage = (len(suspicious_events) / len(logs)) * 100
print(f"Percentage of logins flagged as suspicious: {suspicious_percentage:.2f}%")

print("\nSuspicious events by system:")
print(suspicious_events["system_name"].value_counts())
# Identify suspicious events without second-factor authentication
suspicious_no_2fa = suspicious_events[
    suspicious_events["is_second_factor"] == False
]

print("\n=== SUSPICIOUS EVENTS WITHOUT SECOND FACTOR ===")
print(f"Events detected: {len(suspicious_no_2fa)}")

print("\nTop source countries:")
print(
    suspicious_no_2fa["ip_country_anonymized"]
    .value_counts()
    .head(5)
)
# Detect IP addresses generating repeated suspicious activity
ip_activity = (
    suspicious_events["ip_address_anonymized"]
    .value_counts()
)

repeated_suspicious_ips = ip_activity[ip_activity >= 5]

print("\n=== REPEATED SUSPICIOUS IP ACTIVITY ===")
print(f"IPs with 5 or more suspicious events: {len(repeated_suspicious_ips)}")

print("\nTop suspicious IP addresses:")
print(repeated_suspicious_ips.head(10))
# Export repeated suspicious IP activity for further investigation
security_report = repeated_suspicious_ips.reset_index()
security_report.columns = ["ip_address_anonymized", "suspicious_event_count"]

security_report.to_csv(
    "output/suspicious_ip_report.csv",
    index=False
)

print("\n=== REPORT EXPORTED ===")
print("Security report saved to output/suspicious_ip_report.csv")