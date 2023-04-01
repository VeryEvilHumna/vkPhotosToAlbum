# Group Album Photo Uploader for Vkontakte

![Tested with Python 3.11.0](https://img.shields.io/badge/tested%20with-Python%203.11.0-brightgreen)

This Python script is designed to upload photos from a specified directory to a VK album using the VK API.


## Requirements

You need to have a VK account and a group with an album to upload the photos to. 

## Usage

1. Install requirements using this command:
   
    ```
    pip install -r requirements.txt
    ```
2. Configure the `config.py` file with your VK API access token, group and album ID, and the directory path where the photos are located on your system.
3. Run the script using this command:

    ```
    python main.py
    ```

## Configuration

- `TOKEN`: Your **user** VK API access token. (you can get it from https://vkhost.github.io/)
- `GROUP_ID`: The ID of the group you want to upload the photos to.
- `ALBUM_ID`: The ID of the album in the specified group to upload the photos to.
- `PHOTOS_DIR`: The directory path where the photos are located on your system.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
