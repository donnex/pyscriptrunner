Python script runner wrapper. I'm using it to wrap my scripts for running once from cron or in an infinite loop.

**Usage**

    if __name__ == '__main__':
        ScriptRunner(MyClass, sys.argv)

*python myscript.py* will run the script in an infinite loop. Change sleep time with *sleep=seconds*, defaults to 60.

    ScriptRunner(MyClass, sys.argv, sleep=10)

Use *python myscript.py cron* to execute the script once, eg. when you run it from cron.

If you install [tendo](http://pypi.python.org/pypi/tendo) you can pass *single_instance=True* to make sure that only one instance of the script is allowed to run at the same time.

    ScriptRunner(MyClass, sys.argv, single_instance=True)
