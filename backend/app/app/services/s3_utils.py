# app/services/s3_utils.py

from app.services.s3_service import s3, BUCKET

def upload_file_to_s3(local_path, s3_key):
    s3.upload_file(
        local_path,
        BUCKET,
        s3_key
    )

    return f"s3://{BUCKET}/{s3_key}"