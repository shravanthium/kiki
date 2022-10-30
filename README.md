# kiki
A small distance courier service to deliver packages.


This repo consists of below modules:

1. Courier Module:
Estimate the total delivery cost of each package with an offer code (if applicable).

Command to compute delivery cost for each packge from cli.

```
$ python3 kiki.py 100 3 -p PKG1,5,5,OFR001 PKG2,15,5,OFR002 PKG3,10,100,OFR003
```


2. Scheduler Module:
Computes the estimated delivery time for every package by maximizing no. of packages in every shipment.

Command to compute delivery time for each packge from cli.

```
$ python3 kiki.py 100 5 -p PKG1,50,30,OFR001 PKG2,75,125,OFFR0002 PKG3,175,100,OFFR003 PKG4,110,60,OFFR002 PKG5,155,95,NA -v 2,70,200
```
