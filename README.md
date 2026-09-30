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
