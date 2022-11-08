# python-webapp-peach
TASK

You are required to build a web application hosted on AWS. 

Infrastructure

- The web application should be served on a container. 
- The container can be hosted on an orchestration engine such as Kubernetes (EKS) or ECS or an EC2 instance. (EKS would be a plus, however due to cost implications, running it on an EC2 instance is just as valid.)
- The infrastructure on which the container runs should be provisioned using terraform.
- The docker container should be deployed using CI/CD (of your choice). 
- The code should be hosted on either GitHub or GitLab. 


Note: Very little detail is provided here to gauge what kind of instinct you as an engineer have on provisioning infrastructure reliably. Consider things such as high availability, low latency and security. Please send through questions to my email address (grace.mukendi@peachpayments.com) should you have any.



Web Application

The web application renders a page that prompts for a name, last name, email address and password to ‘register’ for accessing our application. Once the details have been stored in the db (no need to validate email address), the user can login and view their profile which simply redisplays the information previously provided by the user. 

Another endpoint is made available for managers to analyse the behaviour of end users and prospective clients. Once a user has signed up, this information should be made available in the manager’s dashboard. The signing up process events should also be made available for the managers to see, in order for them to assess whether a user has completed sign up or not.


Note: This section is the least important and should be attended to last. Ensure that your infrastructure is up and running and follows the guidelines specified before tackling this task. The language of choice is Python. You can host the application on a web server of your choice.

