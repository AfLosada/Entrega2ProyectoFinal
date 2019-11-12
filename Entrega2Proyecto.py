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

os.system("clear")

Model = ConcreteModel()

numPaises = 3
numObjetivos = 5
numSexos = 2
numIdiomas = 2
numEdades = 6
numNichos = 2
numUbicaciones = 2
presupuesto = 100 # El presupuesto del ususario

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
Model.costoObjetivo[1] = 0.7   #Engagement
Model.costoObjetivo[2] = 1   #Brand Awareness
Model.costoObjetivo[3] = 0.6 #Traffic
Model.costoObjetivo[4] = 0.2 #Lead Generation
Model.costoObjetivo[5] = 0.1   #Conversions

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
Model.costoPorImpresion[1] = 66/1000 #Colombia
Model.costoPorImpresion[2] = 1/1000 #E.E.U.U.
Model.costoPorImpresion[3] = 11.55/1000 #UK

#variables

Model.objetivo = Var(Model.objetivos, domain=Binary)
Model.sexo = Var(Model.sexos, domain=Binary)
Model.idioma = Var(Model.idiomas, domain=Binary)
Model.nicho = Var(Model.nichos, domain=Binary)
Model.ubicacion = Var(Model.ubicaciones, domain=Binary)

Model.x = Var(Model.paises, domain=Binary) # Elige o no el páis

def poblacion(p, s, i, n):
    return (Model.numeroHabitantes[p]*Model.x[p])  * porcOyS(s) * porcHyN(i,n)


def porcOyS(s): 
    return Model.sexo[s]*Model.porcentajeSexo[s]

def costosPorPersona(u, o, p):
    return Model.costoUbicacion[u] * Model.ubicacion[u] + Model.costoPorImpresion[p] * Model.x[p] + Model.costoObjetivo[o] * Model.objetivo[o]

def porcHyN(i, n):
    return Model.porcentajeHablantes[i] * Model.idioma[i] * Model.porcentajeDentroDeNicho[n] * Model.nicho[n]
#Funcion Objetivo
Model.func_objetivo = Objective(expr = sum( Model.numeroHabitantes[p]*Model.x[p] * porcOyS(s) * porcHyN(i,n) * presupuesto * Model.costoPorImpresion[p]*Model.x[p] * (Model.costoObjetivo[o] * Model.objetivo[o]) * (Model.costoUbicacion[u] * Model.ubicacion[u])  for p in Model.paises for s in Model.sexos for i in Model.idiomas for n in Model.nichos for o in Model.objetivos for u in Model.ubicaciones), sense=maximize)

#Constraints

Model.canObjetivos = Constraint(expr = sum(Model.objetivo[o] for o in Model.objetivos) == 1)
Model.canSexos = Constraint(expr = sum(Model.sexo[s] for s in Model.sexos) == 1)
Model.canIdiomas = Constraint(expr = sum(Model.idioma[i] for i in Model.idiomas) == 1)
Model.canNicho = Constraint(expr = sum(Model.nicho[n] for n in Model.nichos) == 1)
Model.canUbicacion = Constraint(expr = sum(Model.ubicacion[u] for u in Model.ubicaciones) == 1)
Model.canPaises = Constraint(expr = sum(Model.x[p] for p in Model.paises) == 1)



#Solver
solver = SolverFactory('ipopt')
solver.options['max_iter']= 10000 #number of iterations you wish
solver.solve(Model)


Model.display()


