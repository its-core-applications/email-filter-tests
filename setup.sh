pip3 install --user pytest

# brute force removal of the datastore sync
sudo crontab -r

sudo tee /etc/mail/recipient.deny <<EOF
postmaster@example.com
EOF

sudo tee /etc/mail/recipient.trust <<EOF
postmaster@umich.edu
EOF

sudo tee /etc/mail/string.deny <<EOF
sibboleth
EOF
