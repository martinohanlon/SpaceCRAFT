cd ~/SpaceCRAFT
sudo rm ~/SpaceCRAFT/spacecraft/*.csv
sudo rm ~/SpaceCRAFT/spacecraft/RTIMULib.ini
sudo rm ~/SpaceCRAFT/scripts/RTIMULib.ini
sudo rm ~/SpaceCRAFT/spacecraft/*.pyc
sudo rm -R ~/SpaceCRAFT/spacecraft/__pycache__
sudo rm -R ~/SpaceCRAFT/build
sudo rm -R ~/SpaceCRAFT/dist
sudo rm -R ~/SpaceCRAFT/spacecraft.egg-info

git add -A
git commit -m "$1"
git push origin master
