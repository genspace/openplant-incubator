# OpenPlant Infra

This repo contains the code necessary to spin up AWS infrastructure relevant to OpenPlant App.
Currently, it includes instructions to create an Ubuntu EC2 Server.

## How To

In order to use this repo, the user must take the following steps on their system:

1. Install [terraform]
2. Create a file in project root called `secret.tfvars` with the following contents:


>```
>access_key = "<YOUR AWS ACCESS KEY>"
>secret_key = "<YOUR AWS SECRET KEY>"
>ssh_key_name = "<RSA KEY FILE NAME>"
>ssh_key_pub = "<PUBLIC RSA KEY CONTENTS>"
>```

1. Now, run `terraform init` in the project directory to initialize terraform access
2. Simply call `./bin/do.sh apply` in the project root to create infrastructure

[terraform]: https://www.terraform.io/downloads.html
