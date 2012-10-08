Python script runner wrapper. I'm using it to wrap my scripts for running once from cron or in an infinite loop.

myscript.py

    if __name__ == '__main__':
        ScriptRunner(MyClass, sys.argv)
        
Now the script will run in an inifinite loop if you run it without any arguments and once if you pass cron to argv.