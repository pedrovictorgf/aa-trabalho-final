#!/bin/bash

DEFAULT_NUMBER_OF_ROUNDS=15

for ((i = 0 ; i < ${1:-DEFAULT_NUMBER_OF_ROUNDS} ; i++)); do
  	python3 strassen.py

	python3 traditional.py
done
