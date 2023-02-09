#! /bin/bash
yum update -y
yum install python3 -y
pip3 install flask
yum install git -y
cd /home/ec2-user
wget -P templates https://raw.githubusercontent.com/serdarcw/cli_deneme/master/templates/index.html
wget -P templates https://raw.githubusercontent.com/serdarcw/cli_deneme/master/templates/result.html
wget https://raw.githubusercontent.com/serdarcw/cli_deneme/master/app.py
python3 app.py



# #!/bin/bash -x
# yum update -y
# yum install python3 -y
# pip3 install flask
# cd /home/ec2-user
# FOLDER="https://raw.githubusercontent.com/altazbhanji/my-repository/main/Project-001-Roman-Numerals-Converter"
# wget ${FOLDER}/app.py
# mkdir templates
# cd templates
# wget ${FOLDER}/templates/index.html
# wget ${FOLDER}/templates/result.html
# cd ..
# python3 app.py