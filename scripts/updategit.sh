cd ~/SpaceCRAFT
sudo rm ~/SpaceCRAFT/spacecraft/*.csv
sudo rm ~/SpaceCRAFT/spacecraft/RTIMULib.ini
sudo rm ~/SpaceCRAFT/scripts/RTIMULib.ini
sudo rm ~/SpaceCRAFT/spacecraft/*.pyc
sudo rm -R ~/SpaceCRAFT/spacecraft/__pycache__
git add -A
git commit -m "$1"
git push origin master
