#!/bin/sh

artillery quick  --rate 4 --duration 30 http://localhost:5000/sleep
