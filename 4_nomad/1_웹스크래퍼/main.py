from save import save_to_file
from indeed import get_jobs as get_indeed_jobs
from jobkorea import get_jobs as get_jobkorea_jobs

indeed_jobs = get_indeed_jobs()
jobkoreajobs = get_jobkorea_jobs()
jobs = indeed_jobs + jobkoreajobs
save_to_file(jobs)

