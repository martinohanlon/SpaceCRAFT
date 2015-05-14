#create variables
dateandtime=$(date +"%Y-%m-%d-%H-%M-%S")
outputdir="/home/pi/data"
datafile="$outputdir/data.$dateandtime.csv"
logfile="$outputdir/output.$dateandtime.log"

#create an output directory
mkdir -p $outputdir

#run data logger
sudo python /home/pi/SpaceCRAFT/datalogger/astropidatalogger.py $datafile 43200 1 > $logfile 2>&1

#gzip datafile
gzip $datafile
