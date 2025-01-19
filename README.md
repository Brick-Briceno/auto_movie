# Auto Movie

This is a software that provides an interface that adapts to each resolution by adapting it in a 1:1 ratio

It has line wrapping so that the words do not go off the screen

To create new templates, just access `templates.py` and add all the ones you want
The parameters to be modified are explained below.

## Tutorial

### Install moviepy and Pillow:
go to cmd or preferably powershell and type

```bash
pip install moviepy
pip install pillow
```

If you get any error update pip with
```bash
pip install --upgrade pip
```

And download Visual C++ Build Tools https://visualstudio.microsoft.com/downloads/?q=build+tools

![select these options](https://i.sstatic.net/h3mTO.png)

### how to use it?
just access the `example.py` file and put the text and the template number with which you want to convert the videos

```python
from auto_movie import Video_n_Text

#define the template text and number
text = "Hi, how are you! ✨"
Video_n_Text.create_videos(text=text, template_number=5)
```

If the process of rendering the video to see the result is slow for you, there is the option of generating the result in a png.

```python
from subs import make_text

img = make_text(text=text, font="fonts/proxima-nova-7.ttf", stroke_width=3.5, bg_mode="square",
          stroke_color="#154F3B", color="#42F5E2", background="#ceccca")
img.save("subs.png")
```

#### Explanation of parameters
text: Here is the text
font: file path, supports ttf and otf format
stroke_width: font border size
stroke_color: border color
color: text color
background: background color
bg_mode: background mode can be "rounded" or "square", If it is none it will have no background

A new feature allows you to set hexadecimal colors instead of complicated tuples as was previously the case, allowing for faster template development

but...

### how to create templates?

You can edit or add more templates in the `templates.py` file, just modify the metadata in the dictionary (template) you want

```python
templates = [
    # example template
    {"font":"fonts/proxima-nova-7.ttf", "color":"#fff",
            "stroke_width": 3.5, "stroke_color": "#000",
                "background": False, "bg_mode": None},
]
```

### How to configure where videos are saved or collected?

In the `auto_movie.py` file you can make some settings like the maximum length of text in one line

```python
class Video_n_Text:
    "Configure ✔"
    path_in = "videos"
    path_out = "result"
    #maximum characters to display on one line
    max_characters = 20
```

The files will be saved in the output folder
if the folder does not exist it will be created
