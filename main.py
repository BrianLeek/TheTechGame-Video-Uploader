from __future__ import unicode_literals
import youtube_dl
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from chromedriver_py import binary_path
import config
import time
import sys
import os

# This function is used to download the videos from YouTube. Could be a whole playlist or just one video at a time.
def download_youtube_video():
    global ydl_opts_video, ydl_opts_playlist, video_id, playlist_id, info_dict, video_title, video_desc

    # Set the name of the output file for a video or videos downloaded from a playlist from YouTube.
    ydl_opts_video = {'outtmpl': '%(autonumber)s %(title)s.%(ext)s'}
    ydl_opts_playlist = {'outtmpl': '%(playlist_index)s %(title)s.%(ext)s'}

    # If "downloads" is set to "True" in config.py go through the process of downloading the video from YouTube. This changes depending on if "download_opt" is set to "video" or "playlist" in config.py.
    if config.downloads == True:
        if config.download_opt == "video":
            try:
                video_id = input("Video ID From YouTube (Example: dQw4w9WgXcQ): ")
                print("Downloading video...")
                with youtube_dl.YoutubeDL(ydl_opts_video) as ydl_video:
                    ydl_video.download([f'{config.youtube_video_url}{video_id}'])

                    # Get the title and description of the video for later use.
                    info_dict = ydl_video.extract_info(f"{config.youtube_video_url}{video_id}", download=False)
                    video_title = info_dict.get('title', None)
                    video_desc = info_dict.get('description', None)
                print("Successfully downloaded video.")
            except ValueError:
                print("Failed to download video. Please try again.")
                sys.exit()
        # Downloads the videos from a playlist but no way to save the title and description for those videos yet.
        elif config.download_opt == "playlist":
            try:
                playlist_id = input("Playlist ID (Example: PLIREbX-q9JYkQzRmQOjvZsrJQQVX2nGR9): ")
                print("Downloading videos in playlist...")
                with youtube_dl.YoutubeDL(ydl_opts_playlist) as ydl_playlist:
                    ydl_playlist.download([f'{config.youtube_playlist_url}{playlist_id}'])

                    # info_dict = ydl.extract_info(config.video_url, download=False)
                    # video_title = info_dict.get('title', None)
                    # video_desc = info_dict.get('description', None)
                print("Successfully downloaded videos in playlist.")
            except ValueError:
                print("Failed to download video in playlist. Please try again.")
                sys.exit()
        else:
            print('Please enter a valid option in "download_opt" in config.py and try again.')
            sys.exit()
    else:
        pass

# This function will be used later to load the Selenium script and options.
def load_selenium():
    global options, prefs, driver

    # Load the Selenium part of the script.
    options = Options()
    prefs = {"profile.default_content_setting_values.notifications" : 2} # Press "Allow" on the notifications popup.
    # Disable images from being displayed if "disable_images" is set to "True" in config.py.
    if config.disable_images == True:
        disable_images_prefs = {"profile.managed_default_content_settings.images": 2}
        prefs.update(disable_images_prefs)
    else:
        pass
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--no-sandbox")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.headless = config.headless # Run script in headless mode or not. Uses value from config.py.
    if config.custom_user_dir == True:
        options.add_argument(f"--user-data-dir={config.browser_user_dir}")
    else:
        pass

    driver = webdriver.Chrome(executable_path=binary_path,chrome_options=options)

# This function will soon be used to cycle through the videos, select one and be used to input the correct titles and descriptions (maybe). For now it's just used to select the number in the title for downloaded videos.
def cycle_through_videos():
    if config.download_opt == "video":
        video_number_str = "00001"
    elif config.download_opt == "playlist":
        video_number_str = "001"

# This function contains all other functions that the script will use if the user wants to upload to TheTechGame.com.
def thetechgame_mode():
    # This function will be used to log into TheTechGame.com. Login details set in config.py
    def thetechgame_login():
        driver.get(f"{config.ttg_base_url}{config.ttg_login_url}")

        if config.ttg_already_loggedin == False:
            try:
                print(f"Logging into {config.ttg_base_url}")
                # This is used on TheTechGame because sometimes the script doesn't input the login info so with this it clicks "Login" again to reload the page and it works everytime.
                login_button = driver.find_element_by_xpath('//*[@class="forumlink"]')
                login_button.click()

                time.sleep(2)

                # Find the login username input field, click it, then input your username set in config.py.
                login_username = driver.find_element_by_name(f"{config.ttg_html_login_username_field_id}")
                login_username.click()
                login_username.send_keys(f"{config.ttg_username}")

                # Find the login password input field, click it, then input your password set in config.py.
                login_password = driver.find_element_by_name(f"{config.ttg_html_login_password_field_id}")
                login_password.click()
                login_password.send_keys(f"{config.ttg_password}")

                driver.find_element_by_name("submit").click()

                print(f"Successfully logged into {config.ttg_base_url}")

                time.sleep(2)

                driver.get(f"{config.ttg_base_url}{config.ttg_upload_url}")
            except ValueError:
                print(f"Failed to log into {config.ttg_base_url}. Please check your login details in config.py and try again.")
        else:
            time.sleep(2)
            driver.get(f"{config.ttg_base_url}{config.ttg_upload_url}")
            time.sleep(2)

    # This function will be used on the submit video page to input the title, description, etc. Also to select the video to be uploaded.
    def thetechgame_video_upload_page():
        # Find the video title input field, click it, then input the video title.
        print(f"\nEntering video title: {video_title} {config.video_title_}")
        video_title_input = driver.find_element_by_id(f"{config.ttg_html_video_title_field_id}")
        video_title_input.click()
        video_title_input.send_keys(f"{video_title} {config.video_title_}") # Input the title from YouTube then followered up by a custom one if set in config.py.

        cycle_through_videos()

        # Select the video input field and select the video.
        print(f"Selecting video: {config.videopath}{video_number_str} {video_title}.{config.video_out_opt}")
        video_upload_input = driver.find_element_by_id(f"{config.ttg_html_video_upload_filed_id}").send_keys(f"{config.videopath}{video_number_str} {video_title}.{config.video_out_opt}") # Looks in the path set in config.py and tries to find a video that was downloaded containing the title from YouTube that ends in the extension set in config.py.

        # Find the video category input field, click it, then select the video category which is set in config.py.
        print(f"Selecting video category number: {config.ttg_html_video_cat_number}")
        video_cat = Select(driver.find_element_by_id(f"{config.ttg_html_video_cat_field_id}"))
        video_cat.select_by_index(config.ttg_html_video_cat_number)

        # Find the video description input field, click it, then input the video description.
        if config.custom_desc == False:
            print(f"Entering video description: {video_desc}")
        else:
            print(f"Entering video description: {config.video_desc_}")
        video_desc_input = driver.find_element_by_id(f"{config.ttg_html_video_desc_field_id}")
        video_desc_input.click()
        if config.custom_desc == False:
            video_desc_input.send_keys(f"{video_desc}") # Input the description pulled from YouTube for the video.
        else:
            video_desc_input.send_keys(f"{config.video_desc_}") # Input the custom description for the video if set in config.py.

        time.sleep(5) # Set to 5 to allow enought time to input the info.

        # Find the video submit button and click it.
        print("Pressing submit video button.")
        print("Waiting on video to finish submitting.")
        video_submit_button = driver.find_element_by_css_selector("#buttons > button:nth-child(1)").click()
        print("Successfully submitted the video. Please run the script again to submit another.")

        sys.exit()

    # The multiple videos part of this function is still in development and should not be used but it will allow you to download a set videos from a playlist and cycle through them and upload them to TheTechGame with the right titles, descriptions, etc.
    # If using this function "video_upload_repeat" must be set to "True" in config.py
    def thetechgame_video_upload_multiple():
        # Keep uploading videos if video_upload_repeat = True and until the script has uploaded 10 videos.
        if config.video_upload_repeat == True:
            thetechgame_video_upload_page()

            video_uploading_num = 1 # Always starts at 1
            while video_uploading_num < config.ttg_video_uploading_total:
                try:
                    print(f"Submitting video {video_uploading_num} of {config.ttg_video_uploading_total}")
                    driver.get(f"{config.ttg_base_url}{config.ttg_upload_url}")
                    thetechgame_video_upload_page()

                    video_uploading_num = video_uploading_num + 1
                    print(f"Successfully submitted video {video_uploading_num} of {config.ttg_video_uploading_total}")
                except ValueError:
                    print(f"Failed to submit video {video_uploading_num} of {config.ttg_video_uploading_total}")
                    sys.exit()
            else:
                pass
        else:
            thetechgame_video_upload_page()

    thetechgame_login()
    thetechgame_video_upload_multiple()

download_youtube_video()

if config.video_upload == True:
    load_selenium()
    thetechgame_mode()
elif config.playlist_upload == True:
    load_selenium()
    thetechgame_mode()
else:
    sys.exit()
