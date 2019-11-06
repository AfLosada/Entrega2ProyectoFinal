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
nicho = Range(1,numNicho)
ubicaciones = Range(1,numUbicaciones)
