import pya
from pya import *
import SiEPIC
from SiEPIC.verification import layout_check
from SiEPIC.scripts import zoom_out
from SiEPIC.utils import get_technology_by_name
import os
import siepic_ebeam_pdk
import sys


# Print all command-line arguments for debugging
print("Command-line arguments:", sys.argv)

# Check the length of sys.argv to avoid "list index out of range" issues
if len(sys.argv) > 1:
    gds_file = sys.argv[1]
    print("GDS File:", gds_file)
    
    # Your script logic here using gds_file
else:
    print("Error: No command-line argument provided for GDS file.")

# gds file to run verification on
#gds_file = "ebeam_adiabatic_te1550.gds"
#gds_file = os.environ.get('GDS_FILE')
gds_file = sys.argv[1]

print("Gds file:", gds_file)

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
# filename = str(gds_file)

print('SiEPIC_EBeam_PDK: {} - verification'.format(gds_file))
file_lyrdb = os.path.join(path,gds_file+'.lyrdb')
num_errors = layout_check(cell = top_cell, verbose=True, GUI=True, file_rdb=file_lyrdb)

print('SiEPIC_EBeam_PDK: {} - done'.format(gds_file))

# Print the result value to standard output
print(f"::set-output name=result::{num_errors}")


