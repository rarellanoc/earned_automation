# earned_automation
Make yourself replaceable way of thinking


## Instagram script:

This replaces a tab delimited csv into a semicolon delimited csv, and then into simple text based images using Magick (requires a version of imagemagick). 

requires readcsv.sh


```shell
mv sample_100.csv sample.csv
sed 's/    /;/g'  sample.csv > sample2.csv
./readcsv.sh
```



## Mail preview

This is a simple html page previewer in horizontal mode. Instead of printing A4 pages, you can then have an overview of letters or mail sequences. 

requires convert_indoc.py or convert_nurture.py

```
cp Documents/01.txt data_nurture/01.txt 
python convert_nurture.py > data_nurture.js
python -m SimpleHTTPServer
```

to view:

```
customer_journey_nurture.html
```
or
```
localhost:8000
```



## Blog

To trigger the rendering on the pelican (python) blog, based on .md files. 
More info on Pelican documentation. 

```
pelican blog/content -o blog/output -s pelicanconf.py -e SITENAME=‘”The title - the blog“’ 
git add files
git commit -m ‘message’
git push origin master
```

## Dissemination calendar

A python file to print a calendar (made from scratch, warning) and some repetition event (like a social media schedule). Works for this year, or you have to change the first day of the year weekday (currently: 7). 

I have another that handles multiple events, but it's too tailored and patchy for now. 

You can call it by the flags like this: 

-d or --day (the day you start tracking the repetition)
-m or --month (the month of that day)
-r or --repeat (in days)

```shell
python dissemination_repeat.py -d 12 -m 7 -r 30 --csv=1 > output.csv
```

csv 1 or 0 changes between commas and tabs. 

