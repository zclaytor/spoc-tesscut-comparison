#!/usr/bin/env python

import lightkurve as lk
import matplotlib.pyplot as plt

# Set target string
tic = "TIC25063200"

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
# Search for TESS-SPOC target pixel file
print("Downloading SPOC data")
sr = lk.search_targetpixelfile(tic, sector=1, author="tess-spoc")
spoc = sr.download()
spoc.plot(title=f"SPOC TPF for {tic}", ax=ax[0])

# Search for TESSCut TPF by either TIC ID or coordinates
print("Downloading TESSCut data")
sr = lk.search_tesscut(f"{spoc.ra} {spoc.dec}", sector=1)
#sr = lk.search_tesscut(tic, sector=1)
tesscut = sr.download(cutout_size=11)
tesscut.plot(title=f"TESSCut TPF for {tic}", ax=ax[1])

# Print WCS information
print("")
print("SPOC WCS:")
print(spoc.wcs)
print("")
print("TESSCut WCS:")
print(tesscut.wcs)

fig.tight_layout()
plt.show()
