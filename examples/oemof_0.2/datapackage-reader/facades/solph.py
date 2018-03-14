# -*- coding: utf-8 -*-
"""
"""
import os
import os.path

from oemof.solph import Bus, EnergySystem, Flow, Model, Sink
from oemof.solph.facades import Demand
from oemof.tools.datapackage import FLOW_TYPE


es = EnergySystem.from_datapackage(
    os.path.join(os.path.dirname(os.path.realpath(__file__)),
                 'datapackage_facades/datapackage.json'),
    attributemap={
        # Translations on `object` will be used every time, unless a more
        # specific translation is found.
        object: {"profiles": "profile"},
        Flow: {}},
    typemap={
        'demand': Sink,
        'bus': Bus, # DOES NOT WORK WITHOUT THIS, WHY!?
        FLOW_TYPE: Flow})


m = Model(es)