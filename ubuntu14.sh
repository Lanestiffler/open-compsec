sudo apt-get install ufw
sudo apt-get install rkhunter
sudo apt-get install gcloud

ufw enable
rkhunter --update
rkhunter --scan

sudo apt-get upgrade
