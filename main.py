# Reguläre Ausdrücke importieren
import re


def calculate(term):

	expression = ["parentheses"]
	while expression is not None:
		if (re.search(r"(\([^(]*\))", term)) is None:
			phrase = term
		else:
			phrase = str((re.search(r"(\([^(]*\))", term)).group(1))
			phrase = re.sub(r"\(", " ", phrase, count=1)
			phrase = re.sub(r"\)", " ", phrase, count=1)

		# Potenzieren
		expression = ["exponentiate"]
		# Für alle Potenzen durchgehen
		while expression is not None:
			# Potenz suchen
			expression = re.search(r"(-?\d+\.?\d*)\s*(\^)\s*(-?\d+\.?\d*)", phrase)
			# Falls Potenz gefunden
			if expression is not None:
				# Wert der Potenz berechnen
				value = float(expression.group(1)) ** float(expression.group(3))
				# Potenz durch Wert ersetzen
				phrase = re.sub(r"(-?\d+\.?\d*)\s*(\^)\s*(-?\d+\.?\d*)", str(value), phrase, count=1)

		# Multiplizieren und Dividieren
		expression = ["multiply_divide"]
		# Für alle Multiplikationen und Divisionen durchgehen
		while expression is not None:
			# Multiplikation oder Division suchen
			expression = re.search(r"(-?\d+\.?\d*)\s*([*/])\s*(-?\d+\.?\d*)", phrase)
			# Falls Multiplikation oder Division gefunden
			if expression is not None:
				# Falls Multiplikation
				if expression.group(2) == "*":
					# Produkt berechnen
					value = float(expression.group(1)) * float(expression.group(3))
				# Falls Division
				elif expression.group(2) == "/":
					# Quotient berechnen
					value = float(expression.group(1)) / float(expression.group(3))
				else:
					value = None
				# Multiplikation oder Division durch Produkt oder Quotient ersetzen
				phrase = re.sub(r"(-?\d+\.?\d*)\s*([*/])\s*(-?\d+\.?\d*)", str(value), phrase, count=1)

		# Addieren und subtrahieren
		expression = ["add_subtract"]
		# Für alle Additionen und Subtraktionen durchgehen
		while expression is not None:
			# Addition oder Subtraktion suchen
			expression = re.search(r"(-?\d+\.?\d*)\s*([+-])\s*(-?\d+\.?\d*)", phrase)
			# Falls Addition oder Subtraktion gefunden
			if expression is not None:
				# Falls Addition
				if expression.group(2) == "+":
					# Summe berechnen
					value = float(expression.group(1)) + float(expression.group(3))
				# Falls Subtraktion
				elif expression.group(2) == "-":
					# Differenz berechnen
					value = float(expression.group(1)) - float(expression.group(3))
				else:
					value = None
				# Addition oder Subtraktion durch Summe oder Differenz ersetzen
				phrase = re.sub(r"(-?\d+\.?\d*)\s*([+-])\s*(-?\d+\.?\d*)", str(value), phrase, count=1)
		if (re.search(r"(\([^(]*\))", term)) is None:
			term = phrase
		else:
			term = re.sub(r"(\([^(]*\))", phrase, term, count=1)
			expression = ["True"]
	return term


while True:
	print(calculate(input("Taschenrechner: ")))
	weitere_berechnung = input("Willst du eine weitere Berechnung durchführen [Y/n]? ")
	if weitere_berechnung != "y" and weitere_berechnung != "Y" and weitere_berechnung != "":
		break

print("\nVielen Dank für die Benutzung des Taschenrechners!")
