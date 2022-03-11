apt-get update
apt-get install -y git expect

git config --global user.name "chiupam"
git config --global user.email "com"
mkdir ~/.ssh/
echo "-----BEGIN OPENSSH PRIVATE KEY-----
-----END OPENSSH PRIVATE KEY-----" > ~/.ssh/id_rsa
chmod 700 ~/.ssh/id_rsa
cd /serverless
echo -E "#!/usr/bin/expect

spawn git pull origin master
expect "yes/no"
send "yes\r"
interact
" > ssh.sh
expect ssh.sh
