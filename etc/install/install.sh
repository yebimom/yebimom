# Update Package Manager ( apk ), and upgrade pre-installed pacakges
apt-get update -y
apt-get upgrade -y

# Install Essential Packages
# https://github.com/yyuu/pyenv/wiki/Common-build-problems
apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline6 libreadline6-dev libncurses5-dev libsqlite3-dev wget curl llvm

# Install Additional Packages
apt-get install -y git python python-dev

# Install Project Dependencies
# This is required to exec "pip install -r requirements.txt"
apt-get install -y graphviz libgraphviz-dev pkg-config

# Install Python Version Manager ( pyenv ), Python Virtual Enviroment Manager ( virtualenv )
# https://github.com/yyuu/pyenv-installer
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc

# Install Yebimom Production Environment
pyenv install 2.7.9
pyenv virtualenv 2.7.9 yebimom

# Install Postgresql
# https://help.ubuntu.com/community/PostgreSQL
sudo apt-get install -y postgresql-client
sudo apt-get install -y postgresql postgresql-contrib libpq-dev

# Activate Installed Virtual Environment ( Yebimom )
pyenv shell yebimom
pyenv activate yebimom

# Install Project Dependencies
pip install -r requirements.txt

# Load Environment Variables
source .env.production

# Init Database
sudo -u postgres createdb yebimom
sudo -u postgres psql -c "CREATE USER yebimom;"
sudo -u postgres psql -c "ALTER USER yebimom PASSWORD 'yebimom';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE yebimom to yebimom;"

python manage.py makemigrations users centers events reviews
python manage.py migrate
python manage.py loaddata regions centers facilities
