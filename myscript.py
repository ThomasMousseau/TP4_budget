import os
import subprocess

bad_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("ascii").strip()
good_hash = 'bfdccab909c32635457d41eeb6e7fed322026170'

os.system(f'git bisect start {bad_hash} {good_hash} 2>&1')
os.system('git bisect run python manage.py test 2>&1')
os.system('git bisect reset 2>&1')


