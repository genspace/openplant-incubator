#!/bin/bash

RSA_PEM="$1"
BASTION="$(terraform output bastion_public_ip)"

echo $RSA_PEM
echo $BASTION

ssh -i $RSA_PEM\
    ec2-user@${BASTION}
