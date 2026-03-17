def generate_report(logger):

    stats = logger.stats()
    bruteforce = logger.detect_bruteforce()

    report = []
    report.append("===== HONEYPOT ATTACK REPORT =====\n")

    report.append(f"Total connections: {stats['total_connections']}")
    report.append(f"Unique IPs: {stats['unique_ips']}")

    if stats["top_username"]:
        report.append(f"Top username tried: {stats['top_username'][0][0]}")

    if stats["top_password"]:
        report.append(f"Top password tried: {stats['top_password'][0][0]}")

    report.append("\nPossible brute-force attackers:")

    if bruteforce:
        for ip, attempts in bruteforce:
            report.append(f"{ip} -> {attempts} attempts")
    else:
        report.append("None detected")

    report_text = "\n".join(report)

    print(report_text)

    with open("honeypot_report.txt", "w") as f:
        f.write(report_text)

    print("\nReport saved to honeypot_report.txt")