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




