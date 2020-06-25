# yt-downloader
Pobiera film z youtube ze wskazanego przedziału czasowego. Działa przy użyciu FFmpeg i youtube-dl

## Linux
Aby skrypt działał plik musi być wykonywalny (`chmod +x exec.py`).

Aby pobrać film z youtube skrypt musi być odtworzony z podanymi argumentami (początek i czas można pominąć)

`./exec.py -download [adres filmu na youtube] -into [nazwa pliku] -from [początek pobierania] -for [czas do pobrania]`
  
Przykładowo: `./exec.py -download https://youtu.be/9cX17CeYKt0 -into Jumper -from 00:00:47.00 -for 00:00:03.00` pobierze moment upadku osoby na nagraniu https://youtu.be/9cX17CeYKt0 do pliku „Jumper.mp4” 


