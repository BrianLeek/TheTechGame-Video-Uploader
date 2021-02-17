# TheTechGame Video Uploader
TheTechGame Video Uploader 0.1 by [Brian Leek](https://brianleek.me/).

## About 
This is a script created in Python with Selenium that downloads videos from [YouTube](https://youtube.com/) and then uploads them to [TheTechGame](https://thetechgame.com). This script only uploads one video at a time to respect [TheTechGame](https://thetechgame.com) rules and to prevent spamming.

## Installation
1. Download or clone the GitHub repo.
2. Run `setup.sh`. This will install all the needed Python dependencies that are in requirements.txt file and setup `config.py` for you.
3. That's it! Now run `python main.py` and enjoy.

## Usage

Run `main.py` then the script will ask you for the ID for the video on YouTube you would like to download. Example of a video ID looks like: `dQw4w9WgXcQ`. Then a few things will happen after you input the ID:

1. The script will use YouTube DL to download the video.
2. After the script will go to TheTechGame.com and login with the set info.
3. Then the script will open the submit video page and enter the required info.
4. Submits the video and exits the script.

That's it! It isn't the fastest method or the best but it works.

## Options

### Enabling Headless Mode
By enabling headless mode you can run the script in the background well your doing other things with no broswer window in the way. To enable headless mode just open `config.py` and find `headless = False` and change it to `True`. This really hasn't been tested.

### Disable Images
By setting `disable_images` to `True` in `config.py` the script will not load images on TheTechGame when it goes to login and submit a video. Keep in mind for the `config.py` file to be created you need to run `setup.sh` if this your first time running the script.

### Custom Video Descripion (TheTechGame)
If you would like to use your own description for the video you are submitting to TheTechGame open `config.py` and set `custom_desc` to `True`. After, set your descripion in `video_desc_` and save. Now the script will use that descripion instead of the one from YouTube. Keep in mind for the `config.py` file to be created you need to run `setup.sh` if this your first time running the script.

### Change Video Category
If you would like to select a different video category for the video your are submitting to TheTechGame open `config.py` and find `ttg_html_video_cat_number` and change the number to the category you want. Keep in mind for the `config.py` file to be created you need to run `setup.sh` if this your first time running the script.

### Custom Broswer Profile
If you would like to set a custom broswer profile to keep you login to TheTechGame open `config.py` and set `custom_user_dir` to `True` and set the path to the profile in `browser_user_dir`. To stay signed in to TheTechGame run the script once with the profile to allow it to signin to TheTechGame then after set `ttg_already_loggedin` to `True` in `config.py`. This will skip going to the signin page everytime the script runs. Keep in mind for the `config.py` file to be created you need to run `setup.sh` if this your first time running the script.

### Update TheTechGame Login
When you first setup the script with `setup.sh` it will ask for your login info and uses that but if you want to update it after just open `config.py` and find `ttg_username` and `ttg_password` and update your login there. 

## Changelog:
### 0.1:
 - Initial release

## Contributing
If you would like to contribute to this project in any way, feel free too. You will be credited for any work you do. Please make sure to test your code before submitting it. Thanks!
