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


paises = RangeSet(1,numPaises)
objetivos = RangeSet(1,numObjetivos)
sexos = Range(1,numSexos)
idiomas = Range(1,numIdiomas)
sexos = Range(1,numSexos)
edad = Range(1,numEdades)
nichos = Range(1,numNicho)
ubicaciones = Range(1,numUbicaciones)







#variables

Model.objetivo = Var(objetivos, domain=PositiveIntegers)
Model.sexo = Var(sexos, domain=PositiveIntegers)
Model.idioma = Var(idiomas, domain=PositiveIntegers)
Model.nicho = Var(nichos, domain=PositiveIntegers)
Model.ubicacion = Var(ubicaciones, domain=PositiveIntegers)

Model.x = Var(paises, domain=Binary)
Model.y = Var(sexos, domain=Binary)
