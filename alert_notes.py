import json

def lecture_notes(nom_fichier):
	json_file = open(nom_fichier)
	notes = json.load(json_file)
	json_file.close()
	return(notes['marks'])

def nouvelles_notes(notes_old, notes_new):
	notes = []
	indice_old = 0
	indice_new = 0
	while indice_new < len(notes_new):
		if (indice_old>=len(notes_old) or notes_new[indice_new]!=notes_old[indice_old]):
			notes.append(notes_new[indice_new])
		else :
			indice_old+=1
		indice_new+=1
	return (notes)

def afficher_notes(notes):
	for note in notes:
		print("Vous avez obtenu la note de "+str(note['mark'])+" en "+note['label']+": "+note['testName'])

def main():
	pluriel = ""
	fichier_old = '/data/Documents/Passion/arel_api/alert_notes/marks_old.json'
	fichier_new = '/data/Documents/Passion/arel_api/alert_notes/marks_new.json'
	notes_old = lecture_notes(fichier_old)
	notes_new = lecture_notes(fichier_new)
	nbreNotesOld = len(notes_old)
	nbreNotesNew = len(notes_new)
	if (nbreNotesNew != nbreNotesOld):
		if (nbreNotesNew > 1):
			plruiel = "s"
		print("Vous avez "+str(nbreNotesNew-nbreNotesOld)+" nouvelle"+pluriel+" note"+pluriel+" sur "+str(nbreNotesNew))
		notes = nouvelles_notes(notes_old, notes_new)
		afficher_notes(notes)
	else:
		print("Aucune nouvelle note")

main()