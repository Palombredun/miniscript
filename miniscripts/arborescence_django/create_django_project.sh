#!/bin/bash

n=1
for arg in "$@"
do
	if [ $n = 1 ]; then
		`django-admin startproject $arg .
		n=$((n+1))
	else
		echo $arg
		python manage.py startapp $arg
		touch "$arg"/urls.py
		mkdir "$arg"/templates
		mkdir "$arg"/templates/"$arg"
		mkdir "$arg"/static
		mkdir "$arg"/static/"$arg"
	fi
done
