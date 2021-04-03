#!/bin/bash

echo "enter project name"
read project_name

outer_dir=$(dirname $PWD)
new_proj_path=$outer_dir/$project_name


echo "remove old git tracking information? (y/n)"
read rm_git
if [ $rm_git == "y" ]; then
	echo "removing git files"
	rm .gitignore
	rm *.md
	rm -rf .git
fi

echo "add new git remote? (y/n"
read add_git
if [ $add_git == "y" ]; then
	echo "enter remote url"
	read git_remote
	if [ ! -z "$git_remote"  -a "$git_remote" != " " ]; then
		echo "adding git remote " $git_remote
		echo "# $project_name" >> README.md
		git init
		git add *
		git commit -am "initial commit"
		git branch -M main
		git remote add origin $git_remote
		git push -u origin main
	fi
fi

echo "configuring project: $project_name"
python cvproj.py $project_name

cd $new_proj_path
mkdir build
cd build
cmake ..
make
./$project_name
cd ..
rm cvproj.py
rm setup.sh
subl $new_proj_path
gnome-terminal