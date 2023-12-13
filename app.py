#!/usr/bin/env python3
import aws_cdk as cdk

from aws_cicd_cdk.aws_cicd_cdk_stack import AwsCicdCdkStack


app = cdk.App()
AwsCicdCdkStack(app, "AwsCicdCdkStack",
                env=cdk.Environment(account="241916871697",
                                    region="ap-northeast-1"),
                )

app.synth()
