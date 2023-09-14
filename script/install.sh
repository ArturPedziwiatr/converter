apt-get update
apt-get install build-essential -y
apt-get install git -y
apt-get install wget -y

wget --quiet https://go.dev/dl/go1.21.1.linux-amd64.tar.gz -O ~/go.tar.gz
tar -C /usr/local -xzf ~/go.tar.gz
rm ~/go.tar.gz

cd /opt/app

git clone https://github.com/mfbonfigli/gocesiumtiler.git

cd gocesiumtiler

go env -w CGO_ENABLED=1
go build

wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh

chmod +x ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
rm ~/miniconda.sh
conda create -n app_env -c conda-forge entwine
# conda run -n app_env /bin/bash -c
# cd ..

# pip install -r ./requirements.txt
