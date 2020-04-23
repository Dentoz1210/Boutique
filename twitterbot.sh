#! /bin/bash
#Please do not change anything in this section!

sleep 15s
cd output
rm news.png
rm shop.png
sleep 15s

#Change the "background" image URL to something different.
curl "https://user-images.githubusercontent.com/64136458/80143172-b40f6b80-85ac-11ea-9b71-bdba3ed25a80.jpg" --output shop.png

#Please do not change anything in this section!
cd ..
python app.py
sleep 20s
cd output

#Change the "background" image URL to something different.
curl "https://user-images.githubusercontent.com/64136458/80138673-70fdca00-85a5-11ea-8cd4-7f46c3260777.jpg" --output news.png

#Please do not change anything in this section!
cd ..
python news.py
exit
