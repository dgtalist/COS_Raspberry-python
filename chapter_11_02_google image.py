pip install git+https://github.com/​Joeclinton1/google-images-download.git


from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()
arguments = {"keywords":"신민아", "limit":50, "print_urls":True, "format":"jpg"} 
paths = response.download(arguments) 
print(paths)
