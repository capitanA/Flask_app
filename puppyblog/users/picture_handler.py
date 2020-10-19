from flask import current_app
from puppyblog.models import User
from PIL import Image
import os


def save_profile_pic(uploaded_pic, username):
    file_name = uploaded_pic.filename

    pic_ext = file_name.split(".")[-1]
    profile_pic_name = username + "." + pic_ext
    storage_pic_path = os.path.join(current_app.root_path, "static/profile_pics", profile_pic_name)
    pic_size = (200, 200)
    pic = Image.open(uploaded_pic)
    pic.thumbnail(pic_size)
    pic.save(storage_pic_path)
    return profile_pic_name
