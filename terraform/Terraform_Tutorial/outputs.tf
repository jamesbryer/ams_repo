# output "ec2_id" {
#     value = aws_instance.EC2[count.index].public_ip
# }
# using this in cli for getting values from output: export TERR_IP=$(terraform output -raw ec2_id)