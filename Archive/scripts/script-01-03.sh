#https://exercism.org/tracks/bash/exercises

#BASH AVANCE : bash scripting .pdf



#!/bin/bash

#https://medium.com/@sankad_19852/shell-scripting-exercises-5eb7220c2252

# ls -l to see all permissions

# chmod +rwx filename to add permissions
# chmod -rwx filename to remove
# chmod +x filename to allow executable

# chmod u+rwx /  g+rwx / o+rwx

# Files test operators:  returns true if 
# 	-e file exists
#	-a file exists
#	-f file is a regular file (not a directory or device file)
#	-s file is not zero size
#	-d is a directory
#	-b file is a block device
#	-c file is a character device

function ex1 {
	message="Shell Scripting is Fun!"
	OUT=$(hostname)

	echo $message
	echo "This scritp is running on" $OUT
}


function ex2 {
	FILE=~/myFile.txt

	if [ -f "$FILE" ] ; then
		if [ -w "$FILE" ]; then
			echo "You have permissions to write on $FILE."
		else
			echo "You do NOT have permissions to write on $FILE."
		fi
	else
		echo "$FILE passwords are enabled."
	fi
}

function ex3 {
	ANIMALS="man bear pig dog cat sheep"
	for ANIMAL in $ANIMALS 
	do
      		echo $ANIMAL
	done
}



#https://tldp.org/LDP/abs/html/fto.html
function ex4 {
	INPUT=$1

	if [ -f "$INPUT" ] ; then
		echo "$INPUT is a regular file."
	elif [ -d "$INPUT" ]; then 
		echo "$INPUT is a directory."
	else
		echo "$INPUT is any type of file."

	fi
	ls -l $INPUT
}

function ex5 {
	INPUT=$1

	if [ -f "$INPUT" ] ; then
		echo "$INPUT is a regular file."
	elif [ -d "$INPUT" ]; then 
		echo "$INPUT is a directory."
	else
		echo "$INPUT is any type of file."

	fi
	ls -l $INPUT
}

function ex6 {
	FILES=$@
	for FILE in $FILES
	do
		echo " "
		ex5 $FILE
	done
}

function ex7 {
	echo "This script will exit with 0 exit status."
	exit 0
	#echo "The date command exit status : ${status}"
}


#Le fichier /etc/shadow est utilisé pour augmenter le niveau de sécurité des mots de passe. Le fichier contient une version hashée des mots de passe et seuls des utilisateurs très privilégiés peuvent y avoir accès. Généralement, ces données sont conservées dans des fichiers appartenant à l'utilisateur root et seulement accessibles par lui.
function ex8 {
	cat /etc/shadow
	#echo $?
	if [ "$?" -eq "0" ] ; then
	    echo "Command succeeded"
	    exit 0  
	else
	    echo "Command failed"
	    exit 1
	fi
}


function ex9 {
	local NUMBER_OF_FILE=$(ls -l | wc -l)
    	echo "$NUMBER_OF_FILE"
}

function ex10 {
	myPATH=$1
	DAY=$(date +%F)
	for FILE in $myPATH*.txt
	do
		myfile=$(basename $FILE .txt)
		EXT="${FILE##*.}"
		echo $myPATH $FILE $(basename $FILE .txt) ${myPATH}${DAY}-${myfile}.$EXT
		mv $FILE ${myPATH}${DAY}-${myfile}.$EXT
	done
}


function ex11 {
	DIR=$(pwd)
	
	myPATH=$1
	DAY=$(date +%F)
	
	cd $myPATH
	
	echo "Please enter the file extension:"
   	read EXTENSION

	echo "Please enter the prifix:(press enter for $DAY)"
   	read DAY
   	
   	echo $EXTENSION $DAY $(pwd)
   	
   	for NAME in *.$EXTENSION
	 do
	   echo "Renaming $NAME to ${DAY}-${NAME}"
	   #mv $NAME ${DAY}-${NAME}
	 done
	 
	 cd $DIR
}

# Created the start-up script for an application start and stop.
function ex12 {
INPUT=$1
cd /hms/installs/mongod/mongodb-linux-x86_64-2.6.0/bin
case $INPUT instart)
       ./mongod -f ../../mongod.conf &
       echo "Mongodb server Start"
       ;;stop)
      PID_ID=$(ps -ef | grep mongo | cut -d" " -f3 | sed '1!d')
      kill $PID_IDif [ $? -eq '0']
      echo "Mongodb server Stop"
      ;;*)
     echo "Error input"
     ;;esac
}


#Write the shell script that displays one random number on the screen and also generates a system log message with that random number.Use the “user” facility and “info” facility for your messages.
function ex13 {
	MESSAGE="Random number is:$RANDOM"
	echo "$MESSAGE"
	logger -p user.info "$MESSAGE"
}

#ex4 $1
#ex6 $@
#ex7
#ex8
#ex10 $1
#ex11 $1


