# pip install instaloader

# to download the profile picture from instagram using username

import instaloader

ig=instaloader.Instaloader()
dp=input("Enter Insta Username :")

ig.download_profile(dp,profile_pic_only=True)

