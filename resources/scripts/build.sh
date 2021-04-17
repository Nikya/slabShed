#!/bin/bash

##### Init
echo ; echo "#########################"
me="SlabShebBuilder >"
echo "$me Start building !"
echo "$me into folder:"
projectRoot="../.." # Up 2 times : resources/scripts
cd $projectRoot
pwd

##### Version build
version=$(date '+%Y%m%d%H%M')
version="$1-$version"

echo "$me Version to build '$version'"

##### Continue?

read -p "Are you sure you wish to continue? (y/n) : "
if [ "$REPLY" != "y" ]; then
   exit
fi

##### Edit README
echo ; echo "#########################"
mainReadmeFile=$projectRoot
echo "$me Inject the version into README file"
sed -E -i "s/(<span id=\"textVerson\">)(.*)(<\/span>)/\1$version\3/" ./README.md
echo
echo ">>>README HEAD"
head -n8 ./README.md
echo "<<<README HEAD"

##### Cleaning
echo ; echo "#########################"
echo "$me Removing useless file (like FreeCad backup file '*.FCStd99')"
echo
find ./ -regex '.*\.FCStd[0-9]+' -print -delete

##### Git tag preparing
echo ; echo "#########################"
echo "$me Git tag preparing (not executed)"
echo "    git commit -am 'Prepare release $version'"
echo "    git tag -a $version -m 'SlabShed release $version'"
echo "    git push origin && git push origin --tags"

##### End
echo ; echo "#########################"
echo "$me Done!"