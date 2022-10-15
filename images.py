from google_images_search import GoogleImagesSearch

gis = GoogleImagesSearch('AIzaSyDdj1tm_nBO-Z0ZAWbwcLDgF5LsbQXB-Qo','c285b6813ec6e4a17')

_search_params = {
    'q':'South Korea Hospital Building',
    'num': 1,
    'safe': 'off',
    'imgType': 'photo',
    'imgSize': 'medium'
}

gis.search(search_params = _search_params)

for image in gis.results():
    url = image.url
    print(url)