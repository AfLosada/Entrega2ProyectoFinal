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
numSexos = 3
numIdiomas = 2
numEdades = 6
numNichos = 3
numUbicaciones = 2

# Sets: cada entero representa un pais
paises = RangeSet(1,numPaises)
objetivos = RangeSet(1,numObjetivos)
sexos = RangeSet(1,numSexos)
idiomas = RangeSet(1,numIdiomas)
edades = RangeSet(1,numEdades)
nichos = RangeSet(1,numNichos)
ubicaciones = RangeSet(1,numUbicaciones)

#Parametros

numeroHabitantes = Param(paises, mutable = True)
costoObjetivo = Param(objetivos, mutable = True)
porcentajeSexo = Param(sexos, mutable = True)
porcentajeHablantes = Param(idiomas, mutable = True)
porcentajeDentroNicho = Param(nichos, mutable = True)
costoUbicacion = Param(ubicaciones, mutable = True)
costoPorImpresion = Param(paises, mutable = True)

#variables

Model.objetivo = Var(objetivos, domain=PositiveIntegers)
Model.sexo = Var(sexos, domain=PositiveIntegers)
Model.idioma = Var(idiomas, domain=PositiveIntegers)
Model.nicho = Var(nichos, domain=PositiveIntegers)
Model.ubicacion = Var(ubicaciones, domain=PositiveIntegers)

Model.x = Var(paises, domain=Binary)
Model.y = Var(sexos, domain=Binary)