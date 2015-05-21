cd ~/SpaceCRAFT
sudo rm ~/SpaceCRAFT/spacecraft/*.pyc
sudo rm -R ~/SpaceCRAFT/spacecraft/__pycache__
git add -A
git commit -m "$1"
git push origin master
