# QCards 

QCards is a very simple Python script that will generate QSL cards in bulk. At the moment, QCards accepts a CSV file and will generate the QSL cards for you.

QCards is configurable via a simple configuration file. Customize QCards by setting the following customizable items:

* BACKGROUND_IMAGE - your background image template. It can be JPEG or PNG or whatever.
* BIG_FONT - the font that will be used to render the callsign.
* BIG_FONT_SIZE - the size of the callsign font in pixels.
* BIG_FONT_COLOR - the font color (eg. #ffffff).
* SMALL_FONT - the font that will be used to render the extra details text about the QSO.
* SMALL_FONT_SIZE - the size of the details font in pixels.
* SMALL_FONT_COLOR - the font color for the details text.

### License
 This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at https://mozilla.org/MPL/2.0/.

## Installation

To install QCards, you can clone this Git repository or download the artifacts.
`git clone https://github.com/hardwyrd/qcards.git`

# Running QCards

## Requirements

Since QCards is a Python script, it is much better to provide QCards with a virtual environment. I personally just use Python 3's own virtual env module (venv). You can feel free to use whatever method you prefer, be it pyenv, pipenv, conda, and others. It's all perfectly fine ^_^. 

Go ahead and create the virtual environment and activate:

```
python3 -m venv qcards_env
source qcards_env/bin/activate
```

Install the required Python modules via the requirements.txt file:

`pip install -r requirements.txt`

## Configuration

The repository includes a sample config.sample file. Feel free to copy config.sample to config.ini and modify and update config.ini as you see fit.

The QCards repository DOES NOT INCLUDE fonts that you can use to generate your QSL cards. However, you can feel free to download free and open source TrueType fonts anywhere on the web. Make sure to set in your config.ini the path of the fonts that QCards will use. Ideally, you can put the font files within the QCards directory/folder.

## Template Image

To make things way simpler, QCards uses an image template which will serve as your background image for the generated QSL cards. QCards will only insert the callsign, and the call details. All other elements that you would like to include in your QSL card design like the logos, background colors, extra background images and other design elements will need to be modified by you using your favorite image editor and prepare prior. 

By default, QCards expects that your background image/template is 1280 pixels wide, and 720 pixels high. If you are going to use images with different dimensions, make sure to update config.ini under the [DEFAULT] section and modify the following:

```
[DEFAULT]
CARD_W=1280
CARD_H=720
```

## CSV Data

QCards accepts data from CSV with the following format:

`Callsign, Handle, Date & Time, Mode, RST`

Example:

```
4g9lbz,Romar,06/19/2024 20:00:00 Asia/Manila,ASL,5/9
```

The included sample netcall_logs.csv.sample follows this format. Feel free to copy or rename netcall_logs.csv.sample to netcall_logs.csv and update with your own data.

## Syntax

To generate QSL cards using the default configuration, run

`./qcards.py`

To generate QSL cards using a custom configuration, run 

`./qcards.py -c <your config file>`

To generate QSL cards from a custom CSV file, run

`./qcards.py -f <your CSV file>`

To generate QSL cards from a custom configuration and custom CSV file, run

`./qcards.py -c <your config file> -f <your CSV file>`

### Support
If you like this little tool, you can buy me coffee ^_^ and thank you for your support. 
https://buymeacoffee.com/ninerlbz
