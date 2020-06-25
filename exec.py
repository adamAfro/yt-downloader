#!/usr/bin/env python


from subprocess import PIPE, run
import argparse, sys, os, yaml


with open("config.yaml", "r") as configF:
	config = yaml.load(configF, Loader = yaml.FullLoader)

	if config["directory"] and os.path.exists(config["directory"]):
		path = config["directory"]


parser = argparse.ArgumentParser()

parser.add_argument('-download', help='Youtube URL')
parser.add_argument('-into', help='Nazwa nowego pliku')
parser.add_argument('-from', help='Początek filmu')
parser.add_argument('-for', help='Czas trwania')

args = parser.parse_args()


ytUrl = getattr(args, "download")

startT = getattr(args, "from")
time = getattr(args, "for")

if path:
	fName = path + "/" + getattr(args, "into")
else:
	fName = os.getcwd() + "/" + getattr(args, "into")


convParams = "-c:v copy -c:a copy -strict -2";
timeParams = "";

if startT:
	timeParams += "-ss " + startT + " "
if time:
	timeParams += "-t " + time + " "

finalCommand = 'ffmpeg {t} -i "{v}" {t} -i "{a}" {c} {f}.mp4'


print("youtube-dl ...")

urlsFetchCommand = "youtube-dl -g " + ytUrl;
urls = run(urlsFetchCommand, stdout = PIPE, stderr = PIPE, universal_newlines = True, shell = True).stdout.split("\n")

videoUrl = urls[0]
audioUrl = urls[1]


print("...")

finalCommand = finalCommand.format(t = timeParams, v = videoUrl, a = audioUrl, c = convParams, f = fName);


print("FFmpeg ...")

os.system(finalCommand)
