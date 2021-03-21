#!/bin/bash

##### Init
me="SlabSlebBuilder >"
echo "$me Start building !"
echo "$me into"
projectRoot="../.." # Up 2 times : resources/scripts
cd $projectRoot
pwd

##### Version build
version=$(date '+%Y%m%d%H%M')
version="$1-$version"

echo 
echo "$me Version to build '$version'"

##### Edit README
mainReadmeFile=$projectRoot
echo
echo "$me Inject the version into README file"
sed -E -i "s/(<span id=\"textVerson\">)(.*)(<\/span>)/\1$version\3/" ./README.md
echo ">>>README HEAD"
head -n10 ./README.md
echo "<<<README HEAD"

##### Cleaning
echo
echo "$me Removing useless file"
echo "  (Like FreeCad backup file '*.FCStd99')"
echo
find ../ -regex '.*\.FCStd[0-9]+' -print #-delete

##### End
echo
echo "$me Done!"