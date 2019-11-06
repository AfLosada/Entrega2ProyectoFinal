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
Model.paises = RangeSet(1,numPaises)
Model.objetivos = RangeSet(1,numObjetivos)
Model.sexos = RangeSet(1,numSexos)
Model.idiomas = RangeSet(1,numIdiomas)
Model.edades = RangeSet(1,numEdades)
Model.nichos = RangeSet(1,numNichos)
Model.ubicaciones = RangeSet(1,numUbicaciones)

#Parametros

Model.numeroHabitantes = Param(Model.paises, mutable = True)
Model.costoObjetivo = Param(Model.objetivos, mutable = True)
Model.porcentajeSexo = Param(Model.sexos, mutable = True)
Model.porcentajeHablantes = Param(Model.idiomas, mutable = True)
Model.porcentajeDentroNicho = Param(Model.nichos, mutable = True)
Model.costoUbicacion = Param(Model.ubicaciones, mutable = True)
Model.costoPorImpresion = Param(Model.paises, mutable = True)

#variables

Model.objetivo = Var(Model.objetivos, domain=PositiveIntegers)
Model.sexo = Var(Model.sexos, domain=PositiveIntegers)
Model.idioma = Var(Model.idiomas, domain=PositiveIntegers)
Model.nicho = Var(Model.nichos, domain=PositiveIntegers)
Model.ubicacion = Var(Model.ubicaciones, domain=PositiveIntegers)

Model.x = Var(Model.paises, domain=Binary)
Model.y = Var(Model.sexos, domain=Binary)

pob = sqrt(-Model.numeroHabitantes[p]*Model.x[p] for p  )