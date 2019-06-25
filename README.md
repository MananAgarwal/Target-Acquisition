# Target-Acquisition
Python script which plots the ACQCENT (Measured) and ACQPREF (Desired) target position using the raw FITS files of ACQ/IMAGE type target acquisition from the COS/HST (Cosmic Origin Spectrograph / Hubble Space Telescope).

The script takes the name of the FITS file as a command line argument.

`$ python target_acquisition.py your_fits_file_rawacq.fits`

To run the script on all the files in a folder, use the following shell script inside that folder

`$ for f in *; do python target_acquisition.py $f; done`

This is part of my summer project the Space Telescope Science Institute (STScI), Baltimore as a SASP'19 intern. STScI is the science operations center for the Hubble Space Telescope (HST) and for the James Webb Space Telescope (JWST). It is operated for NASA by AURA.
