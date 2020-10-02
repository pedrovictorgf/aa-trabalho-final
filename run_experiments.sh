#!/bin/bash

for ((i = 0 ; i < $1 ; i++)); do
  	python3 strassen.py

	python3 traditional.py
done