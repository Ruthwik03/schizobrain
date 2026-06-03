from s3_service import s3, BUCKET



print("BUCKET =", BUCKET)

s3.upload_file(
    "test.txt",
    BUCKET,
    "uploads/test.txt"
)

print("Upload successful")