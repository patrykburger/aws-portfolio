# AWS S3 & CloudFront Static Portfolio Website

Welcome to my portfolio repository! This project showcases a modern, high-contrast personal portfolio website hosted natively in the Amazon Web Services (AWS) cloud ecosystem.

## 🌐 Live Demo

* **Live Site:** [https://dihygzx3tp3j0.cloudfront.net](https://dihygzx3tp3j0.cloudfront.net)

---

## 🚀 Overview

The portfolio features a sleek, minimalist UI/UX design with smooth GSAP animations, interactive cursor micro-interactions, and a seamless B&W profile image mask. It serves as both a personal tech showcase and a production-grade cloud architecture implementation.

### Key Technologies:
* **Frontend:** HTML5, CSS3, JavaScript (ES6+), GSAP (GreenSock Animation Platform)
* **Cloud Infrastructure & Security:** Amazon Web Services (AWS)
  * **Amazon CloudFront:** Content Delivery Network (CDN) providing global edge caching, SSL/TLS termination (`HTTPS`), and cost optimization (AWS Free Tier: 1 TB transfer & 10M requests).
  * **Amazon S3:** Secure, private object storage acting as the CloudFront origin.
  * **Origin Access Control (OAC):** Restricts direct S3 bucket access, ensuring traffic is only routed securely through CloudFront.
  * **AWS CLI:** Automated local-to-cloud file deployment.
* **Version Control:** Git & GitHub

---

## 🛠️ AWS Cloud Architecture & Security

[ User Request ] ---> ( HTTPS ) ---> [ Amazon CloudFront (Edge) ]
|
( Origin Access Control )
|
v
[ Private Amazon S3 Bucket ]

1. **Private S3 Bucket:** Direct public access (`Block Public Access`) is fully enabled on the S3 bucket to prevent unauthorized access and untracked API request costs.
2. **CloudFront Distribution with OAC:** Configured with Origin Access Control (OAC) to securely serve static assets (`index.html`, `profile.jpg`) via AWS global Edge Locations with HTTPS encryption.
3. **Cost & Performance Optimization:** By caching static assets at CloudFront edge locations, direct `GET` operations to S3 are virtually eliminated, keeping infrastructure costs at $0.00 within the AWS Free Tier limits.

---

## 💻 Local Development & Deployment Workflow

Deployment and file synchronization from the local environment (`/portfolio`) to S3 using the AWS CLI:

```bash
# Sync local assets to private S3 bucket
aws s3 sync . s3://aws-portfolio-patryk/ --delete

Note on Caching: If HTML or asset files are updated in S3, run a CloudFront invalidation to instantly refresh cached content globally:
aws cloudfront create-invalidation --distribution-id E3NHUDKPMSUKL9 --paths "/*"
