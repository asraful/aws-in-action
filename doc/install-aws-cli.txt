
Step One: Download the Amazon ECS CLI

sudo curl -Lo /usr/local/bin/ecs-cli https://amazon-ecs-cli.s3.amazonaws.com/ecs-cli-linux-amd64-latest

Step Two: Verify the Amazon ECS CLI using PGP signatures 

curl -Lo ecs-cli.asc https://amazon-ecs-cli.s3.amazonaws.com/ecs-cli-linux-amd64-latest.asc

Step Three: Apply Execute Permissions to the Binary 

sudo chmod +x /usr/local/bin/ecs-cli

Step 4: Complete the Installation

ecs-cli --version

Reference : https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI_installation.html
