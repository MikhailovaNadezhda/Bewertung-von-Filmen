## Eine Bewertung von Filmen mit Empfehlung von Ansichten

Es gab eine Tabelle mit der Geschichte des Ansehens von Filmen in einem Online-Kino.
Zwei Felder: Benutzer, Film

Ich habe ein Python-Skript erstellt,
die die Logik des Algorithmus implementieren würden, um Filme zum Ansehen zu empfehlen, die Benutzer noch nicht gesehen haben.

Die Logik ist folgende:
<br>•Nehmen wir an, der Benutzer hat sich Film A angesehen
<br>•Stellen Sie fest, welche anderen Benutzer Film A gesehen haben
<br>• Bestimmen Sie, welche anderen Filme alle diese Benutzer gesehen haben
<br>•Wir gruppieren die gefundenen Filme nach Namen und ermitteln für jeden die Anzahl der Nutzer, die ihn angesehen haben
<br>•Je mehr Benutzer es angesehen haben, desto höher ist ihre Bewertung in der Empfehlungsliste.
<br>•Die abschließende Abfrage sollte alle Filme, die alle Nutzer angesehen haben, im Empfehlungsmodell berücksichtigen.
<br>•Ausgabetabelle: Benutzer, Empfehlungsfilm, Bewertung der Empfehlung
