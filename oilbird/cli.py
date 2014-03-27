from clint.textui import puts, indent
from clint.textui.colored import yellow
from clint import arguments
from . import config
from . import http
from . import version
import sys


def uuid(args):
    uuid = args.get(1)
    if uuid is None:
        print(yellow('must supply a job id'))
        sys.exit(1)
    return uuid


def main():
    try:
        input = raw_input
    except NameError:
        pass

    args = arguments.Args()
    puts('oilbird version {}'.format(version))
    puts('no operations supported yet.')

    command = args.get(0)
    if command == 'init':
        if config.config_exists():
            puts(yellow('Config found!'))
            answer = input('Overwrite? ')
            if answer not in ('y', 'yes'):
                puts('exiting...')
                sys.exit()

            account = input('enter account name: ')
            username = input('enter username: ')
            password = input('enter password: ')

            # context = {
            #     'account': account,
            #     'username': username,
            #     'password': password,
            # }
    else:
        pass

    # context = config.Config()

    if command == 'list':
        c = config.Config('FalconSocial', 'dennis@falconsocial.com', 'falconium10')

        cache = args.get(1)

        if not cache:
            puts('getting jobs from gnip...')
            resp = http.list_jobs(c)
            puts(str(resp))
            # Update the local cache with new results.
            # And purge those that expired.

        puts('jobs in cache is:')
        with indent(4):
            for job in []:
                puts(job)

    elif command == 'create':
        for job in args.files:
            print(job)

    elif command in ('status', 'monitor'):
        job_id = uuid(args)

    elif command == 'accept':
        job_id = uuid(args)

    elif command == 'reject':
        job_id = uuid(args)
    elif command == 'download':
        job_id = uuid(args)
