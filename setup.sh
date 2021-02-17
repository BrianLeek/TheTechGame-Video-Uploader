#!/bin/bash
echo "TheTechGame Video Uploader Setup"
echo ""
if [ ! -f .is_setup ]; then
    echo "Give us a second to install the Python dependencies."
    pip3 install -r requirements.txt
    if [ $? -eq 2 ]; then
        echo "Error: Something went wrong. We may need root to continue. Please put in your password to continue."
        sudo pip3 install -r requirements.txt
        if [ $? -eq 2 ]; then
            echo "Error: Cannot install Python dependencies. Check your permissions and try again."
            exit
        fi
    fi
    echo "Installed all required packages! Now, just a few questions. You can edit these later in config.py."
    echo ""
  echo "Path where videos will be saved to after downloading."
	echo "Example (Windows): C:/Users/FakeUser/Desktop/TheTechGame Video Uploader/"
	while true; do
		printf "Video Path: "
		read videopath
	if [[ "$videopath"  != "" ]]
	then
		break
	fi
	done

  echo "TheTechGame.com part of the script will not work if the login details are wrong."
	echo "Example: JohnSmith"
  while true; do
    printf "TheTechGame Username: "
    read ttg_username
  if [[ "$ttg_username"  != "" ]]
  then
    break
  fi
  done

  echo "Example: ThisIsMyPassword123!"
  while true; do
    printf "TheTechGame Password: "
    read ttg_password
  if [[ "$ttg_password"  != "" ]]
  then
    break
  fi
  done

	echo "'''
This is the config file that helps you customize the script to your liking or setup anything that is necessary to run the script.

If this is your first time running this script you will need to edit the following options:
 - videopath
 - ttg_username
 - ttg_password

Once those are filled out you will be good to go and run the script without any problems. Some of the settings below should not be touched so take caution when editing this file.

Note: You can run "setup.sh" to make filling out those options easier.
'''

# Script Options
headless = False # If set to True the script will run in the background with no browser window.
disable_images = False # If set to True the Selenium part of the script will display images being displayed in the browser.
downloads = True # If set to False the script won't download the video or videos again but will just skip that step and go right to submitting the video. Don't disbale right now because the script needs to download the video from YouTube to pull the title and description.
video_upload = True # Do you want to upload the video to the set website/mode? (True/False)
video_upload_repeat = False # Upload another video after the first upload finishes.
playlist_upload = False # Do you want to upload the video downloaded from the playlist to the set website? (True/False). Leave disbaled for now please.
download_opt = \"video\" # Would you like the script to download a video or a whole playlist? (video/playlist). Only download videos at this time not playlist.
video_out_opt = \"mp4\" # Do not edit! More extensions coming in the future.

custom_user_dir = False # Set this option to True if you are using a custom user profile, then set the path to the profile below.
# Example (Windows): C:/Users/FakeUser/AppData/Local/Google/Chrome/User Data. See https://stackoverflow.com/a/45654226.
browser_user_dir = \"$custom_profile_path\" # This can be left blank if not needed.

# YouTube DL Settings
youtube_video_url = \"https://www.youtube.com/watch?v=\" # The link to YouTube to watch a vdeio. DO NOT EDIT!
youtube_playlist_url = \"https://www.youtube.com/playlist?list=\" # The link to YouTube. DO NOT EDIT!

# Custom Input Settings
video_title_ = \"\" # Title of video to be submitted to the set website. Note: The text placed here will be placed after the title pulled from YouTube. Can be left blank.
custom_desc = False # Set to True if you would like to use a custom description instead of the one from YouTube.
video_desc_ = \"\" # Custom description of video to be submitted to the set webpage. Note: The above option needs to be set to True for this to work. Can be left blank if the above option is set to False.
# Example C:/Users/FakeUser/Desktop/TheTechGame Video Uploader/
videopath = \"$videopath\" # Path where to find videos to be uploaded. Should be the root of the scripts folder. This needs to be set so the script knows where to find the videos.

# TheTechGame.com Website Settings and Paths.
ttg_username = \"$ttg_username\" # The username of your account on TheTechGame.com. This needs to be set to allow video uploading,
ttg_password = \"$ttg_password\" # The password of your account on TheTechGame.com. This needs to be set to allow video uploading,
ttg_base_url = \"https://thetechgame.com/\" # DO NOT EDIT!
ttg_login_url = \"Account.html\" # DO NOT EDIT!
ttg_upload_url = \"Videos/submit.html\" # DO NOT EDIT!
ttg_already_loggedin = False # Set this to True if you are using your own browser user profile after the first time logging into TheTechGame.com using the script with that profile.
ttg_html_login_username_field_id = \"username\" # The username input field id on TheTechGame.com. Your account username DOESN'T go here. DO NOT EDIT!
ttg_html_login_password_field_id = \"password\" # The password input field id on on TheTechGame.com. Your account password DOESN'T go here. DO NOT EDIT!
ttg_html_video_title_field_id = \"title\" # The video title input field id on TheTechGame.com submit video page. DO NOT EDIT!
ttg_html_video_desc_field_id = \"description\" # The video description input field id on TheTechGame.com submit video page. DO NOT EDIT!
ttg_html_video_upload_filed_id = \"url\" # The video upload input field id on TheTechGame.com submit video page. DO NOT EDIT!
ttg_html_video_cat_field_id = \"cid\" # The video category input field id on TheTechGame.com submit video page. DO NOT EDIT!
'''
TheTechGame.com Video Categories:
 1 = Funny Videos
 2 = Game Clips
 3 = Game Montages
 4 = Game Trailers
 5 = Game Play
 6 = General Videos
 7 = Glitches and Tricks
 8 = Interviews and Shows
 9 = Modding
 10 = Walkthroughs and Guides
'''
ttg_html_video_cat_number = 2 # The number starting from 1 for that category you want to select. #2 selects "Game Clips" on TheTechGame.com. You can edit this option if needed.
ttg_video_uploading_total = 10 # How much videos will be submitted. You can edit this option if needed.
" > config.py

  echo ""
  echo "Thank you! Finishing up. You can edit additional settings in the config.py file."
	echo ""
	echo "Credit goes to Shuga (https://github.com/Shugabuga) for the setup.sh file."
  echo "TheTechGame Video Uploader was successfully setup! Remember you can edit theses options at anytime in config.py."
  echo ""
	touch .is_setup
else
	echo "TheTechGame Video Uploader has already been set up. Aborting..."
fi
