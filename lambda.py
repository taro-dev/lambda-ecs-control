import boto3
from botocore.exceptions import ClientError
def lambda_handler(event, context):
    try:
        client = boto3.client('ecs')
        for cluster_name, service_name in [('clusterName', 'seaviceName')]:
            service_update_result = client.update_service(
                cluster = cluster_name,
                service = service_name,
                desiredCount = 0 # ここの数を増減させる
            )
            print(service_update_result)
    except ClientError as e:
        print("exceptin: %s" % e)
