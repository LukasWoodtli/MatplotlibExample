#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import time
import datetime as dt
import os

IN_FILE = os.path.split(os.path.realpath(__file__))[0]
IN_FILE = os.path.join(IN_FILE, "in.txt")

def get_data():
  dates = []
  values = []
  data = open(IN_FILE, 'r')
  for line in data:
    line = line.strip()
    if line != "":
      tokens = line.split(';')
      assert len(tokens) == 2
      dates.append(dt.datetime.strptime(tokens[0],"%d.%m.%Y").date())
      value = tokens[1].strip()
      values.append(float(value.strip()))
  return dates, values


def plot(data):
  fig, ax = plt.subplots()
  ax.plot(data[0], data[1],'b-')

  x1,x2,y1,y2 = plt.axis()
  plt.axis((x1,x2,89,95))

  # rotates and right aligns the x labels, and moves the bottom of the
  # axes up to make room for them
  fig.autofmt_xdate()

  ax.grid(True)
  plt.show()


def main():
    plot(get_data())

if __name__ == "__main__":
  main()
