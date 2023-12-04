import pya
from pya import *
import SiEPIC
from SiEPIC.verification import layout_check
from SiEPIC.scripts import zoom_out
from SiEPIC.utils import get_technology_by_name
import os
import siepic_ebeam_pdk

# gds file to run verification on
gds_file = "ebeam_adiabatic_te1550.gds"

# load into layout
layout = pya.Layout()
layout.read(gds_file)

top_cell = layout.top_cell()


# set layout technology because the technology seems to be empty, and we cannot load the technology using TECHNOLOGY = get_technology() because this isn't GUI mode
# refer to line 103 in layout_check()
# tech = layout.technology()
# print("Tech:", tech.name)
layout.TECHNOLOGY = get_technology_by_name('EBeam')


# run verification
zoom_out(top_cell)

path = os.path.dirname(os.path.realpath(__file__))
filename = 'ebeam_adiabatic_te1550'

print('SiEPIC_EBeam_PDK: ebeam_adiabatic_te1550 - verification')
file_lyrdb = os.path.join(path,filename+'.lyrdb')
num_errors = layout_check(cell = top_cell, verbose=True, GUI=True, file_rdb=file_lyrdb)

print('SiEPIC_EBeam_PDK: ebeam_adiabatic_te1550 - done')


