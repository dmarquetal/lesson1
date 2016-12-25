#!/usr/bin/python
# -*- coding: utf-8 -*-

# preguntar por tu deporte favorito
print "¿Cuál es tu deporte favorito?",
deporte = raw_input()
print "Has elegido %s" %(deporte)

if deporte == "baloncesto":
    print "es muy guay este deporte"
elif deporte == "futbol":
    print "esto no eh"
elif deporte == "balonmano":
    print "este deporte no es tan guay"
else:
    print "no conozco la %s" %(deporte)
