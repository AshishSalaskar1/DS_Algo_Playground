from utils import get_user_details, register_upload, upload_image_to_linkedin, create_post_with_image, validate_media_asset

auth_token = "AQXxIVWZsSkqg-072oxsGZxo2bZI7Lf0T1S1N_Fj8xsD46Sok9BpUgx7dM5Rj7UPG0khozvBgHsUCtbOAa-80CEj_GGIV2FTq-sUAuN0LonPcpGtT4tuDrdBwxx4gG7lEzecsk32hCha_3wxHBupsggtOb_BOdPmwzGzZ6OoXKX3UIbpXoSBTy74LDZhkpzk0qkqAyv0tq2z4w73f42-XN1N34Ss0a8h1IhhulYrn6NdU3IgMKa0FGewH-Ibcj_c2VhBgpIFDM8SazxW1OYZN1dLI7I1-ByQfpBhrWMAG617F4HytjhVxHW2TbrKy_bla_oecj49a4i0sIl50w2Hky1RTQEhlg"

def share_post_with_image():
    # # GET USER ID
    # print("=> Fetching User ID...")
    # user_response = get_user_details(oauth_token=auth_token)
    # user_id = user_response.get("sub")

    # # REGISTER UPLOAD
    # print("=> Register Image Upload...")
    # register_upload_response = register_upload(oauth_token=auth_token,user_id=user_id)
    # # print(register_upload_response)
    # upload_url = register_upload_response["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["uploadUrl"]
    # media_asset_url = register_upload_response["value"]["asset"]

    # print(media_asset_url)

    # validate_media_asset(asset_id=media_asset_url.split(":")[-1], oauth_token = auth_token)
    # print()


    # UPLOAD IMAGE
    upload_url = 'https://api.linkedin.com/mediaUpload/sp/D5622AQEoALqTo-Pdig/uploaded-image/0?ca=vector_feedshare&cn=uploads&m=AQJw_wp5oO3FOgAAAY0y_Vi7xTCgnnTZY8w2bvwdJcGC5702hN4ap7K_cyI&app=216043314&sync=0&v=beta&ut=2OfDgjv3LMSb41'
    print("=> Uploading image...")
    file_path = "D:/Github\DS_Algo_Playground/Code_Snippets/LinkedIn_API/UPLOADFILE_API/img.png"
    upload_image_to_linkedin(
        upload_url=upload_url,
        oauth_token=auth_token,
        image_path = file_path
    )

    # validate_media_asset(asset_id=media_asset_url.split(":")[-1], oauth_token = auth_token)
    # print()

        
    # # SHARE POST WITH IMAGE
    # print("=> Sharing post with uploaded image...")
    # post_content = "TESTING THE DEV API..."
    # create_post_with_image(
    #     user_id=user_id, 
    #     post_text=post_content,
    #     oauth_token=auth_token, 
    #     image_media_url=media_asset_url
        
    # )

share_post_with_image()
    

