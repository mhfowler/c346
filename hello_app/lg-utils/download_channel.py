import os
import urllib

from hello_app.arena import arena as arena
from hello_app.hello_settings import ENV_DICT, DATA_PATH


def download_channel(slug, dest_folder):
    arena_api = arena.Arena(access_token=ENV_DICT['ARENA_TOKEN'])

    channel = arena_api.channels.channel(slug)
    end = False
    page = 0
    links = []
    while not end:
        contents = channel.contents(page=page)['contents']
        end = not contents
        for block in contents:
            source = block['source']
            if source:
                url = source['url']
                links.append(source)
                print('url: {}'.format(url))
        page += 1

    # for each link download it into a folder
    for index, source in enumerate(links):
        try:
            if source['title'] and source['url']:
                d = os.path.join(dest_folder, source['title'])
                print('++ downloading {}'.format(source['title']))
                urllib.request.urlretrieve(source['url'], d)
        except:
            print('++ failed to download: {}'.format(source['url']))

if __name__ == '__main__':
    dest = os.path.join(DATA_PATH, 'good-shapes')
    if not os.path.exists(dest):
        os.makedirs(dest)
    download_channel(slug='good-shapes', dest_folder=dest)