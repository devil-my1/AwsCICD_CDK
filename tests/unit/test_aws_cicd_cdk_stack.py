import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cicd_cdk.aws_cicd_cdk_stack import AwsCicdCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cicd_cdk/aws_cicd_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCicdCdkStack(app, "aws-cicd-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
