import sys

# Import boto3
import boto3


def s3_create_bucket(session, newBucketName):

	# Create an S3 resource 
	s3 = session.resource('s3')

	# Create bucket
	new_bucket = s3.create_bucket(Bucket=newBucketName)

	# List buckets
	for bucket in s3.buckets.all():
		print(bucket)


def s3_list_objects_in_bucket(session, bucketname):

	# Create an S3 resource 
	s3 = session.resource('s3')

	# List objects (files) in an s3 bucket
	for obj in s3.Bucket(bucketname).objects.all():
		print(obj)


def main():

	print(f'AWS Python Utility Tools v1.0.1')

	args = len(sys.argv) - 1
	if args == 0:
		print(f'Error: You must specify a parameter')
		exit(1)


	# Determine function type


	# Create session
	session = boto3.Session(profile_name='nprovision')


 	# Create bucket
	#s3_create_bucket(session, sys.argv[1])

	# List a bucket's contents
	s3_list_objects_in_bucket(session, sys.argv[1])


if __name__ == '__main__':
	main()
