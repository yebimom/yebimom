# Update Package Manager ( apk ), and upgrade pre-installed pacakges
apt-get update -y
apt-get upgrade -y

# Install Essential Packages
# https://github.com/yyuu/pyenv/wiki/Common-build-problems
apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm

# Install Additional Packages
apt-get install -y git python python-dev

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
