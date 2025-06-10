import boto3

def create_emr_cluster(cluster_name, release_label="emr-6.13.0", instance_type="m5.xlarge", instance_count=3):
    emr = boto3.client('emr')
    response = emr.run_job_flow(
        Name=cluster_name,
        ReleaseLabel=release_label,
        Instances={
            'InstanceGroups': [
                {
                    'Name': "Master nodes",
                    'Market': 'SPOT',
                    'InstanceRole': 'MASTER',
                    'InstanceType': instance_type,
                    'InstanceCount': 1,
                },
                {
                    'Name': "Core nodes",
                    'Market': 'SPOT',
                    'InstanceRole': 'CORE',
                    'InstanceType': instance_type,
                    'InstanceCount': instance_count - 1,
                },
            ],
            'KeepJobFlowAliveWhenNoSteps': False,
            'TerminationProtected': False,
        },
        Applications=[{'Name': 'Spark'}],
        JobFlowRole='EMR_EC2_DefaultRole',
        ServiceRole='EMR_DefaultRole',
        VisibleToAllUsers=True,
        AutoScalingRole='EMR_AutoScaling_DefaultRole'
    )
    print(f"Started EMR cluster with id: {response['JobFlowId']}")

if __name__ == "__main__":
    create_emr_cluster("TrafficOffloadEMR")