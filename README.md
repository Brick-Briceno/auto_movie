#Auto Movie

This is a software that provides an interface that adapts to each resolution by adapting it in a 1:1 ratio

It has line wrapping so that the words do not go off the screen

To create new templates, just access templates.py and add all the ones you want

Tutorial

Install moviepy: go to cmd or preferably powershell and type "pip install moviepy"

Download Imagemagick
https://imagemagick.org/script/download.php#windows

If you get any error update pip with "pip install --upgrade pip"

And download Visual C++ Build Tools https://visualstudio.microsoft.com/downloads/?q=build+tools

![select these options](https://i.sstatic.net/h3mTO.png)


change_settings({"IMAGEMAGICK_BINARY": "C:\\Program Files\\ImageMagick-7.1.1-Q8\\magick.exe"})

Video_n_Text.create_videos(text=text, template_number=0)

put the path of ImageMagick in the file "auto_movie.py"
´´´
change_settings({"IMAGEMAGICK_BINARY": "C:\\Program Files\\ImageMagick-7.1.1-Q8\\magick.exe"})
´´´
put the text and the template number with which you want to convert the videos

´´´
Video_n_Text.create_videos(text=text, template_number=0)
´´´

You can edit or add more templates in the "templates.py" file, just modify the metadata in the dictionary (template) you want

The files will be saved in the output folder, if the folder does not exist it will be created
