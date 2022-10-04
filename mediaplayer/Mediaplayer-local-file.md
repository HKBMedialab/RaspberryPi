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
2. Im Raspberry Pi Imager Betriebssystem auswählen: "Raspberry Pi OS (32bit) Desktop Lite"
3. Einstellungen (Zahnrad Symbol unten rechts) öffnen.
   1. User und Passwort setzen und irgendwo notieren.
   2. bei Bedarf WLAN Zugangsdaten eingeben.
4. SD-Karte auswählen
   (Beim einstecken der SD-Karte darauf achten, dass die Schreibschutz-Lasche nicht nach vorne rutscht.)
5. SD-Karte beschreiben
   Um den Schreibvorgang zu starten muss ein Adminpasswort eingegeben werden. Die Karte wird nach dem Prozess automatisch ausgeworfen.

**3. Für Gebrauch mit Composite zusätzliche Schritte ausfühen**

*ACHTUNG!! Polarität des TRRS-Steckers muss mit RaspberryPi übereinstimmen. Beachte Punkt 3. unter TIPPS am Ende dieser Anleitung!*

1. Karte herausziehen und nochmals einstecken.
2. Im Verzeichnis `boot` die Datei `config.txt` zum bearbeiten in einem CodeEditor oder z.B. TextEdit öffnen.
   1. folgende Zeilen kommentieren (ein # am Zeilenbeginn eingeben)
      ```
      #hdmi_force_hotplug=1
      ```
   2. folgdende Teilen auskommentieren (# entfernen) bzw. ergänzen.
      ```
      hdmi_ignore_hotplug=1
      enable_tvout=1
      sdtv_mode=2
      disable_splash=1
      ```
   3. Danach Karte wieder auswerfen.

**4. Raspberry Pi starten**

Die Speicherkarte muss eingesetzt werden, bevor der Strom angeschlossen wird und darf nicht unter Strom ausgezogen werden!

**5. Betriebssystem Einrichten**

Mit dem installierten Betriebssystem bootet der Raspberry Pi automatisch zum Desktop und startet den Einrichtungsassistenten.
Das Setup ist selbsterklärend und schnell gemacht. Achtung beim Passwortwechsel: dieser kann nicht Rückgängig gemacht werden.

Die Systemeinstellungen auf dem Raspberry Pi erreichen wir über das Hauptmenu oder indem wir eine Konsole starten und folgenden Befehl eingeben:
`sudo raspi-config`

`System Options` > `Audio` Audioausgang wählen
`Localisation Options` > `Locale`, `Timezone` und `Keyboard` anpassen

Links zu Raspberry Pi Einstieg:
https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started
https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up
https://projects.raspberrypi.org/en/projects/raspberry-pi-using
https://projects.raspberrypi.org/en/projects/demo-programs/5

## Die Konsole im Raspberry Pi
<details><summary>Tipps aufklappen</summary>

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

</details>
	
## MediaPlayer einrichten

**1. Daten übertragen**

Die Daten werden am einfachsten per USB-Stick auf den Raspberry Pi in den Ordner /home/pi/Videos kopiert und bestenfalls umbenannt in einen einfachen Namen ohne Sonderzeichen, z.B.: `video.mp4`. Unterstützt werden die Container mp4, mov, mkv, ogg. Max Bitrate 20Mbit/s, empfohlen h.264.

**3. Videoplayer testen**

Nun kann der Film mit dem installierten VLC abgespielt werden:

`vlc /home/pi/Videos/video.mp4`

`vlc --help` listet alle möglichen Befehle und Optionen auf.

**4. Autostart einrichten**

Bestehende Autostart-Datei editieren:

`sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`

```bash
@lxpanel --profile LXDE-pi
@pcmanfm --desktop --profile LXDE-pi
@xscreensaver -no-splash
```

Am Ende der Datei folgende Zeile einfügen:

` @bash /home/pi/player.sh &`

Mit `Ctrl + X` schliessen und mit `Y` speichern.

**5. Player Datei erstellen**

`sudo nano /home/pi/player.sh`

Bestimmte lokale Datei abspielen:
<details><summary>Aufklappen</summary>

```bash
#!/usr/bin/bash
while :
do
	cvlc -f --no-video-title-show --play-and-exit /home/pi/Videos/video.mp4
done
```

</details>

Alle Filme auf USB-Stick abspielen
<details><summary>Aufklappen</summary>

```bash
#!/usr/bin/bash

sleep 5
	
find /media/pi/*/* -maxdepth 0 -iregex '.*\.\(mp4\|mov\|mkv\|avi\)$' -type f > /home/pi/playlist.txt

while :
do
        while read -r line; do
                cvlc -f --no-video-title-show  --play-and-exit "$line"
        done < /home/pi/playlist.txt
done
```

*Erklärung:* Wenn ein USB-Stick angeschlossen ist, wird er im Pfad `/media/pi/` angezeigt. Mit dem Befehl `find`suchen wir im Hauptordner des USB-Sticks nach Dateien mit einer der folgenden Endungen. Mit `-type f`beschränken wir die Resultate zudem auf Dateien, also keine Ordner oder Verknüpfungen. Alle Resultate werden in die Datei `playlist.txt`geschrieben. Anschliessend wird mit `while`ein unendlicher Loop gestartet, in dem jede Zeile der Playlist mit `cvlc` abgespielt wird.


</details>

- `-f`		 startet den Player im Fullscreen-Modus
- `--no-video-title-show` 	verhindert eingeblendeten Dateinamen
- `--play-and-exit` 	Abspielen und beenden, statt auf dem letzten Frame stehen zu bleiben.

Mit `Ctrl + X` schliessen und mit `Y` speichern.

Die eben erstelle Datei wird ausführbar gemacht:

`sudo chmod +x /home/pi/player.sh`

Nach einem Neustart mit `sudo reboot` wird der Mediaplayer automatisch starten.

## TIPPS

1. Zwischen den Wiedergaben, erscheint kurz der Desktop. Um dies zu verhindern, gibt es folgende Optionen
   1. Das Video bereits in der Datei x mal loopen.
   2. Desktop-Hintergrund ändern mit Rechtsklick auf den Desktop. Layout "No-Image", Farbe Schwarz wählen.
   3. Rechtsklick auf die Menubar, `Panel Settings` > `Advanced` > `Minimize panel ...` aktivieren.
   4. Rechtsklick auf die Menubar, `Panel Appearance` > `Colour` schwarz auswählen.
   
2. Für mehrere Videos in der Datei `player.sh` die Zeile `cvlc ... ` duplizieren und Dateinamen anpassen.

3. Video- und Audio-Ausgänge konfigurieren für Composite
   
   Bei Composite beachten, dass das Stecker-Layout vom RaspberryPi folgende Belegung hat. Eventuell mit Messgerät nachprüfen. Wichtig ist, dass Video und Ground richtig liegen. 

   | Stecker  | Signal   |
   | -------- | -------- |
   | Spitze   | Audio-L  |
   | Ring 1   | Audio-R  |
   | Ring 2   | Ground   |
   | Ring 3   | Video    |
   
   Video Optionen (HDMI, Composite)
   https://www.raspberrypi.org/documentation/configuration/config-txt/video.md
   https://bhavyanshu.me/tutorials/force-raspberry-pi-output-to-composite-video-instead-of-hdmi/03/03/2014/

   [Quelle](https://www.raspberrypi-spy.co.uk/2014/07/raspberry-pi-model-b-3-5mm-audiovideo-jack/)

5. Boottext deaktivieren

   1. `sudo nano /boot/cmdline.txt`
   2. `console=tty1` ändern zu `console=tty3`
   3. am Ende der Zeile `consoleblank=1 logo.nologo quiet loglevel=0 plymouth.enable=0 vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fastboot noatime nodiratime noram` einfügen. Achtung: kein Zeilenumbruch einfügen!

   [Quelle](https://ampron.eu/article/tutorial-simplest-way-to-remove-boot-text-on-the-raspberry-pi-based-kiosk-or-digital-signage-display/) 
