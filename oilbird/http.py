import requests


def list_jobs(context):
    url = context.baseurl() + '/jobs.json'
    return requests.get(url, auth=context.auth())


def job_status(context, uuid):
    url = context.baseurl()
    url += '/publishers/twitter/historical/track/jobs/{}.json'.format(uuid)
    return requests.get(url, auth=context.auth())


def create_job(context, instructions):
    return requests.post()


def reject_job(context, uuid):
    return requests.put()


def accept_job(context, uuid):
    return requests.put()


def monitor_job(context, uuid):
    return requests.get()


def download_job_result(uuid):
    return requests.get()
