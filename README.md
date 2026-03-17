# AWS Billing Alert System using Lambda, Boto3, and SNS

## 📌 Objective
This project aims to monitor AWS billing automatically and send alerts when the billing exceeds a predefined threshold using AWS services.

---

## 🛠️ Services Used
- AWS Lambda
- Amazon SNS (Simple Notification Service)
- Amazon CloudWatch
- Amazon EventBridge
- IAM (Identity and Access Management)
- Python (Boto3)

---

## ⚙️ Project Workflow
1. AWS Lambda function fetches billing data from CloudWatch.
2. The billing amount is compared with a predefined threshold.
3. If the threshold is exceeded, an alert is sent using SNS.
4. EventBridge triggers the Lambda function daily.

---

## 💻 Lambda Function Code
The Lambda function is implemented in Python using Boto3 to:
- Retrieve AWS billing metrics
- Compare billing threshold
- Send notification via SNS

(File: `lambda_function.py`)

---

## 🔄 Automation
- EventBridge is used to schedule the Lambda function.
- Execution frequency: `rate(1 day)`

---

## 📸 Screenshots
Include the following:
- SNS Topic creation
- Email subscription confirmation
- IAM Role setup
- Lambda function code
- EventBridge schedule
- Lambda test execution
- Email alert received

---

## ⚠️ Important Note
**The “Receive Billing Alerts” option was not visible because the account is a linked account. Billing preferences are managed at the payer account level, so this setting could not be enabled.**

Due to this limitation, actual billing metrics may not be available. However, the system logic and alert mechanism were successfully implemented and tested.

---

## ✅ Output
- The system successfully triggers the Lambda function.
- SNS sends email notifications when the threshold condition is met (tested using simulated values).

---

## 🚀 Future Enhancements
- Integration with Slack/WhatsApp alerts
- Real-time cost dashboard using AWS services
- Advanced cost anomaly detection

---

## 👤 Author
Prashant Kumar
