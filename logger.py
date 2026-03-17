from collections import Counter


class HoneypotLogger:

    def __init__(self):

        self.connections = []
        self.credentials = []
        self.ip_attempts = {}

    def log_connection(self, ip, timestamp):

        self.connections.append({
            "ip": ip,
            "timestamp": timestamp
        })

        if ip not in self.ip_attempts:
            self.ip_attempts[ip] = 0

    def log_credentials(self, ip, username, password):

        self.credentials.append({
            "ip": ip,
            "username": username,
            "password": password
        })

        self.ip_attempts[ip] += 1

    def detect_bruteforce(self, threshold=5):

        attackers = []

        for ip, attempts in self.ip_attempts.items():

            if attempts >= threshold:
                attackers.append((ip, attempts))

        return attackers

    def stats(self):

        ips = [c["ip"] for c in self.connections]
        usernames = [c["username"] for c in self.credentials]
        passwords = [c["password"] for c in self.credentials]

        return {
            "total_connections": len(self.connections),
            "unique_ips": len(set(ips)),
            "top_username": Counter(usernames).most_common(1),
            "top_password": Counter(passwords).most_common(1)
        }