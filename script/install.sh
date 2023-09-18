pacman -Syu --noconfirm
pacman -S gcc --noconfirm
pacman -S git --noconfirm
pacman -S wget --noconfirm

pacman -S go --noconfirm

pacman -S pdal --noconfirm

pacman -S python --noconfirm
pacman -S python-pip --noconfirm
pacman -S python-virtualenv --noconfirm
pip --version
python -m venv ~/venv
source ~/venv/bin/activate
pip install -r /opt/app/requirements.txt


cd /opt/app

git clone https://github.com/mfbonfigli/gocesiumtiler.git

cd gocesiumtiler

go env -w CGO_ENABLED=1
go build
