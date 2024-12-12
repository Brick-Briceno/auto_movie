from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip, ImageClip
from moviepy.config import change_settings
from templates import templates
import os

#pip install moviepy

#if it is not installed, please install it
#https://imagemagick.org/script/download.php#windows
change_settings({"IMAGEMAGICK_BINARY": "C:\\Program Files\\ImageMagick-7.1.1-Q8\\magick.exe"})

class Video_n_Text:
    "Configure ✔"
    path_in = "videos"
    path_out = "result"
    #maximum characters to display on one line
    max_characters = 20

    def fit_text(text, max_length):
        words = text.split(" ")
        line = ""
        result = ""
        for word in words:
            if len(line) + len(word) + 1 <= max_length:
                line += word + " "
            else:
                result += line.strip() + "\n"
                line = word + " "
        result += line.strip()
        return result

    def template_to_obj(text, template_number, set_duration, letter_size):
        tn = templates[template_number]
        #if not tn["stroke_width"]: tn["stroke_width"] = None
        return TextClip(
            Video_n_Text.fit_text(text,
                max_length=Video_n_Text.max_characters),
            #parameters for text
            fontsize=tn["fontsize"]*letter_size, color=tn["color"],
            interline=tn["interline"], bg_color=tn["bg_color"],
            font=tn["font"], transparent=tn["transparent"],
            stroke_width=tn["stroke_width"]*letter_size,
            kerning=tn["kerning"], align=tn["align"],
            stroke_color=tn["stroke_color"],
                ).set_position(
                    lambda t: (
                        'center', 50+t)
                        ).set_duration(set_duration)

    def create_videos(text="This is an example text :D", template_number=0):
        #create necessary folders if they do not exist
        for path in (Video_n_Text.path_in, Video_n_Text.path_out):
            if not os.path.isdir(path):
                os.mkdir(path)
        for video in os.listdir(Video_n_Text.path_in):
            clip = VideoFileClip(f"{Video_n_Text.path_in}\\{video}")
            #take the minimum resolution between height and width
            resolution = min(clip.size)
            letter_size = resolution * 1/720
            #create composition
            pre_composition = [clip]
            #pre_composition.append(
            #    Video_n_Text.template_to_obj(
            #        text, template_number, clip.duration, letter_size))
            image = ImageClip("subs.png")
            pre_composition.append(image)
            composition = CompositeVideoClip(pre_composition, size=(resolution, resolution))
            composition.duration = clip.duration
            #export
            composition.write_videofile(f"{Video_n_Text.path_out}\\Edited {video}", clip.fps)


#define the template text and number
text = "Hi, how are you! ✨"
Video_n_Text.create_videos(text=text, template_number=2)
