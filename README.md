# ML/IDA 1: Project 2 -- Fire in the ***Montesinho*** Nature Park
This repository contains my final project for "Machine Learning and Intelligent Data Analysis 1". The project was part of the requirements for passing the course during the summer semester 2022 at the University of Potsdam. 

## Problem Setting
The administration of the nature park Montesinho in north-east Portugal wants to predict wild fires based on weather data of the Fire-Wheather-Index (FWI). The aim is to recognize the affected area and consequently the intensity of the imminent wild fire as early as possible in order to be able to adequatly assess the danger caused by the fire. To this aim, data from 517 wild fires have been collected. 
You have been asked to develop a model that predicts the burnt forest area as accurately as possible from the given data.

## Repo Structure
- documents: task description documents
- src:
    - data:
        - fires.csv: the data
        - README.md: explanation of features in database
    - additional_functions.py: outsourced functions for cleaner looking notebooks
    - data_exploration.ipynb: notebook exploring the data + finding preprocessing steps
    - models.ipynb: notebook implementing & comparing models + final thoughts
