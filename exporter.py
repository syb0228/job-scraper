import csv

def save_to_file(word, jobs):
    file = open(f"{word}.csv", mode="w", newline='', encoding="utf-8-sig")
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location", "Link"])

    for job in jobs:
        writer.writerow(list(job.values()))
    return