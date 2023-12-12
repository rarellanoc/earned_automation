#! /bin/bash
export MAGICK_HOME="$HOME/Downloads"
export PATH="$MAGICK_HOME/bin:$PATH"
export DYLD_LIBRARY_PATH="$MAGICK_HOME/lib/"
i=1
while IFS=";" read -r stop enroll aspire action
do
  new=$(printf "_%03d_" "$i")
  echo "$new"
  echo -n "$stop" | magick -gravity center -background '#fff8eb' -fill black -size 430x300 -font /System/Library/Fonts/HelveticaNeue.ttc  caption:@- -background '#fff8eb' -extent 1280x1280  -set filename:mysize "$new" 'post_%[filename:mysize]_1.png'
  echo -n "$enroll" | magick -gravity center -background '#fff8eb' -fill black -size 400x300 -font /System/Library/Fonts/HelveticaNeue.ttc  caption:@- -background '#fff8eb' -extent 1280x1280  -set filename:mysize "$new" 'post_%[filename:mysize]_2.png'
  echo -n "$aspire" | magick -gravity center -background '#fff8eb' -fill black -size 400x300 -font /System/Library/Fonts/HelveticaNeue.ttc  caption:@- -background '#fff8eb' -extent 1280x1280  -set filename:mysize "$new" 'post_%[filename:mysize]_3.png'
  echo -n "$action" | magick -gravity center -background '#fff8eb' -fill black -size 400x300 -font /System/Library/Fonts/HelveticaNeue.ttc  caption:@- -background '#fff8eb' -extent 1280x1280  -set filename:mysize "$new" 'post_%[filename:mysize]_4.png'
  let i=i+1
done < <(tail -n +1 sample2.csv)

