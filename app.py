#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import aws_cdk as cdk

from aws_cicd_cdk.aws_cicd_cdk_stack import AwsCicdCdkStack

load_dotenv()

app = cdk.App()
AwsCicdCdkStack(app, "AwsCicdCdkStack",
                env=cdk.Environment(account=os.getenv('CDK_ACCOUNT'),
                                    region=os.getenv('CDK_REGION')),
                )

app.synth()
