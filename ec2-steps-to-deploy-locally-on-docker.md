# ec2 - steps-to-deploy-locally-on-docker

##  SSH to provision EC2 instance
```bash
ssh -i <yourpemkey> ubuntu@<public ip>
```

## update container
```bash
sudo apt-get update -y
```
```bash
sudo apt-get upgrade -y
```

## install python      
```bash
sudo apt-get install python3
```

## install pip      
```bash
sudo apt-get install pip -y
```

```bash
pip3 install --upgrade awscli
```

## install aws cli 
```bash
sudo apt-get install awscli -y   
```
# choose you region and country when prompt

## configure aws configuration
```bash
aws configure
```

## Since model upload after training and application will download model from s3, hence we need to configure
```bash
AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
AWS_DEFAULT_REGION=us-east-1
```

```bash
sudo apt-get install libgl1-mesa-glx -y
```

## install wget
```bash
sudo apt-get install wget -y
```

## install git
```bash
sudo apt-get install git -y
```

## install nano
```bash
sudo apt-get install nano
```

## install vi
```bash
sudo apt-get install vi
```

## install unzip
```bash
sudo apt-get install unzip
```

## git clone
```bash
git clone https://github.com/mayankchugh-learning/End-to-end-Object-Detection-Project.git
```

## change directory to clonned repository
```bash
cd End-to-end-Object-Detection-Project
```

## install all requirement
```bash
pip install -r requirements.txt
```

## to check if aws cli is installed
```bash
aws --version
```

## execute application
```bash
python3 app.py
```
