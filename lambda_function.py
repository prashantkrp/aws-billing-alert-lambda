import boto3
from datetime import datetime, timedelta

# Initialize clients
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')
sns = boto3.client('sns')

# SNS Topic ARN 
SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:927681712212:BillingAlertTopic"

# Billing threshold
THRESHOLD = 50  # USD

def lambda_handler(event, context):
    try:
        # Get time range (last 24 hours)
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(days=1)

        # Fetch billing metric
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/Billing',
            MetricName='EstimatedCharges',
            Dimensions=[
                {'Name': 'Currency', 'Value': 'USD'}
            ],
            StartTime=start_time,
            EndTime=end_time,
            Period=86400,
            Statistics=['Maximum']
        )

        # Extract billing amount
        datapoints = response['Datapoints']

        if not datapoints:
            print("No billing data found.")
            return

        current_bill = datapoints[0]['Maximum']
        print(f"Current AWS Bill: ${current_bill}")

        # Compare with threshold
        if current_bill > THRESHOLD:
            message = f"⚠️ ALERT: Your AWS bill is ${current_bill}, which exceeds the threshold of ${THRESHOLD}."

            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="AWS Billing Alert",
                Message=message
            )

            print("Alert sent via SNS!")

        else:
            print("Billing is within limit.")

    except Exception as e:
