#!/bin/bash

today=`date +"%Y-%m-%d"`
echo "${today}"

git add .
git commit -m "${today}"
git push -u origin master

