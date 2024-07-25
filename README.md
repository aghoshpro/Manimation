# Manim Community

<p align="center">
    <a href="https://github.com/3b1b/manim">
        <img src="https://raw.githubusercontent.com/3b1b/manim/master/logo/cropped.png">
    </a>
</p>

[![pypi version](https://img.shields.io/pypi/v/manimgl?logo=pypi)](https://pypi.org/project/manimgl/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)
[![Manim Subreddit](https://img.shields.io/reddit/subreddit-subscribers/manim.svg?color=ff4301&label=reddit&logo=reddit)](https://www.reddit.com/r/manim/)
[![Manim Discord](https://img.shields.io/discord/581738731934056449.svg?label=discord&logo=discord)](https://discord.com/invite/bYCyhM9Kz2)
[![docs](https://github.com/3b1b/manim/workflows/docs/badge.svg)](https://3b1b.github.io/manim/)

Manim is an engine for precise programmatic animations, designed for creating explanatory math videos. **Note**, there are **many versions** of manim are available. Check [this page](https://docs.manim.community/en/stable/faq/installation.html#different-versions) for more details.

We are using [Manime Community Edition](https://github.com/ManimCommunity/manim/) developed in 2020 by a group of developers forked it from the [original work](https://github.com/3b1b/videos) by [3Blue1Brown](https://www.3blue1brown.com/), with a goal of being more stable, better tested, quicker to respond to community contributions, and all around friendlier to get started.

## Installation

> We will follow the instructions to install [ManimCommunity](https://docs.manim.community/en/stable/installation.html)

OR

> Follow the experience

<!-- Manim runs on Python 3.7 or higher.

System requirements are [FFmpeg](https://ffmpeg.org/), [OpenGL](https://www.opengl.org/) and [LaTeX](https://www.latex-project.org) (optional, if you want to use LaTeX).
For Linux, [Pango](https://pango.gnome.org) along with its development headers are required. See instruction [here](https://github.com/ManimCommunity/ManimPango#building). -->

# My Hands-On Experience on Windows

<!-- <html><div style="background-color:green;"><strong>&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Working Example</strong></div></html> -->

### Prerequisites

### 0. Install `Chocolatey`

- Open **cmd** or **terminal** and type `choco` to check if you have it already.
- Else go to https://chocolatey.org/install#individual to install it

### 1. Install `manimce`

To install Manim ([link](https://community.chocolatey.org/packages/manimce#install)), run the following command from the **cmd** or **powershell**

```
choco install manimce
```

That’s it, no further steps required. You can continue with installing the optional dependencies below.

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

### 2. Install a LaTeX distribution

- For Windows, the recommended LaTeX distribution is [MiKTeX](https://miktex.org/download).

```
choco install miktex.install
```

If you are concerned about disk space, there is an alternative, smaller distributions of LaTe which is a dedicated package for Manim based on TinyTeX which contains all the required packages that Manim interacts with.

```
choco install manim-latex
```

## Working with Manim

RUN an example as mentioned in `example_scenes.py`. This should pop up a window playing a simple scene.

```sh
manimgl example_scenes.py OpeningManimExample
```

7. To save the videos as `.mp4` files in local directory please set the `out_dir` at **line86** in the `scene_file_writer.py` as follows,

   ```sh
   out_dir = self.output_directory or "./output/"
   ```

   Then run the follwing

   ```sh
   manimgl example_scenes.py OpeningManimExample -o
   ```

<!-- ### More useful -tags

- `-w` to write the scene to a file
- `-o` to write the scene to a file and open the result
- `-s` to skip to the end and just show the final frame.
  - `-so` will save the final frame to an image and show it
- `-n <number>` to skip ahead to the `n`'th animation of a scene.
- `-f` to make the playback window fullscreen

Take a look at custom_config.yml for further configuration. To add your customization, you can either edit this file, or add another file by the same name "custom_config.yml" to whatever directory you are running manim from.

For example [this is the one](https://github.com/3b1b/videos/blob/master/custom_config.yml) for 3blue1brown videos. There you can specify where videos should be output to, where manim should look for image files and sounds you want to read in, and other defaults regarding style and video quality.

Look through the [example scenes](https://3b1b.github.io/manim/getting_started/example_scenes.html) to get a sense of how it is used, and feel free to look through the code behind [3blue1brown videos](https://github.com/3b1b/videos) for a much larger set of example.

**Note**, however, that developments are often made to the library without considering backwards compatibility with those old videos. To run an old project with a guarantee that it will work, you will have to go back to the commit which completed that project. -->

## Building Blocks Examples

### 1. Circle

<img src="./output/CreateCircle.mp4"/>

### 1. Polygons

<img src="./output/SquareToCircle.mp4_20240725_222131.gif"/>

### 2. Graphs on numberline

https://github.com/user-attachments/assets/4387782c-9c7b-491f-983f-c8f7f55138fd

## Ideas

### Idea 02 - Simple Area Under Curve

### Idea 01 - Mandelbrot Fractals Pattern

## Documentation

Documentation is in progress at [3b1b.github.io/manim](https://3b1b.github.io/manim/). And there is also a Chinese version maintained by [**@manim-kindergarten**](https://manim.org.cn): [docs.manim.org.cn](https://docs.manim.org.cn/) (in Chinese).

[manim-kindergarten](https://github.com/manim-kindergarten/) wrote and collected some useful extra classes and some codes of videos in [manim_sandbox repo](https://github.com/manim-kindergarten/manim_sandbox).

## Contributing

Is always welcome. As mentioned above, the [community edition](https://github.com/ManimCommunity/manim) has the most active ecosystem for contributions, with testing and continuous integration, but pull requests are welcome here too. Please explain the motivation for a given change and examples of its effect.

## License

This project falls under the MIT license.

```

```
