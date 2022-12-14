# Movie Recommender System
![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)
![API](https://img.shields.io/badge/API-TMDB-fcba03)

## Table of Content
* [Overview](#overview)
* [Screenshots](#screenshots)
* [Cosine Similarity](#cosine-similarity)
* [Installation And Run The Project](#installation-and-run-the-project)

## Overview
A web based movie recommendation system using content based filtering
and recommendation based on the idea that is if a person likes a movie 
of a particuler category then another same category movie which has not 
been watched by him yet can be recommended to him.

## Screenshots
![2022-08-14 (2)](https://user-images.githubusercontent.com/93439623/184534479-5f2a72f2-0a2e-4086-ad3e-7043166b8089.png)

## Cosine Similarity
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity
## Installation And Run The Project
- Clone or download this repository to your local machine.
- Install all the libraries from requirements.txt file by using
```bash
  pip  install -r reuirements.txt
```
- Get your API key from https://www.themoviedb.org/ 
- Replace api_key in the 9th line of reco.py and save it.
- Open your terminal and run the following command
```bash
  streamlit run reco.py
```
- Go to your browser and type http://localhost:8501/ in the address bar.

- And, there you go!
