#!/usr/bin/env python3
#
# QCards
# hardwyrd.at.gmail.dot.com

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from PIL import Image, ImageDraw, ImageFont
from configparser import ConfigParser
import click
import csv

# Fetch recent version
with open('version.txt', 'r') as version_file:
    version_lines = version_file.readlines()
    for version in version_lines:
        version_num = version

@click.command()
@click.version_option(version_num, prog_name="QCards")
@click.option('-c', '--configuration_file', help='Custom config file')
@click.option('-f', '--csv_file', help='CSV file')
def generate_card(configuration_file, csv_file):

    config = ConfigParser()

    # Parse config
    if configuration_file:
        config.read(configuration_file)
    else:
        config.read('config.ini')
    
    # Load CSV file
    if csv_file:
        call_logs = csv_file
    else:
        call_logs = config['DEFAULT']['CSV_FILE']

    with open(call_logs, newline='') as netcall:
        callers = csv.reader(netcall, delimiter=',')

        for caller in callers:
            # We run everything under the for loop kay para ma-instantiate ug bag-o 
            # nga Image/ImageDraw kay if dili fresh instantiation, magsapaw-sapaw ang 
            # injected texts once mag-call na ug Image.save() later.

            # Default card dimensions
            # We pick up the card dimensions from config.ini 
            W, H = (config['DEFAULT']['CARD_W'],config['DEFAULT']['CARD_H'])

            # Default font position height coords (in pixels)
            # Gi-set ni sila statically dinhi kay dili man ga-change ang height
            # sa injected texts. We only need to make sure nga naka-center ang 
            # texts later.
            cs_h = 276
            de_h = 520

            # Load settings into variables
            # Ako lang ni gi-ingon ani kay para dili kaayo taas ang i-reference 
            # nga variables. Kapoy type! ^_^
            background_image = config['SETTINGS']['BACKGROUND_IMAGE']
            cs_fontface = config['SETTINGS']['BIG_FONT']
            cs_fontsize = config['SETTINGS']['BIG_FONT_SIZE']
            cs_fontcolor = config['SETTINGS']['BIG_FONT_COLOR']
            de_fontface = config['SETTINGS']['SMALL_FONT']
            de_fontsize = config['SETTINGS']['SMALL_FONT_SIZE']
            de_fontcolor = config['SETTINGS']['SMALL_FONT_COLOR']

            # Load the QSL card template image
            # Mao pud ni nga object atong ipa-save later.
            qcard_bg = Image.open(background_image)

            # Initialize the draw method
            qcard = ImageDraw.Draw(qcard_bg)

            # Set up CS fontface and size
            cs_font = ImageFont.truetype(cs_fontface, int(cs_fontsize))

            # Set up details fontface and size
            de_font = ImageFont.truetype(de_fontface, int(de_fontsize))

            # Construct the fields
            # Ako ra ni gi-humanize para dali ma-ilhan kay kapoy
            # mag-psycho sa list items ug list item id :D
            # Technically, gi-slice ra nato ang list item. Naay lain way nga
            # maka-wow pero the simpler the better.
            cs = caller[0]
            handle = caller[1]
            datetime = caller[2]
            mode = caller[3]
            rst = caller[4]

            # Prep the qsl card details format
            details = f'Name: {handle} | Date/Time: {datetime} | Mode: {mode} | RST: {rst}'

            # Get the text length so we can properly center the text
            cs_w = qcard.textlength(cs.upper(), font=cs_font)
            de_w = qcard.textlength(details, font=de_font)

            # Inject the texts and generate the qsl card image
            print(f'Generating QSL card for {cs.upper()} ...')

            # Things to note lang. We need to make sure to cast the numbers to int()
            # para dili mabuang sa calculation.
            # Where: qcard.text((X coordinate, Y coordinate), text, font, fontcolor)
            qcard.text(((int(W) - int(cs_w))/2, cs_h), cs.upper(), font=cs_font, fill=cs_fontcolor)
            qcard.text(((int(W) - int(de_w))/2, de_h), details, font=de_font, fill=cs_fontcolor)
            qcard_filename = f"{cs}.png"
            qcard_bg.save(qcard_filename)

if __name__ == '__main__':
    generate_card()