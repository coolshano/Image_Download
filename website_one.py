import requests

def download_images(url,directory, file_name):

    try:
        image_content = requests.get(url)

        if image_content.status_code == 200:

            with open(f"{input_dir}/{file_name}.png","wb") as capture:
                capture.write(image_content.content)

    except Exception:
        print("Download Failed!")


input_url = input("Please input image url: ")
input_dir = input("Please input directory to download image: ")
file_name = input("Enter file name: ")
download_images(url=input_url, directory=input_dir, file_name=file_name)


