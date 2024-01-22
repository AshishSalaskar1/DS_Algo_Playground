from utils import get_user_details, register_upload, upload_image_to_linkedin, create_post_with_image, validate_media_asset

auth_token = ""

def share_post_with_image():
    # GET USER ID
    print("=> Fetching User ID...")
    user_response = get_user_details(oauth_token=auth_token)
    user_id = user_response.get("sub")

    # REGISTER UPLOAD
    print("=> Register Image Upload...")
    register_upload_response = register_upload(oauth_token=auth_token,user_id=user_id)
    # print(register_upload_response)
    upload_url = register_upload_response["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["uploadUrl"]
    media_asset_url = register_upload_response["value"]["asset"]

    print(media_asset_url)

    validate_media_asset(asset_id=media_asset_url.split(":")[-1], oauth_token = auth_token)
    print()


    # UPLOAD IMAGE
    print("=> Uploading image...")
    file_path = "C:/Users/ashis/Desktop/fake_note.png"
    upload_image_to_linkedin(
        upload_url=upload_url,
        oauth_token=auth_token,
        image_path = file_path
    )

    validate_media_asset(asset_id=media_asset_url.split(":")[-1], oauth_token = auth_token)
    print()

        
    # SHARE POST WITH IMAGE
    print("=> Sharing post with uploaded image...")
    post_content = "TESTING THE DEV API..."
    create_post_with_image(
        user_id=user_id, 
        post_text=post_content,
        oauth_token=auth_token, 
        image_media_url=media_asset_url
        
    )

share_post_with_image()
    

