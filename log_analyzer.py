logs = [
    "Login successful",
    "Login failed",
    "Login failed",
    "Login successful",
    "Login failed"
]

failed_attempts = 0

for log in logs:
    if log == "Login failed":
        failed_attempts += 1

print("Security Log Analysis")
print("Total logs:", len(logs))
print("Failed login attempts:", failed_attempts)

if failed_attempts >= 3:
    print("Alert: Multiple failed login attempts detected!")
