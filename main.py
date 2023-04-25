# -*- coding: utf-8 -*-
# Copyright 2023 @VeryEvilHumna on github

#TODO: Multithreading

# I don't f#####g know why i made this sh!t async

import asyncio
import os
import requests
from vk import API, session, exceptions

import config


ACCESS_TOKEN = config.TOKEN
GROUP_ID = config.GROUP_ID
ALBUM_ID = config.ALBUM_ID
PHOTOS_DIR = config.PHOTOS_DIR


async def upload_photo_to_album(vk_session, group_id, album_id, photo_path):
    upload_url = vk_session.photos.getUploadServer(album_id = album_id, group_id = group_id)['upload_url']

    with open(photo_path, 'rb') as photo_file:
        response = requests.post(upload_url, files={'file1': photo_file})

    upload_response = response.json()
    photo_data = vk_session.photos.save(**upload_response, album_id = album_id, group_id = group_id)[0]
    return photo_data['id']


async def upload_photos():
    vk_session = session.API(access_token=ACCESS_TOKEN, v=config.API_VERSION)

    photos = [os.path.join(PHOTOS_DIR, f) for f in os.listdir(PHOTOS_DIR) if os.path.isfile(os.path.join(PHOTOS_DIR, f))]

    if not photos:
        print(f'Error: No photos found in directory {PHOTOS_DIR}.')
        return

    photo_ids = []


### # Upload counter. Prevents loosing all progress if internet or power goes off
    if os.path.exists('UPLOAD_COUNTER'):
        with open('UPLOAD_COUNTER', 'r') as f:
            UPLOAD_COUNTER = int(f.read())
    else:
        UPLOAD_COUNTER = 0

    for i, photo in enumerate(photos[UPLOAD_COUNTER:], UPLOAD_COUNTER):
        try:
            photo_id = await upload_photo_to_album(vk_session, GROUP_ID, ALBUM_ID, photo)
            photo_ids.append(photo_id)
            print(f'Photo {UPLOAD_COUNTER + 1} of {str(len(photos))}. Successfully uploaded {photo}.')
            
            UPLOAD_COUNTER += 1
            with open('UPLOAD_COUNTER', 'w') as f:
                f.write(str(UPLOAD_COUNTER))


####### # Exceptions handling
        except exceptions.VkAPIError as e:
            print(f'Error {e.code}: {e}')



    print(f'Successfully uploaded {UPLOAD_COUNTER} photos to album {ALBUM_ID} in group {GROUP_ID}.')

    os.remove('UPLOAD_COUNTER')  # Delete the upload counter file after uploading all photos
    print('Upload counter file deleted.')

    print('Press any key to exit...')
    input()


# Entry point
if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(upload_photos())
