## Journal
#### What is it?
TBD
#### Dependencies
* Python 2.7
* peewee
* pillow
* icalendar
* ExifRead
* lxml

#### Data Preparation
Create a `data` folder in `journal/`

###### `Facebook`
  1. Download personal Facebook data
  (Detailed instructions can be found on Facebook Help Center [_here_](https://www.facebook.com/help/1701730696756992?helpref=hc_global_nav))
  2. Unzip downloaded `facebook-<username>.zip` to `data` and rename unzipped folder to `facebook`

###### `Google`
  1. Download personal Google data archive with the following:
  (Detailed instructions can be found on Google Account Help [_here_](https://support.google.com/accounts/answer/3024190?hl=en)):
      1. Calendar
      2. Location History
      3. Map (your places)
  2. Unzip downloaded archive to `data` and rename unzipped folder to `google`

###### `Twitter`
  1. TBD
  2. TBD
  3. TBD

###### `Steam`
  1. Create a `steam` subfolder in `/data`
  2. In steam, click on your wallet amount, then click on "View licenses and product key activations".
  3. Save this page as an html document to `/data/steam`.


#### Run
* `python2.7 import_all.py`
* `python2.7 main.py`

#### Contribution
TBD

#### License
[MIT](/LICENSE)
