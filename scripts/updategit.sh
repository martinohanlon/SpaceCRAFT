cd ~/SpaceCRAFT
sudo rm ~/SpaceCRAFT/poc/*.pyc
sudo rm ~/SpaceCRAFT/minecraft/*.pyc
sudo rm ~/SpaceCRAFT/datalogger/*.pyc
git add *
git commit -m "$1"
git push origin master
