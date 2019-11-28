#!/bin/bash
# lecture_notes.sh

if [ "$1" = "afficher" ]
then
	read -p 'Entrez votre mot de passe : ' -s pass
	echo -e "\nChargement des notes..."
	key=`http -a alert-notes-79:nBiMgXIyXZqEorwIp3q9 -f POST https://arel.eisti.fr/oauth/token grant_type=password username=tirelnicol password=$pass scope=read format=json | tail -1 | jq '.access_token'`
	if [ $key != "null" ]
	then
		key=`sed -e 's/^"//' -e 's/"$//' <<<"$key"`
		http -v -j https://arel.eisti.fr/api/me/marks --auth-type=jwt --auth=$key | tail -1 > /data/Documents/Passion/arel_api/alert_notes/marks_new.json
		python3 /data/Documents/Passion/arel_api/alert_notes/alert_notes.py
	else
		echo "Le mot de passe entré n'est pas le bon."
	fi
elif [ "$1" = "remplacer" ]
then
	mv /data/Documents/Passion/arel_api/alert_notes/marks_new.json /data/Documents/Passion/arel_api/alert_notes/marks_old.json
else
	echo "Erreur, il faut passer 'afficher' ou 'remplacer' en paramètre"
fi