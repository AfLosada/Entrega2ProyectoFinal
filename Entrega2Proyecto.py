# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 07:01:38 2019

@author: Andres Losada
"""

from __future__ import division
from pyomo.environ import *

from pyomo.opt import SolverFactory

import sys
import os
from math import sqrt

os.system("clear")

Model = ConcreteModel()

numPaises = 3
numObjetivos = 5
numSexos = 2
numIdiomas = 2
numEdades = 6
numNichos = 2
numUbicaciones = 2
presupuesto = 100000 # El presupuesto del ususario

# Sets: cada entero representa un pais
Model.paises = RangeSet(1,numPaises)
Model.objetivos = RangeSet(1,numObjetivos)
Model.sexos = RangeSet(1,numSexos)
Model.idiomas = RangeSet(1,numIdiomas)
Model.nichos = RangeSet(1,numNichos)
Model.ubicaciones = RangeSet(1,numUbicaciones)

#Parametros

Model.numeroHabitantes = Param(Model.paises, mutable = True)
Model.costoObjetivo = Param(Model.objetivos, mutable = True)
Model.porcentajeSexo = Param(Model.sexos, mutable = True)
Model.porcentajeHablantes = Param(Model.idiomas, mutable = True)
Model.porcentajeDentroDeNicho = Param(Model.nichos, mutable = True)
Model.costoUbicacion = Param(Model.ubicaciones, mutable = True)
Model.costoPorImpresion = Param(Model.paises, mutable = True)

#Habitantes por Pais con Facebook
Model.numeroHabitantes[1] = 33000000  #Colombia
Model.numeroHabitantes[2] = 230000000 #E.E.U.U.
Model.numeroHabitantes[3] = 44000000  #UK

#Costo Objetivos
Model.costoObjetivo[1] = 1   #Trafico
Model.costoObjetivo[2] = 0.3 #Brand Awareness
Model.costoObjetivo[3] = 0.8 #Traffic
Model.costoObjetivo[4] = 1.4 #Lead Generation
Model.costoObjetivo[5] = 2   #Conversions

#Porcentaje de Cada Sexo con Facebook
Model.porcentajeSexo[1] = 0.62
Model.porcentajeSexo[2] = 0.38

#Porcentaje de Hablantes 
Model.porcentajeHablantes[1] = 0.52 #Ingles
Model.porcentajeHablantes[2] = 0.16 #Español

#Porcentaje Dentro De Nicho
Model.porcentajeDentroDeNicho[1] = 0.03 #Viajero
Model.porcentajeDentroDeNicho[2] = 0.013 #High Tech

#Costo por Ubicacion
Model.costoUbicacion[1] = 20/1000 #Facebook
Model.costoUbicacion[2] = 28/1000 #Instagram

#Costo por Impresion en dolares
Model.costoPorImpresion[1] = 1/1000 #Colombia
Model.costoPorImpresion[2] = 33/1000 #E.E.U.U.
Model.costoPorImpresion[3] = 11.55/1000 #UK

#variables

Model.objetivo = Var(Model.objetivos, domain=Binary)
Model.sexo = Var(Model.sexos, domain=Binary)
Model.idioma = Var(Model.idiomas, domain=Binary)
Model.nicho = Var(Model.nichos, domain=Binary)
Model.ubicacion = Var(Model.ubicaciones, domain=Binary)

Model.x = Var(Model.paises, domain=Binary) # Elige o no el páis

def pob(p):
    return sqrt(-1*Model.numeroHabitantes[p]*Model.x[p]*(22*(10**8)))

def costos1(p, o, s): 
    return Model.x[p] * Model.costoObjetivo[o] + Model.sexo[s]*Model.porcentajeSexo[s]

def costos2(u, p):
    return Model.costoUbicacion[u] * Model.ubicacion[u] + Model.costoPorImpresion[p]*Model.x[p]

def porc1(i, n):
    return Model.porcentajeHablantes[i]*Model.idioma[i] + Model.porcentajeDentroDeNicho[n]+Model.nicho[n]
#Funcion Objetivo
Model.func_objetivo = Objective(expr = sum( ((pob(p)*costos1(p,o,s)*costos2(u,p)*porc1(i,n))/presupuesto) for p in Model.paises for o in Model.objetivos for s in Model.sexos for u in Model.ubicaciones for i in Model.idiomas for n in Model.nichos ))

#Constraints

#Model.rest = Constraint(expr = sum(Model.objetivo[o] for o in Model.objetivos) == 1)

#Solver
SolverFactory('mindtpy').solve(Model, mip_solver='glpk', nlp_solver='ipopt')


Model.display()

