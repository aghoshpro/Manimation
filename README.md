<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./output/Gif-filename_Black.gif">
  <source media="(prefers-color-scheme: light)" srcset="./output/Gif-filename_White.gif">
  <img alt=OntoRaster Logo" src="./output/Gif-filename_White.gif" style="width:auto;">
</picture>

<!-- <p align="center">
    <a href="https://github.com/3b1b/manim">
        <img src="https://raw.githubusercontent.com/3b1b/manim/master/logo/cropped.png">
    </a>
</p> -->

[![pypi version](https://img.shields.io/pypi/v/manimgl?logo=pypi)](https://pypi.org/project/manimgl/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)
[![Manim Discord](https://img.shields.io/discord/581738731934056449.svg?label=discord&logo=discord)](https://discord.com/invite/bYCyhM9Kz2)
[![docs](https://github.com/3b1b/manim/workflows/docs/badge.svg)](https://3b1b.github.io/manim/)

Manim is an engine for precise programmatic animations, designed for creating explanatory math videos. **Note**, there are **many versions** of manim are available. Check [this page](https://docs.manim.community/en/stable/faq/installation.html#different-versions) for more details.

We use [Manim Community Edition](https://github.com/ManimCommunity/manim/), forked from [original work](https://github.com/3b1b/videos) by [3Blue1Brown](https://www.3blue1brown.com/), in 2020 by a group of developers to make it more reliable, better tested, faster to respond to community additions, and easier to start. It's well-maintained and documented.

## Official Installations

One can follow the instructions to install [ManimCommunity](https://docs.manim.community/en/stable/installation.html) for any Os. You can also follow the step-by-step win-installation that worked for me.

<!-- Manim runs on Python 3.7 or higher.

System requirements are [FFmpeg](https://ffmpeg.org/), [OpenGL](https://www.opengl.org/) and [LaTeX](https://www.latex-project.org) (optional, if you want to use LaTeX).
For Linux, [Pango](https://pango.gnome.org) along with its development headers are required. See instruction [here](https://github.com/ManimCommunity/ManimPango#building). -->

### For Windows

<!-- <html><div style="background-color:green;"><strong>&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Working Example</strong></div></html> -->

### 0. Check and Install `Chocolatey`

- Open **cmd** or **terminal** with _administrative privilege_ and type `choco` to check if you have it already.
- Else go to https://chocolatey.org/install#individual to install it

### 1. Install `manimce`

To install Manim Community Edition ([link](https://community.chocolatey.org/packages/manimce#install)),
run the following command from the **cmd** or **powershell** with _administrative privilege_

```
choco install manimce
```

That’s it, no further steps are required. You should get something like below.

```
The install of manimce was successful.
Software install location not explicitly set, could be in package or
default install location if installer.

Chocolatey installed 5/5 packages.
See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).

Installed:
- manimce v0.18.1
- python v3.11.9
- python3 v3.11.9
- ffmpeg v7.0.1
- python311 v3.11.9

PS C:\Windows\system32>
```

## 2. Install a LaTeX distribution

- For Windows, the recommended LaTeX distribution is [MiKTeX](https://miktex.org/download) to enable LaTeX in the manim videos.

```sh
choco install miktex.install
```

## 3. Start Working with Manim

- Open `terminal` or `cmd` and clone this repo

  ```
  git clone https://github.com/aghoshpro/Manimation.git
  ```

- Initially one has to create `scene.py` file which will contain the animations as classes. Here `scene.py` is created in the repo and now let's create a class named `CreateCircle` which will draw a circle.

  ```sh
  from manim import *

  class CreateCircle(Scene):
      def construct(self):
          circle = Circle()  # create a circle
          circle.set_fill(PINK, opacity=0.5)  # set color and opacity
          self.play(Create(circle))  # show the circle on screen
  ```

- Save the code in scene.py. Then, run it with the following command,

  ```
  manim -pqk scene.py CreateCircle
  ```

  To see more options please check [Manim Community Edition](https://github.com/ManimCommunity/manim/?tab=readme-ov-file#command-line-arguments)

* **Output**

  <img src="./output/CreateCircle_ManimCE_v0.18.1.gif" width=500/>

* To check the structure and options of `manim` run the following,

  ```sh
   manim render --help
  ```

## 4. Saving

### Save the files in the local directory with desired `./path/output`

<!-- - To save the videos in the local directory please set the `out_dir` at **line86** in the `scene_file_writer.py` as follows, -->

### as `.gif` files

```sh
manim -pqh scene.py SquareAndCircle -o Z:/Git_PhD/Manimation/output/filename01 --format gif
```

### as `.mp4` files

```sh
manim -pqh scene.py SquareAndCircle -o Z:/Git_PhD/Manimation/output/filename02 --format mp4
```

### as `mp4` with `.png` (-s)

```
manim -pqh scene.py SquareAndCircle -s -o Z:/Git_PhD/Manimation/output/filename03 --format mp4
```

<!-- - To save the videos as `.mp4` files in local directory please set the `out_dir` at **line86** in the `scene_file_writer.py` as follows, -->

<!-- ```sh
out_dir = self.output_directory or "./output/"
```

Then run the following

```sh
manimgl example_scenes.py OpeningManimExample -o
``` -->

<!-- ### More useful -tags

- `-w` to write the scene to a file
- `-o` to write the scene to a file and open the result
- `-s` to skip to the end and just show the final frame.
  - `-so` will save the final frame to an image and show it
- `-n <number>` to skip ahead to the `n`'th animation of a scene.
- `-f` to make the playback window fullscreen

Take a look at custom_config.yml for further configuration. To add your customization, you can either edit this file or add another file by the same name "custom_config.yml" to whatever directory you are running manim from.

For example [this is the one](https://github.com/3b1b/videos/blob/master/custom_config.yml) for 3blue1brown videos. There you can specify where videos should be output to, where manim should look for image files and sounds you want to read in, and other defaults regarding style and video quality.

Look through the [example scenes](https://3b1b.github.io/manim/getting_started/example_scenes.html) to get a sense of how it is used, and feel free to look through the code behind [3blue1brown videos](https://github.com/3b1b/videos) for a much larger set of example.

**Note**, however, that developments are often made to the library without considering backwards compatibility with those old videos. To run an old project with a guarantee that it will work, you will have to go back to the commit which completed that project. -->

## 4. Basic Examples

More examples are can be found ([here](https://docs.manim.community/en/stable/examples.html))

### Equations ([Docs](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html))

<center><img src="./output/Equation_ManimCE_v0.18.0.gif" width=500/></center>

### Polygon Transformation

<center><img src="./output/SquareToCircle_ManimCE_v0.18.1.gif" width=500/></center>

### Writing Text ([Docs](https://docs.manim.community/en/stable/reference/manim.animation.creation.html))

<center><img src="./output/Gif-Text.gif" width=500/></center>

### Graphs ([Docs](https://docs.manim.community/en/stable/reference/manim.mobject.graph.html))

<center><img src="./output/Gif-filename-Graph.gif" width=500/></center>

### Numberline

https://github.com/user-attachments/assets/4387782c-9c7b-491f-983f-c8f7f55138fd

## Ideas

### Idea 01 - Solar System

 <center> <img src="./Ideas/SolarSystem.gif" width=500/> 
 </center>

### Idea 02 - Mandelbrot Fractals Pattern

## Documentation

Documentation is in progress at [Docs](https://docs.manim.community/en/stable/)

<!-- Documentation is in progress at [3b1b.github.io/manim](https://3b1b.github.io/manim/). And there is also a Chinese version maintained by [**@manim-kindergarten**](https://manim.org.cn): [docs.manim.org.cn](https://docs.manim.org.cn/) (in Chinese).

[manim-kindergarten](https://github.com/manim-kindergarten/) wrote and collected some useful extra classes and some codes of videos in [manim_sandbox repo](https://github.com/manim-kindergarten/manim_sandbox). -->

## Contributing

Is always welcome. As mentioned above, the [community edition](https://github.com/ManimCommunity/manim) has the most active ecosystem for contributions, with testing and continuous integration, but pull requests are welcome here too. Please explain the motivation for a given change and examples of its effect.

## License

This project falls under the MIT license.
