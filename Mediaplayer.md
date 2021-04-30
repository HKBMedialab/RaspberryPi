# Rasperry Pi als einfachen MediaPlayer nutzen



## Erste Schritte und Installation

**1. Notwendige Teile**

- Speicherkarte: MicroSDHC oder MicroSDXC 16-32GB, Class 10, A3
- Raspberry Pi 3B, 3B+ oder 4
- USB-Netzteil 5V 3W
- Monitor
- ev. Gehäuse
- ev. microHDMI - HDMI Adapter
- ev. USB-Tastatur, USB-Maus

**2. SD-Karte vorbereiten**

1. [Raspberry Pi Imager](https://www.raspberrypi.org/software/) installieren
2. Im Raspberry Pi Imager Betriebssystem auswählen: "Raspberry Pi OS (32bit) Desktop"
3. SD-Karte auswählen
   (Beim einstecken der SD-Karte darauf achten, dass die Schreibschutz-Lasche nicht nach vorne rutscht.)
4. SD-Karte beschreiben
   Um den Schreibvorgang zu starten muss ein Adminpasswort eingegeben werden. Die Karte wird nach dem Prozess automatisch ausgeworfen.

**3. Vorbereiten für WLAN oder Ethernet**

Wird der Raspberry Pi mit einem Monitor und Tastatur verwendet, bei Punkt 4 fortsetzen. 

Wird der Raspberry Pi über WLAN oder Ethernet betrieben, muss die Karte ausgezogen und nochmals eingesteckt werden. Im Stammverzeichnis der Karte wird nun ein Ordner mit Namen "ssh" erstellt, um den SSH-Zugang zu aktivieren. Diese Option kann jederzeit per diesen Ordner oder in den Systemeinstellungen aktiviert bzw. deaktiviert werden.  

Damit sich der Raspberry Pi bereits beim ersten Start mit einem WLAN verbinden kann, kann zusätzlich – auch im Stammverzeichnis – eine Datei mit WLAN-Verbindungsinformationen angelegt werden.
Die Datei heisst "wpa_supplicant.conf" und hat folgenden Inhalt:

`country=CH`
`update_config=1`
`ctrl_interface=/var/run/wpa_supplicant`

`network={`
 `ssid="WLANNAME"`
 `psk="PASSWORT"`
`}`

Für Verbindungen mit WPA-gesicherten Netzwerken z.b. bfh oder eduroam braucht es spezielle Einstellungen. Bei Fragen den MediaLab Support kontaktieren.

Jetzt kann die Karte ausgeworfen und aus dem Adapter entfernt werden.

**3.1 Verbindung über WLAN**

Als erstes müssen wir die IP des Raspberry Pi herausfinden.  

**MacOS**

Mit Alt-Linksklick auf das WLAN-Icon in der Menuleiste sehen wir unsere eigene IP-Adresse. Die ersten drei Zahlen bilden das Subnet, in dem sich unser Rechner und der Raspberry Pi befinden. z.B. 192.168.0.

Mit dem Befehl`nmap`werden im Terminal alle Geräte im selben Subnet angezeigt: 
`nmap -sP 192.168.0.*`

In der Liste sollte sich ein Gerät mit dem Namen "raspberrypi" finden. (Falls unsicher, Rasp ausschalten, scannen, Rasp wieder einschalten und erneut scannen und die Ergebnisse vergleichen.)

**Windows**
LanScan oder IP-Scanner starten und das WLAN-Netzwerk scannen um die IP des Raspberry Pis herauszufinden. Mit Windows 10 (Update mind 2018) muss ein OpenSSH Client installiert werden: <https://www.raspberrypi.org/documentation/remote-access/ssh/windows10.md>

**3.2 Verbindung über Ethernet**

Gleiches Prozedere wie bei WLAN, aber dafür muss bei MacOS die Internetverbindung freigegeben werden:
Systemeinstellungen > Freigaben > Internetfreigabe > Ethernetadapter auswählen und Freigabe aktivieren.
Für Windows: <https://geekylane.com/giving-internet-to-raspberry-pi-using-ethernet-on-from-windows-10/>

Um die IP des Raspberry Pis herauszufinden:
`arp -a`

**3.3 Verbinden mit SSH**

Verbindung herstellen mit:
`ssh pi@192.168.0.10`

Das Default-Passwort ist "raspberry".

**4. System Einrichten**



**5. Raspberry Pi starten**

Die Speicherkarte muss eingesetzt werden, bevor der Strom angeschlossen wird und darf nicht unter Strom ausgezogen werden!

Monitor und Netzwerk auch vor dem Starten anschliessen.

**6. Einrichten mit Monitor und Tastatur**

Mit dem installierten Betriebssystem bootet der Raspberry Pi automatisch zum Desktop und startet den Einrichtungsassistenten.
Das Setup ist selbsterklärend und schnell gemacht. Achtung beim Passwortwechsel: dieser kann nicht Rückgängig gemacht werden.

Die Systemeinstellungen auf dem Raspberry Pi erreichen wir über das Hauptmenu oder indem wir eine Konsole starten und folgenden Befehl eingeben:
`sudo raspi-config`

Je nach Vorhaben
`System Options` > `Boot / Auto Login` > `Desktop Autologin aktivieren`
`System Options` > `Audio` Audioausgang wählen
`Display Options` > `Resolution`, `Underscan` anpassen
`Localisation Options` > `Locale`, `Timezone`, `Keyboard` anpassen.

Links zu Raspberry Pi Einstieg:
https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started
https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up
https://projects.raspberrypi.org/en/projects/raspberry-pi-using
https://projects.raspberrypi.org/en/projects/demo-programs/5

## Die Konsole im Raspberry Pi

Die Konsole (Terminal) im Raspberry Pi startet entweder direkt oder kann mit angeschlossenem Monitor über das Hauptmenu geöffnet werden.

In der Konsole dienen uns vor allem folgenden Befehle:

```shell
Pfeil hoch              letzten Befehl holen
Pfeil links, rechts     Cursor schieben
Alt + Links, Rechts     Cursor schieben um 1 Wort
Tabulator               Pfad oder Befehl vervollständigen
Ctrl-C                  Aktuellen befehl beenden, abbrechen
   
pwd                     Nennt den aktuellen Pfad/Verzeichnis.
ls						           Listet Dateien und Ordner im aktuellen Pfad.
ls -la					         -l für Liste vertikal, -a für versteckte Dateien.
cd						           "Change Directory"
cd ..					           Ins Verzeichnis darüber wechseln
cd ~					           Ins Homeverzeichnis wechseln (z.B. /home/pi/)
cd /home				         / bedeutet relativ zum System
cd home                 ohne / wird den Ordner "home" im aktuellen Verzeichnis gesucht.
   
man ls                  Manual zu einem Befehl öffnen. Beenden mit q.
mkdir video             Verzeichnis "video" erstellen.
rm film.mp4             Datei film.mp4 löschen. (Achtung, kein Papierkorb!)
cp film.mp4 film2.mp4	  Copy, Datei kopieren
mv film.mp4 film2.mp4	  Move, verschieben bzw. umbenennen.
find                    Dateien und Verzeichnisse suchen.
nano test.txt           Datei test.txt erstellen und mit den Editor nano bearbeiten.
sudo ls                 "super user do", führt Befehl mit Adminrechten aus. (Vorsicht!)
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

`sudo apt-get update`
`sudo apt-get upgrade`
`sudo reboot`

**2. Daten übertragen**

Die Daten können per USB-Stick auf den Raspberry Pi kopiert oder per SSH übertragen werden.

Für SSH ein neues Terminal Fenster öffnen, `scp` schreiben, zu kopierende Datei vom Finder ins Terminal ziehen und loslassen. Danach noch folgenden Befehl ergänzen:  `pi@192.168.0.10:/home/pi/film2.mp4`:

`scp /Users/admin/Desktop/film2.mp4 pi@192.168.0.10:/home/pi/film2.mp4`

Mit dem Passwort des Raspberry Pi bestätigen.

**3. Videoplayer**

Nun kann ein erstes Mal der Film abgespielt werden:

`vlc /home/pi/film2.mp4`
`vlc --help` listet alle möglichen Befehle und Optionen auf.

**4. Autostart mit init.d**

Wir erstellen ein neues Autostartfile:
`sudo nano /etc/init.d/mediaplay` 
und kopieren folgenden Text ein:

```bash
#!/bin/sh
#/etc/init.d/mediaplay
#

### BEGIN INIT INFO
# Provides:          mediaplay
# Required-Start:    $syslog $time $remote_fs
# Required-Stop:     $syslog $time $remote_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: simple media player
# Description:       Mediaplayer with vlc
### END INIT INFO

sudo -u pi /usr/bin/cvlc --fullscreen --loop /home/pi/film2.mp4
exit 1
```

Anstelle von `cvlc` kann auch `vlc` genutzt werden. Die Optionen wie `--loop` sowie auch der Pfad zum Video können selbstverständlich geändert werden. Der Name `mediaplay` nach `Provides:` muss mit dem Dateinamen übereinstimmen.

Mit Ctrl-X schliessen und speichern.

Die eben erstelle Datei muss ausführbar gemacht werden:

`sudo chmod +x /etc/init.d/mediaplay`

Der Dienst kann nun getestet werden:

`sudo /etc/init.d/mediaplay start`

Läuft das Skript wie gewünscht, muss die Autostartdatei in die entsprechenden Startroutinen aufgenommen werden:

` sudo update-rc.d mediaplay defaults`

Nach einem neustart `sudo reboot` sollte der Mediaplayer automatisch starten.

Wird die Autostartdatei geändert (zum Beispiel andere Videodatei) muss anschliessend der Befehl ` sudo update-rc.d mediaplay defaults` erneut ausgeführt werden.

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