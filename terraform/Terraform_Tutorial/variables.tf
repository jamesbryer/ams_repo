variable "ami-id" {
  description = "AMI ID of ubuntu 20.04LTS eu-west-1"
  default     = "ami-007ec828a062d87a5"
}

variable "instance-type" {
  description = "Free tier EC2 Instance type"
  default     = "t2.micro"
}

variable "pem-key" {
  description = "Associated Key to SSH into the EC2 Instance"
  default     = "example"
}