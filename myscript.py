import os
import subprocess
import sys

bad_hash = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("ascii").strip()
good_hash = 'bfdccab909c32635457d41eeb6e7fed322026170'

sys.stdout.flush()
os.system(f'git bisect start {bad_hash} {good_hash}')
os.system('git bisect run python manage.py test')
os.system('git bisect reset')

print('This is the final commit that broke the code:' + str(bad_hash))

