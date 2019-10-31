#!/bin/bash

terraform $1\
  -var-file="secret.tfvars"\
  -var-file="main.tfvars"
