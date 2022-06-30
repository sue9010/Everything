import csv


def save_to_file(jobs):
    file = open("jobs.csv", mode="w", encoding="utf-8", newline='')
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        try:
            writer.writerow(list(job.values()))
        except AttributeError as e:
            pass
    file.close()
    return