################################################################

## Tennis - Datenbeschaffung

## Autoren: R. Arocha, E. Boeni, K. Elliott, M. Huber, F. Schmid
## Prof. Andrea Back
## 8,045,1.00: IC: Technology und Market Intelligence

################################################################

## Beschreibung
################################################################
# In diesem Skript werden die einzelne *.csv Dateien (je Tennisspieler) eingelesen und in eine Excel-Datei zusammengefasst.
# Diese Exceldatei enthält die konsolidierten Instagramposts je Spieler, welche in einem weiteren Schritt mit einer Excel
# Formel übersetzt werden.
#
# In diesem Skript wird auch die *.csv Datei mit den Tweets eingelesen, aufbereitet und als Excel-Datei rausgelesen.
# Die einzelnen Tweets werden ebenfalls mit einer Excel Formel übersetzt.
#
# Die weitere Verarbeitung erfolgt im Skript "Tennis-Datenverarbeitung.Rmd"


## Vorbereitung
################################################################

# Working directory setzen
setwd <- setwd("~/01_Master/023_Technology & Market Intelligence/04_Daten")

## Konsolidierung von sInstagramdatensatz
################################################################

# Alle *.csv Files von jedem Spieler (Datensätze aus Instagram) befinden sich im gleichen Ordner
# Liste aller .csv files erstellen
list.filenames = list.files(getwd(), full.names = TRUE, pattern=".csv")

# Files einlesen
library(plyr)
library(stringr)

# Loop um alle *.csv Dateien vom Verzeichnis einzulesen
read_csv_filename <- function(list.filenames){
  ret <- read.csv(list.filenames, header=TRUE)
  ret$Source <- list.filenames
  ret
}

# Als import.list speichern
import.list <- ldply(list.filenames, read_csv_filename)

# Spalte mit Name vom Spieler einfügen
import.list$FileName <- str_split_fixed(import.list$FileName,"_",2)

# Inhalt ersetzen
import.list$Source <- gsub("C:/Users/aroch/OneDrive/Documents/01_Master/023_Technology & Market Intelligence/04_Daten/",
                           " ", import.list$Source, ignore.case= FALSE)
import.list$Source <- gsub(".csv"," ", import.list$Source, ignore.case= FALSE)
View(import.list)

# Spalten umbenennen
colnames(import.list) <- c("date", "insta_post", "player")


## Twitter
################################################################

# Daten einlesen
# Beachte: Die tweets.csv Datei muss zwingendermasse in einem Unterordner gespeichert werden.
twitter <- read.csv("~/01_Master/023_Technology & Market Intelligence/04_Daten/Tweets/tweets.csv",
  header=TRUE)

# Überflüssige Spalten entfernen
twitter$created_at = NULL
twitter$timezone = NULL
twitter$place = NULL
twitter$location = NULL
twitter$link = NULL
twitter$quote_url = NULL
twitter$video = NULL
twitter$retweet = NULL


# Als Excel-Datei exportieren
library(xlsx)
write.xlsx(import.list, file="instagram_complete_v1.xlsx") # Datumsspalte wird falsch exportiert
write.csv(import.list, file = "import.list.csv",row.names=FALSE) # Um bei der Datenverarbeitung, die Datumsspalte zu benutzen
write.xlsx(twitter, file="twitter_complete_v1.xlsx")


