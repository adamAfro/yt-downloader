#!/usr/bin/env python


from subprocess import PIPE, run
import argparse, sys, os, yaml


# Ścieżki skryptu
SCRIPT_PATH = os.path.dirname(sys.argv[0]) + "/"
TRANSLATIONS_PATH = SCRIPT_PATH + "translations/"


# Konfiguracja
with open(SCRIPT_PATH + "config.yaml", "r") as configF:
	config = yaml.load(configF, Loader = yaml.FullLoader)

	if config["directory"] and os.path.exists(config["directory"]):
		path = config["directory"]

	if config["language"]:
		langPath = TRANSLATIONS_PATH + config["language"] + ".yaml"

		if os.path.exists(langPath):
			with open(langPath, "r") as langF:
				lang = yaml.load(langF, Loader = yaml.FullLoader)


# Argumenty
hasLang = 'lang' in globals()

parser = argparse.ArgumentParser(prog = "yt-download", description = lang["prog-description"] if (hasLang and "prog-description" in lang) else "https://github.com/adamAfro/yt-downloader")

parser.add_argument('-i', '--download', help = lang["url-hint"] if (hasLang and "url-hint" in lang) else "YT URL")
parser.add_argument('-o', '--into', help = lang["output-hint"] if (hasLang and "output-hint") in lang else "output file")
parser.add_argument('-s', '--from', help = lang["startT-hint"] if (hasLang and "startT-hint") in lang else "start time")
parser.add_argument('-t', '--for', help = lang["time-hint"] if (hasLang and "time-hint" in lang) else "time")

args = parser.parse_args()


ytUrl = getattr(args, "download")
startT = getattr(args, "from")
time = getattr(args, "for")

if path:
	fName = path + "/" + getattr(args, "into")
else:
	fName = os.getcwd() + "/" + getattr(args, "into")


# Ustawienia konwersji
convParams = "-c:v copy -c:a copy -strict -2";
timeParams = "";

if startT:
	timeParams += "-ss " + startT + " "
if time:
	timeParams += "-t " + time + " "

finalCommand = 'ffmpeg {t} -i "{v}" {t} -i "{a}" {c} {f}.mp4'


# Pobieranie i konwersja
print("youtube-dl ...")

urlsFetchCommand = "youtube-dl -g " + ytUrl;
urls = run(urlsFetchCommand, stdout = PIPE, stderr = PIPE, universal_newlines = True, shell = True).stdout.split("\n")

videoUrl = urls[0]
audioUrl = urls[1]

print("...")

finalCommand = finalCommand.format(t = timeParams, v = videoUrl, a = audioUrl, c = convParams, f = fName);

print("FFmpeg ...")

os.system(finalCommand)
