# A continuation of how data can be manipulated.
# This checks the validity of an email, checks whether it's properly configured, if it has SPF, and DKIM records.
# Exports emails to new CSV and includes their validation results.

import re
import dns.resolver
import csv


# validates email format.
def validate_email(email):
    results = {
        "Email Format": "Invalid",
        "MX Records": "Invalid",
        "SPF Records": "Invalid",
        "DKIM Records": "Invalid",
    }

    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        results["Email Format"] = "Valid"

    username, domain = email.split("@")

    try:
        # MX record lookup
        mx_records = dns.resolver.query(domain, "MX")
        if mx_records:
            results["MX Records"] = "Valid"

        # SPF record lookup
        spf_records = dns.resolver.query(domain, "TXT")
        for record in spf_records:
            if "v=spf1" in record.to_text():
                results["SPF Records"] = "Valid"
                break

        # very simple DKIM check.
        for record in spf_records:
            if "v=DKIM1" in record.to_text():
                results["DKIM Records"] = "Valid"
                break

    except dns.resolver.NXDOMAIN:
        pass
    except Exception as e:
        print(f"Error: {str(e)} for {email}")

    return results


targets = "targets.csv"
checked_targets = "checked_targets.csv"

with open(targets, "r") as csv_input, open(
    checked_targets, "w", newline=""
) as csv_output:
    reader = csv.reader(csv_input)
    writer = csv.writer(csv_output)

    next(reader, None)

    writer.writerow(
        ["Email", "Email Format", "MX Records", "SPF Records", "DKIM Records"]
    )

    for row in reader:
        email = row[1]
        results = validate_email(email)
        writer.writerow(
            [
                email,
                results["Email Format"],
                results["MX Records"],
                results["SPF Records"],
                results["DKIM Records"],
            ]
        )

print(f"Validation results saved to {checked_targets}")
