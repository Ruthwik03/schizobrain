from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from app.api.dependencies import get_current_user
from app.models.record import RecordModel
from app.services.file_service import FileService
from app.db.database import get_database
from app.services.s3_utils import upload_file_to_s3

router = APIRouter()

@router.post("/")
async def upload_mri(
    file: UploadFile = File(...),
    current_user: dict = Depends(get_current_user)
):
    # Validate file type
    if not (
        file.filename.endswith('.nii') or
        file.filename.endswith('.nii.gz') or
        file.filename.endswith('.dcm')
    ):
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Only .nii, .nii.gz, .dcm allowed."
        )

    # Create record with filename saved
    record = RecordModel(
        user_id  = current_user["user_id"],
        filename = file.filename,
        scan_path= "",
    )

    # Save file to disk via FileService
    file_path = await FileService.save_upload_file(
        file,
        current_user["user_id"],
        record.record_id
    )
    s3_path = upload_file_to_s3(
        file_path,
        f"uploads/{record.record_id}_{file.filename}"
    )

    # Update scan_path after saving
    record.scan_path = file_path
    record.s3_scan_path = s3_path

    # Persist record to MongoDB
    db = get_database()
    await db.records.insert_one(record.dict())

    return {
        "message"  : "File uploaded successfully",
        "record_id": record.record_id
    }