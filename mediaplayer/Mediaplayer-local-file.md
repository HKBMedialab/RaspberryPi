# Rasperry Pi als einfachen MediaPlayer nutzen



## Erste Schritte und Installation

**1. Notwendige Teile**

- Speicherkarte: MicroSDHC oder MicroSDXC 16-32GB, Class 10, A3
- Raspberry Pi 3B, 3B+ oder 4
- USB-Netzteil 5V 3W
- Monitor
- USB-Tastatur
- USB-Maus
- ev. microHDMI - HDMI Adapter

**2. SD-Karte vorbereiten**

1. Raspberry Pi Imager von https://www.raspberrypi.org/software/ installieren
   1. Einstellungen (Zahnrad Symbol) öffnen und bei Bedarf WLAN Passwort einfügen.

2. Im Raspberry Pi Imager Betriebssystem auswählen: "Raspberry Pi OS (32bit) Desktop Lite"
3. SD-Karte auswählen
   (Beim einstecken der SD-Karte darauf achten, dass die Schreibschutz-Lasche nicht nach vorne rutscht.)
4. SD-Karte beschreiben
   Um den Schreibvorgang zu starten muss ein Adminpasswort eingegeben werden. Die Karte wird nach dem Prozess automatisch ausgeworfen.

Danach Karte auswerfen und in den Raspberry Pi einsetzen.

**4. Raspberry Pi starten**

Die Speicherkarte muss eingesetzt werden, bevor der Strom angeschlossen wird und darf nicht unter Strom ausgezogen werden!

**5. Betriebssystem Einrichten**

Mit dem installierten Betriebssystem bootet der Raspberry Pi automatisch zum Desktop und startet den Einrichtungsassistenten.
Das Setup ist selbsterklärend und schnell gemacht. Achtung beim Passwortwechsel: dieser kann nicht Rückgängig gemacht werden.

Die Systemeinstellungen auf dem Raspberry Pi erreichen wir über das Hauptmenu oder indem wir eine Konsole starten und folgenden Befehl eingeben:
`sudo raspi-config`

`System Options` > `Audio` Audioausgang wählen
`Display Options` > `Resolution`, `Underscan`
`Localisation Options` > `Locale`, `Timezone`, `Keyboard`

Links zu Raspberry Pi Einstieg:
https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started
https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up
https://projects.raspberrypi.org/en/projects/raspberry-pi-using
https://projects.raspberrypi.org/en/projects/demo-programs/5

## Die Konsole im Raspberry Pi

Die Konsole (Terminal) im Raspberry Pi startet entweder direkt oder kann mit angeschlossenem Monitor über das Hauptmenu geöffnet werden.

In der Konsole helfen uns folgende Befehle:

```shell
Pfeil hoch              letzten Befehl kopieren
Pfeil links, rechts     Cursor schieben
Alt + Links, Rechts     Cursor schieben um 1 Wort
Tabulator               Pfad oder Befehl vervollständigen
Ctrl + C                Aktuellen befehl abbrechen
   
pwd                     Nennt den aktuellen Pfad.
ls						           Listet Dateien und Ordner im aktuellen Pfad.
ls -la					         -l ausführliche Liste, -a zeigt versteckte Dateien.

cd						           "Change Directory"
cd ..					           Ins Über-Verzeichnis wechseln
cd ~					           Ins Homeverzeichnis des Users wechseln (z.B. /home/pi/)
cd /home				         / bedeutet relativ zum Stammverzeichnis des OS
cd home                 ohne / wird den Ordner im aktuellen Verzeichnis gesucht.
   
man ls                  Manual zu einem Befehl öffnen. Beenden mit q.
ls --help               Hilfe zu befehl erhalten.
mkdir video             Verzeichnis "video" erstellen.
rm film.mp4             Datei film.mp4 löschen. (Achtung, kein Papierkorb!)
cp film.mp4 film2.mp4	  Copy, Datei kopieren
mv film.mp4 film2.mp4	  Move, verschieben bzw. umbenennen.
find                    Dateien und Verzeichnisse suchen.
	find ~ -maxdepth 3 -name "*.txt"    Suche ab Homeverzeichnis Dateien, welche
													auf ".txt" enden, maximal 3 Verzeichnisse tief.

nano test.txt           Datei test.txt erstellen und mit nano bearbeiten.
			ctrl + O                Nano-Editor: Datei speichern
			Y													Nano-Editor: speichern bestätigen
			ctrl + X                Nano-Editor: schliessen

sudo ls                 "super user do", führt Befehl mit Adminrechten aus
													(Vorsicht!)
sudo reboot             System neustarten.
sudo shutdown now       System herunterfahren.
ssh                     stellt eine SSH Verbindung her.
scp                     Datei über ssh von einem Gerät auf ein anderes kopieren.
```

Nützliche Unix Befehle:
https://www.thegeekstuff.com/2010/11/50-linux-commands/
https://en.wikipedia.org/wiki/List_of_Unix_commands

## MediaPlayer einrichten

**1. System Updaten**

WLAN verbinden über Pfeil-Symbol oben rechts. *Für Verbindungen mit WPA-gesicherten Netzwerken z.b. bfh oder eduroam braucht es spezielle Einstellungen. Bei Fragen den MediaLab Support kontaktieren.* Verbindungen zum LAN mit Ethernet erfordern keine zusätzlichen Einstellungen.

*Update ist empfohlen aber nicht zwingend nötig. Dafür ist eine Internetverbindung erforderlich.*

`sudo apt-get update`
`sudo apt-get upgrade`
`sudo reboot`

**2. Daten übertragen**

Die Daten werden am einfachsten per USB-Stick auf den Raspberry Pi in den Ordner /home/pi/Videos kopiert und bestenfalls umbenannt in einen einfachen Namen ohne Sonderzeichen, z.B.: `video.mkv`.

**3. Videoplayer testen**

Nun kann der Film mit dem installierten VLC abgespielt werden:

`vlc /home/pi/film1.mp4`
`vlc --help` listet alle möglichen Befehle und Optionen auf.

**4. Autostart einrichten**

Bestehende Autostart-Datei editieren:

`sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`

```bash
@lxpanel --profile LXDE-pi
@pcmanfm --desktop --profile LXDE-pi
@xscreensaver -no-splash
```

An die bestehenden Zeilen wird folgende Zeile angefügt:

` @bash /home/pi/player.sh`

Mit `Ctrl + X` schliessen und mit `Y` speichern.

Danach wird die Player Datei erstellt und editiert:

`sudo nano /home/pi/player.sh`

```bash
#!/usr/bin/bash
while :
do
	cvlc -f --no-video-title-show --play-and-exit /home/pi/Videos/video.mkv
done
```

- `-f`		 startet den Player im Fullscreen-Modus
- `--no-video-title-show` 	verhindert eingeblendeten Dateinamen
- `--play-and-exit` 	Abspielen und beenden, statt auf dem letzten Frame stehen zu bleiben.

Mit `Ctrl + X` schliessen und mit `Y` speichern.

Die eben erstelle Datei wird ausführbar gemacht:

`sudo chmod +x /home/pi/player.sh`

Nach einem Neustart mit `sudo reboot` wird der Mediaplayer automatisch starten.

Zwischen den Wiedergaben, erscheint kurz der Desktop. Um dies zu verhindern, kann einerseits das Video bereits in der Datei x mal geloopt und so abgespeichert werden.

Zudem wird der Desktop-hintergrund geändert mit Rechtsklick auf den Desktop. Dann Farbe Schwarz wählen. Mit Rechtsklick auf die Menubar kann auch diese Schwarz gefärbt werden und auto-hide aktiviert werden. Danach erscheint zwischen den Wiedergaben lediglich ein schwarzes Fenster.

**5. Video- und Audio-Ausgänge konfigurieren**

Je nach Setup sind Änderungen nötig in den Dateien: `/boot/config.txt` oder `/boot/cmdline.txt`.

Diese Files sind auf dem sichtbaren Teil der SD-Karte und können auch an einem anderen PC angepasst werden. 

Video Optionen (HDMI, Composite)
https://www.raspberrypi.org/documentation/configuration/config-txt/video.md
https://bhavyanshu.me/tutorials/force-raspberry-pi-output-to-composite-video-instead-of-hdmi/03/03/2014/

Bei Composite folgendes Stecker-Layout beachten und eventuell mit Messgerät nachprüfen.
Tip 	->  Left
Ring 1 -> Right
Ring 3 -> Ground
Sleeve -> Video

[Quelle](https://www.raspberrypi-spy.co.uk/2014/07/raspberry-pi-model-b-3-5mm-audiovideo-jack/)

**6. Boottext und Splashscreen deaktivieren**

1. `sudo nano /boot/config.txt` und am Ende der Datei `disable_splash=1` einfügen.

2. `sudo nano /boot/cmdline.txt`
   `console=tty1` ändern zu `console=tty3` und am Ende der Zeile `consoleblank=1 logo.nologo quiet loglevel=0 plymouth.enable=0 vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fastboot noatime nodiratime noram` einfügen. Achtung: kein Zeilenumbruch einfügen!

[Quelle](https://ampron.eu/article/tutorial-simplest-way-to-remove-boot-text-on-the-raspberry-pi-based-kiosk-or-digital-signage-display/) 