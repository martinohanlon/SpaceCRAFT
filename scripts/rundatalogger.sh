#expects 2 parameters
#time_to_run - the time in seconds the data logger should run for
#interval - the interval in seconds between data reads
#rundatalogger.sh <time_to_run> <interval>

#create variables
dateandtime=$(date +"%Y-%m-%d-%H-%M-%S")
outputdir="/home/pi/data"
datafile="$outputdir/data.$dateandtime.csv"
logfile="$outputdir/output.$dateandtime.log"

#create an output directory
mkdir -p $outputdir

#run data logger
sudo stdbuf -oL python /home/pi/SpaceCRAFT/spacecraft/astropidatalogger.py $datafile $1 $2 > $logfile 2>&1

#gzip datafile
gzip $datafile
