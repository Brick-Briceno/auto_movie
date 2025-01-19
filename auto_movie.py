from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip
from templates import templates
import numpy as np
import subs
import os

#pip install moviepy
#pip install pillow

class Video_n_Text:
    "Configure ✔"
    path_in = "videos"
    path_out = "result"
    #maximum characters to display on one line
    max_characters = 20

    def template_to_obj(text, template_number, set_duration, video_resolution):
        template = templates[template_number]
        img = subs.make_text(text,
            font=template["font"],
            color=template["color"],
            stroke_width=template["stroke_width"],
            stroke_color=template["stroke_color"],
            background=template["background"],
            bg_mode=template["bg_mode"])
        center = (video_resolution-img.size[0])//2 #math for center text
        x, y = img.size
        base = video_resolution/x
        base *= .6
        img.resize((int(x*base), int(y*base)))
        img_array = np.array(img)
        return ImageClip(img_array, duration=set_duration).set_position((center-20, 50))
        #20 px since sometimes there're talicas and 20px are added

    def create_videos(text="This is an example text :D", template_number=0):
        for video in os.listdir(Video_n_Text.path_in):
            clip = VideoFileClip(f"{Video_n_Text.path_in}\\{video}")
            #take the minimum resolution between height and width
            resolution = min(clip.size)
            letter_size = resolution * 1/720
            #create composition
            try: pre_composition = [clip, Video_n_Text.template_to_obj(
                    text, template_number, clip.duration, resolution)]
            except IndexError:
                raise IndexError(f"This template does not exist, there are only {len(templates)} templates")
            composition = CompositeVideoClip(pre_composition, size=(resolution, resolution))
            composition.duration = clip.duration #clip.duration
            #export
            composition.write_videofile(f"{Video_n_Text.path_out}\\Edited {video}", clip.fps)

#create necessary folders if they do not exist
for path in (Video_n_Text.path_in, Video_n_Text.path_out):
    if not os.path.isdir(path): os.mkdir(path)
