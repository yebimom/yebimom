# Update Package Manager ( apk ), and upgrade pre-installed pacakges
apt-get update -y
apt-get upgrade -y

# Install Essential Packages
apt-get install -y build-essential git python python-dev

# Install Python Version Manager ( pyenv ), Python Virtual Enviroment Manager ( virtualenv )
# https://github.com/yyuu/pyenv-installer
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc
