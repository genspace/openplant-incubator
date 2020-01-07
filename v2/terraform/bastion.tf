resource "aws_default_vpc" "default" {}

resource "aws_key_pair" "bastion_key" {
  key_name      = "${var.ssh_key_name}"
  public_key    = "${var.ssh_key_pub}"
}

resource "aws_instance" "bastion" {
  ami                           = "${var.amis[var.region]}"
  key_name                      = "${aws_key_pair.bastion_key.key_name}"
  instance_type                 = "t2.micro"
  vpc_security_group_ids        = ["${aws_security_group.bastion-sg.id}"]
  associate_public_ip_address   = true
}

resource "aws_security_group" "bastion-sg" {
  name          = "bastion-security-group"
  vpc_id        = "${aws_default_vpc.default.id}"

  ingress {
    protocol    = "tcp"
    from_port   = 22
    to_port     = 22
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    protocol    = -1
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}

output "bastion_public_ip" {
  value = "${aws_instance.bastion.public_ip}"
}
