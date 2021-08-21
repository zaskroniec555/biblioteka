#TODO: Ujednolicić język kodu - albo polski, albo angielski
#TODO: Wyszukiwanie w katalogu

from flask import Flask, render_template
import csv

app = Flask(__name__)

# TODO: Zamienić CSV na bazę danych SQL
database = list()

with open("database.csv", "r") as databaseFile:
    databaseReader = csv.DictReader(databaseFile)
    for line in databaseReader:
        database.append(line)

#TODO: Baza danych użytkowników
#TODO: Haszowanie haseł
loggedin=True

@app.route("/logowanie")
def logowanie():
    return render_template("logowanie.html")

def wymagaZalogowania(func):
    """
        Użycie tego dekoratora spowoduje, że jeżeli użytkownik nie jest zalogowany,
        zostanie przekierowany do strony logowania.
    """
    if loggedin:
        return func
    else:
        return logowanie

@app.route("/")
@app.route("/katalog")
@wymagaZalogowania
def katalog():
    return render_template("katalog.html", pozycje=database)

@app.route("/dodaj")
@wymagaZalogowania
def dodaj():
    return render_template("dodaj.html")