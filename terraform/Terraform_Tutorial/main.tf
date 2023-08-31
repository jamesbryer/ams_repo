provider "aws" {
  region     = "eu-west-2"
}

resource "aws_instance" "EC2" {
  count         = 2
  ami           = var.ami-id
  instance_type = var.instance-type
  tags = {
    Name = "machine ${count.index}"
  }
  lifecycle {
    create_before_destroy = true
    ignore_changes = [tags, ami, instance_type]
  }
  timoeouts {
    create = "5m"
    delete = "1h"
  }
}