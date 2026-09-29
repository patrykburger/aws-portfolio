# AWS S3 Static Portfolio Website

Welcome to my portfolio repository! This project showcases a modern, high-contrast black-and-white personal portfolio website natively hosted in the Amazon Web Services (AWS) cloud ecosystem.

## 🚀 Overview

The portfolio features a sleek, minimalist UI/UX design with smooth GSAP animations, interactive cursor micro-interactions, and a seamless B&W profile image mask. It serves as both a personal tech showcase and a hands-on cloud architecture implementation.

### Key Technologies:
* **Frontend:** HTML5, CSS3, JavaScript (ES6+), GSAP (GreenSock Animation Platform)
* **Cloud Infrastructure:** Amazon Web Services (AWS)
  * **Amazon S3:** Static Website Hosting & Bucket Policies
  * **AWS CLI:** Automated local-to-cloud file synchronization
* **Version Control:** Git & GitHub

---

## 🛠️ AWS Cloud Architecture & Deployment

1. **Amazon S3 Bucket:** Configured for public static website hosting with custom JSON bucket policies for secure `GetObject` read operations.
2. **AWS CLI Sync:** Synchronized directly from the local development environment (`/portfolio`) to S3 using optimized deployment commands:
   ```bash
   aws s3 sync . s3://aws-portfolio-patryk/ --delete
