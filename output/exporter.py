import csv

def export_to_csv(data, filename="phishfeed_output.csv"):
    if not data:
        return
    keys = data[0].keys()
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)