# LocalStack

A fully functional local AWS cloud stack. Develop and test your cloud & Serverless apps offline! 

[GitHub](https://github.com/localstack/localstack)

## Useage

First export:

```shell
export AWS_ACCESS_KEY_ID=dummy; export AWS_SECRET_ACCESS_KEY=dummy;
```

Create an S3 bucket:

```shell
aws --endpoint-url=http://localhost:4572 s3 mb s3://django
```

Attach an ACL to make it readable:

```shell
aws --endpoint-url=http://localhost:4572 s3api put-bucket-acl --bucket django --acl public-read
```

List buckets to verify it worked:

```shell
aws --endpoint-url=http://localhost:4572 s3 ls s3://django
```