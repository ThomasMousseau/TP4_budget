import os

bad_hash = 'e28079a5586d70c76304d4290db36f90fc41cfde'
good_hash = 'bfdccab909c32635457d41eeb6e7fed322026170'

os.system(f'git bisect start {bad_hash} {good_hash}')
os.system('git bisect run python manage.py test')
os.system('git bisect reset')

