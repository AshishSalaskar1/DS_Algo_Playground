import requests
import json
import mimetypes
import base64


def read_image(image_path):
    with open(image_path, 'rb') as file:
        content_type, _ = mimetypes.guess_type(image_path)
        # image_base64 = base64.b64encode(file.read()).decode('utf-8')

        return file.read(), content_type

def get_user_details(oauth_token):
    url = "https://api.linkedin.com/v2/userinfo"

    payload = {}
    headers = {
    'Authorization': f'Bearer {oauth_token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def register_upload(oauth_token, user_id):
    url = "https://api.linkedin.com/v2/assets?action=registerUpload"

    payload = json.dumps({
    "registerUploadRequest": {
            "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
            "owner": f"urn:li:person:{user_id}",
            "serviceRelationships": [
                {
                    "relationshipType": "OWNER",
                    "identifier": "urn:li:userGeneratedContent"
                }
            ]
        }
    })

    headers = {
        'X-Restli-Protocol-Version': '2.0.0',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {oauth_token}'    
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()


def upload_image_to_linkedin(oauth_token, upload_url, image_path):

    url = upload_url
    img_content, content_type = read_image(image_path)

    payload = img_content
    headers = {
        'Authorization': f'Bearer {oauth_token}',
        'Content-Type': content_type    
    }

    # print(img_content)

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text, response.status_code)


def validate_media_asset(asset_id, oauth_token):

    url = f"https://api.linkedin.com/v2/assets/{asset_id}"

    payload = {}
    headers = {
        'Authorization': f'Bearer {oauth_token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.json())



def create_post_with_image(user_id, post_text, oauth_token, image_media_url):
    url = "https://api.linkedin.com/v2/ugcPosts"

    payload = json.dumps({
            "author": f"urn:li:person:{user_id}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": post_text
                },
                "shareMediaCategory": "IMAGE",
                "media": [
                    {
                    "status": "READY",
                    "description": {
                        "text": "Center stage!"
                    },
                    "media":image_media_url,
                    "title": {
                        "text": "LinkedIn Talent Connect 2021 - random"
                    }
                    }
                ]
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
    )

    
        
    headers = {
        'X-Restli-Protocol-Version': '2.0.0',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {oauth_token}'    
    }

    # print(payload)
    # print(headers)
    

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
