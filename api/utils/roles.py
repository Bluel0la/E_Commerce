from api.v1.models.user import User
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def is_user_admin(user_id: int, db: Session) -> bool:
    user = db.query(User).filter(User.id == user_id, User.role == "Admin").first()
    return user is not None
    
def is_user_vendor(user_id: int,db: Session) -> bool:
    user = db.query(User).filter(User.id == user_id, User.role == "Vendor").first()
    return user is not None


# def is_user_member_of_vendor(user_id: int, vendor_id: int, db: Session) -> bool:
#     user_vendor = db.query(UserVendor).filter_by(user_id=user_id, vendor_id=vendor_id).first()
#     return user_vendor is not None


# # Helper function to check if user is authorized for a vendor
# def check_vendor_authorization(vendor_id: int, current_user: User, db: Session):
#     vendor = db.query(Vendor).filter(Vendor.vendor_id == vendor_id).first()
#     if not vendor:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="Vendor not found."
#         )

#     user_vendor_relationship = (
#         db.query(UserVendor)
#         .filter(
#             UserVendor.vendor_id == vendor_id, UserVendor.user_id == current_user.id
#         )
#         .first()
#     )

#     if not user_vendor_relationship:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Not authorized to perform this action on this vendor.",
#         )
#     return vendor
