from imdb import Cinemagoer
import pandas as pd
import os
from datetime import datetime
import numpy as np
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
from PIL import Image
from fpdf import FPDF

#You can change the movie IMDB number on line 33 to the one for your desired movie
#These IDs can be located at https://www.lddb.com/index.php


#importing libraries to access movie data, access date and time in Y/M/D/H/M/S, and generate a wordcloud

current_timedate = datetime.now()

date_time_filename = current_timedate.strftime("%Y%m%d_%H%M%S")

date_time_text = current_timedate.strftime('%m/%d/%Y')

#Date and time format for displaying .txt file: YYYYMMDD_HHMMSS and adding date to .txt file MMDDYYYY


file_name = "fullName_Godfather_Info" + date_time_filename

#adding my info to the filename.

imdb_retriever = Cinemagoer()

Godfather = imdb_retriever.get_movie('0068646')

print("Format: Movie\n",f"Movie Title: {Godfather}\n")

for director in Godfather['directors']:
 print(f"Director:  {director['name']}\n")

imdb_retriever.update(Godfather, ['technical'])

print("Technical Details:", "\n\n", Godfather.get('tech'))

Godfather_Plot = Godfather.get('plot')
print(f"\nPlot:\n\n {Godfather_Plot}")

#Printing out movie title, directors, technical details, and plot to console



Godfather_main_file = open("Godfather_movie\Godfather_Movie_Info.txt", "a")

Godfather_main_file.write(f"Movie Title: {Godfather}\n\nType: Film\n\nSource: IMDB\n\nInvestigator: fullName")
Godfather_main_file.write(f"\n\nContent Acquired: {date_time_text} \n\nSummary Date: {date_time_text}\n\n Director: {director['name']}\n\n")
Godfather_main_file.write(f"Technical Details: \n\n{Godfather.get('tech')}")
Godfather_main_file.write(f"\n\nContent Summary:\n\n {Godfather_Plot}")
Godfather_main_file.close()

# appending metadata and summary to a .txt file [1]

Godfather_summary_file = open("Godfather_movie/Godfather_Movie_Summary.txt", "w")
Godfather_summary_file.write(f"{Godfather_Plot}")
Godfather_summary_file.close()

#Writing a summary file to be used for wordcloud



Godfather_text = open("Godfather_movie/Movie_Summary.txt").read()
wordcloud = WordCloud(width=500, 
                      height=500,
                      prefer_horizontal=0.5,
                      background_color="rgba(0, 0, 0, 0)", 
                      mode="RGBA").generate(Godfather_text)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file("Godfather_movie/Godfather_wordcloud.png")

# Specifying wordcloud parameters and outputting them to a .png file [1]




#[1] Python-course.eu https://python-course.eu/applications-python/python-wordcloud-tutorial.php





