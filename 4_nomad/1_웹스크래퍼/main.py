from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_stackoverflow_jobs

indeed_jobs = get_indeed_jobs()
stackoverflowjobs = get_stackoverflow_jobs()

# print(stackoverflowjobs)
print(indeed_jobs)
