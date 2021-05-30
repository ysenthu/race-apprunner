# Race App Runner

Sample Flask Application developed to deploy on AWS App Runner.

Full instructions to try out App Runner can be found at : https://medium.com/@ysenthu/race-aws-app-runner-with-copilot-d94bd4d2e73f

## Prerequisites
* Setting up AWS CLI and Credentials. 
* Installing Copilot.
* Installing Docker.

## Initialization

```copilot init ```

The init command sets up your project on AWS, including the infrastructure and manifests you'll need to deploy your app. It will also ask you few interactive questions about the application how you wanna run it.
The First question would be the architecture type to be selected, in our scenario, it's Request-Driven Web Service. The rest of the questions will be targeted around the Application Name, Docker file Location. It will take around 5 minutes for this to finish, Copilot will setup all the required IAM, KMS Keys and other Resources using Cloud formation.

## Deployment 

Deploying apps to AWS App Runner is as simple as,

```copilot deploy ```

The above command will do the below tasks,

* Build your local Dockerfile into an image.
* Tag it with the value from --tag or the latest git sha (if you're in a git directory).
* Push the image to ECR.
* Package your manifest file and addons into CloudFormation.
* Deploy application on App Runner. 
