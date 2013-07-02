###################################################
#
# Game then install env and python packages install
#
###################################################


# Env directory create
virtualenv --no-site-packages env

# activate env
source env/bin/activate

# requirements packages install
pip install -r requirements.txt
