# AWS Cloud-Based Student Management System

## Project Description

The AWS Cloud-Based Student Management System is a web application developed using Flask and deployed on Amazon EC2. The application allows users to manage student records by performing operations such as adding, viewing, and deleting students. Student data is securely stored in Amazon DynamoDB, while IAM Roles provide secure access between EC2 and DynamoDB without hardcoded credentials.

This project demonstrates practical implementation of cloud computing concepts including compute services, NoSQL databases, identity and access management, and cloud-native application deployment.

---

## Project Architecture Diagram

<img width="4836" height="2724" alt="Architecture-diagram" src="https://github.com/user-attachments/assets/c9673960-f851-4127-baa1-8ea852162298" />


---

## AWS Services Used

### Amazon EC2

- Hosts the Flask web application
- Processes user requests
- Connects with DynamoDB using Boto3

### Amazon DynamoDB

- Stores student records
- Provides scalable NoSQL storage
- Supports fast read and write operations

### AWS IAM

- Provides secure access permissions
- Eliminates the need for access keys inside application code

### Amazon VPC

- Provides network isolation
- Hosts EC2 instance securely within AWS infrastructure

### Security Groups

- Controls inbound and outbound traffic
- Allows HTTP and SSH access where required

---

## Technologies Used

- Amazon EC2
- Amazon DynamoDB
- AWS IAM
- AWS VPC
- Security Groups
- Python
- Flask
- Boto3
- HTML
- CSS

---

## Features

### Add Student

Users can add student records by entering:

- Student Name
- Roll Number

The information is stored in DynamoDB.

### View Students

Displays all stored student records in a tabular format.

### Delete Student

Allows removal of existing student records from DynamoDB.

### Secure Access

Uses IAM Roles attached to EC2 for secure communication with DynamoDB.

---

## Project Workflow

### Step 1

User accesses the application through a web browser.

### Step 2

HTTP requests are sent to the Flask application hosted on Amazon EC2.

### Step 3

Flask processes the request.

### Step 4

Boto3 communicates with Amazon DynamoDB.

### Step 5

Student records are stored, retrieved, or deleted.

### Step 6

Results are displayed back to the user.

---

## Learning Outcomes

Through this project, I gained hands-on experience with:

- Amazon EC2
- Amazon DynamoDB
- AWS IAM Roles
- AWS Networking Concepts
- Flask Web Development
- Boto3 SDK
- Cloud Application Deployment
- Secure AWS Service Integration

---

## Future Enhancements

- Student Update Functionality
- User Authentication
- Search Student Records
- Responsive UI Design
- Deployment with Custom Domain
- HTTPS Integration
- CI/CD Pipeline using GitHub Actions
