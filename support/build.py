"""
Builds the version of FitVids.js that's in vendor/fitvids.js and packages
it as a Django app for use with Django staticfiles.
"""
import subprocess
import sys


def cp(src):
    cmd = [
        "cp -R vendor/FitVids.js/%s fitvidsjs/static/fitvidsjs/" % src,
    ]
    subprocess.call(cmd, shell=True)


def main():
    subprocess.call(["mkdir -p ./fitvidsjs/static/fitvidsjs"], shell=True)
    cp("jquery.fitvids.js")


if __name__ == "__main__":
    main()
