from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSPlotter
from pymatgen.electronic_structure.plotter import BSDOSPlotter
from pymatgen.io.vasp.outputs import Vasprun
import numpy as np



vaspout = Vasprun("/home/robert/Documents/new_MnFe2O4/Normal/New_cals/bands-mag/vasprun.xml", parse_projected_eigen=True)
bandstr = vaspout.get_band_structure(line_mode=True)

dosrun = Vasprun("/home/robert/Documents/new_MnFe2O4/Normal/New_cals/scf-mag/vasprun.xml")
dos = dosrun.complete_dos

bsdosplot = BSDOSPlotter(
    bs_projection="elements",
    dos_projection="elements",
)

plt = bsdosplot.get_plot(bandstr, dos=dos)
fig = plt.gcf()
ax = plt.gca()
cmap = plt.get_cmap("magma")


plt.show()