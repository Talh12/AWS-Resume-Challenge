# AWS Cloud Resume Challenge
Welcome to my Cloud Resume Challenge project! ☁️

## [My Web - Click Here!](https://resume.resumetal.com)

![archi888888888888888888888888tecture](https://github.com/yahav123456/AWS-Resume-Challenge/assets/166650066/2d5e9c94-b320-4560-ae84-02d2a29c7c3d)



Over the course of two intensive weekends, I devoted significant effort to this project. Whether you're an experienced professional or new to AWS, I hope my project inspires and assists you on your own cloud computing journey. Let's dive in together!

# This challenge is composed of 8 main parts:

1. Write your resume in HTML and formatting it with CSS
2. Setup CloudFront distribution and S3 Bucket
4. Setting up DynamoDB and AWS Lambda for API
5. Setting up the Lambda and JavaScript to get viewer counter
6. setting up CI/CD for the frontend website and to run lambda Pytest 
7. Implementing infrastructure as code with Terraform
8. Configure GitHub Actions for CI/CD with Azure Storage


## Prerequisites
- aws account
- GitHub account
- Visual Studio Code
- A cheap domain provider (im using GoDaddy)

## Choose region: 
Before starting to work on the project in aws console, i needed to choose which region is the best for me (for best practice).
so how to choose your best region? 
1. Proximity to Users: Select a region closest to your target audience to minimize latency and improve user experience. 
I used this <a href="https://awsspeedtest.com/latency"> site</a>  to verify the latency.

2. Compliance Requirements: Ensure the chosen region complies with any legal or regulatory requirements for data sovereignty, residency, or privacy laws applicable to your application or business. (for me its not a problem)

3. Service Availability: Check the availability of AWS services you plan to use in the region. 

4. Cost Considerations: AWS pricing can vary by region, so evaluate the cost of resources and data transfer in different regions to optimize your budget.

5. Redundancy and High Availability: If high availability is critical for your application, consider deploying resources across multiple regions for redundancy and disaster recovery purposes.

![](images/latency.png)

## Front-end

## Phase-1: Building the Resume-Website

So the first phase was to build a resume static website using html and css. Since I didnt want to spend too much time on desinging the resume website I used a template from the internet and altered the code depending on how I wanted it to look. Then I added all the details necessary for the resume page.
This is the result of the staic resume page.        
![](images/website.png)



## Phase-2: Setup CloudFront distribution and S3 Bucket
This phase focuses on deploying the static site to the cloud. In AWS, this can be achieved by hosting the static site on an S3 bucket. 
AWS S3 has an option to configure it for static website hosting. Once configured, you can upload your website files directly via the AWS Management Console or the CLI. 
The image below shows the uploaded files for the static site in the S3 bucket.
You can access the static website through the endpoint provided by AWS for this specific site. 
Additionally, the S3 bucket is configured to allow traffic only from the CDN, which we will discuss later. This ensures that all requests to the static site go through the CDN, enhancing security and performance.


## Phase-3: Domain and CDN
First I bought a domain (on route53 "https://resume.resumetal.com/") for this project. 

I used Amazon Route 53 for DNS management to transfer the control of my domain to Route 53. I created a Hosted Zone for my domain and received four name servers. I then entered these name servers into Route 53, completing the domain control transfer. Afterward, I created an ACM certificate by adding a record for the domain in Route 53.

CloudFront is a Content Delivery Network (CDN), which is a network of multiple proxy servers with the primary goal of delivering content with high availability and performance. This ensures that users across different geographical locations can access the site faster.

  

## Back-end
## Phase-4: Javascript-webapp
The next challenge was to create a counter to keep track of how many times the page has been viewed, and this can be achieved using JavaScript. I used an event listener to trigger and call the main.js function whenever the DOM elements or content get reloaded. This function sends an HTTP request to an AWS Lambda function (we will discuss this in the next phase) to get the count and display it on the website. You can take a look at the code to understand how it has been done. It is simply a basic GET request.

## Phase-5: Lambda function
Now comes the important part. I have to create a function to update the count of visitors every time the page is reloaded. This can be achieved by using an HTTP trigger for the AWS Lambda function, meaning the function will run every time the page is reloaded. So, I created a function to fetch the count from the Amazon DynamoDB (next phase) and then update the count by increasing it by one, returning it to the front end to display the count.
You can check out the code in the  lambda folder on my Github



## Phase-6: Amazon DynamoDB
To store the number of visitors in AWS, I created an Amazon DynamoDB table. DynamoDB is also serverless, so I only had to pay for the resources I used. After creating the table, I set up the necessary attributes and primary key to store and retrieve the visitor count value. DynamoDB's flexible schema allowed me to adapt quickly, although it took some time to familiarize myself with its structure since it was my first time working with it. I used the AWS SDK to interact with the DynamoDB table, fetching and updating the count value as needed. 




## Phase-7: Terraform

After creating the application with the necessary services, it's time to automate the entire process. To automate the provisioning of resources in AWS, we can use Terraform, an Infrastructure as Code (IaC) tool.

To do this, I created a main.tf file and initialized Terraform using the terraform init command. I then wrote the main.tf file to recreate the function and connect it to my existing DynamoDB table, ensuring it could read data from there. I also defined the path to the function within the Terraform configuration.

Once the configuration was set, I utilized the terraform plan and terraform apply commands to provision the resources. Finally, to clean up, I used terraform destroy to delete the resources.





## CI/CD
Once I had the storage container and static website setup, it was really nice to be able to push updates via GitHub and have a Workflow automatically update the contents of the container. Plus this workflow purges the CDN cache so that any updates you make are immediately reflected.
- I followed Microsoft's docs on [Using GitHub Actions workflow to deploy a static website in Azure Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-static-site-github-actions?tabs=userlevel) which was mostly straightfoward. 
- Every required secret for backend job ,terraform and frontend job are stored as secrets in github actions. 
- Creating a cicd pipeline definitely improve the development process so the developers can focus on the product instead of focusing on deployment and management of it.

  
