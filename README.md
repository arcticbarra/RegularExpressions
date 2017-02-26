# Phone and Email Extractor

Small python program that extracts emails and phones from your clipboard text using regular expressions and then copies them back. Made using python 3.

## Installation
Clone this repo and then install pyperclip using `pip3 install pyperclip`

## Usage
Copy some text and then run `pyton3 phoneAndEmail.py`. Then the phones and emails will be formated like so.

Example:
Copy all text from https://www.nostarch.com/contactus.htm with `cmd+a cmd+c` and then run the program, your clipboard will now be:
```
800-420-7240
415-863-9900
415-863-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
info@nostarch.com
```
