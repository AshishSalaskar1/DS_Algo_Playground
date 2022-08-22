import gdown

def download_from_drive(output_path=""):
    folder_id = "16d4jOP4RGRkI4oDKUKTe__lfuY6k-Cqo"
    folder_url = f"https://drive.google.com/drive/folders/{folder_id}"

    try:
        gdown.download_folder(folder_url, output=output_path,quiet=False, use_cookies=False, )  
    except:
        print("Error while downloading file from google drive..please check folder link and access privileges") 