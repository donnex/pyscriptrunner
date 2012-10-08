import sys
import time


class ScriptRunner(object):
    """Run script in inifinte loop or execute once if cron is passed as arg"""
    def __init__(self, c, argv, sleep=60, *args, **kwargs):
        cron = False
        for arg in argv:
            if arg == 'cron':
                cron = True

        try:
            if cron:
                c(*args, **kwargs)
            else:
                while 1:
                    c(*args, **kwargs)
                    time.sleep(sleep)
        except KeyboardInterrupt:
            print >> sys.stderr, '\nExiting by user request.\n'
            sys.exit(0)
