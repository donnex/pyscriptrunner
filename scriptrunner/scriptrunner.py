import sys
import time


class ScriptRunner(object):
    """Run script in inifinte loop or execute once if cron is passed as arg"""
    def __init__(self, c, argv, sleep=60, *args, **kwargs):
        self.c = c
        self.argv = argv
        self.sleep = sleep
        self.args = args
        self.kwargs = kwargs

        if kwargs.get('single_instance'):
            from tendo import singleton
            me = singleton.SingleInstance()
            del(kwargs['single_instance'])

        self.runner()

    def runner(self):
        cron = False
        for arg in self.argv:
            if arg == 'cron':
                cron = True

        try:
            if cron:
                self.c(*self.args, **self.kwargs)
            else:
                while 1:
                    self.c(*self.args, **self.kwargs)
                    time.sleep(self.sleep)
        except KeyboardInterrupt:
            print >> sys.stderr, '\nExiting by user request.\n'
            sys.exit(0)
