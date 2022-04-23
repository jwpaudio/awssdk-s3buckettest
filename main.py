#Written by: Joshua Pardridge
#This script is a simple example of working with boto3 and S3. It creates a bucket that you name
#and inserts a text file into it. When you are ready, it goes back in and deletes the object and bucket

#This script requires your aws console to be preconfigured with administrative access to S3
import boto3
from tempfile import NamedTemporaryFile

s3 = boto3.resource('s3')

new_bucket = s3.Bucket(f'{input("Enter a new bucket name: ")}')

print("\nCreating your new bucket...")

new_bucket.create()
print("Your new bucket has been created!\n")

new_file_data = input("Write some text to put in your bucket: ")
new_file_name = input("What do you want to name your file?: ")

print("Saving text to bucket...\n")

with NamedTemporaryFile('w+t') as tf:
    tf.write(new_file_data)
    tf.flush()
    new_bucket.upload_file(tf.name, f'{new_file_name}.txt')

print("Check your bucket!\n")
input("Press enter to delete bucket and contents...\n")
print("Deleting bucket objects...")
new_bucket.delete_objects(
    Delete={
        'Objects': [
            {
                'Key': f'{new_file_name}.txt',
            },
        ]
    }
)
print("Deleting bucket...\n")
new_bucket.delete()

print("Bucket deleted!")