import csv
import subprocess

with open('github-user-name.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        branch_name = row[1]
        print(branch_name)
        subprocess.run(['git', 'branch', branch_name])
        subprocess.run(['git', 'push', 'origin', branch_name])

