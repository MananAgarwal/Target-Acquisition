# Target-Acquisition
Python script which plots the ACQCENT (Measured) and ACQPREF (Desired) target position using the raw FITS files of ACQ/IMAGE type target acquisition from the COS/HST (Cosmic Origin Spectrograph / Hubble Space Telescope).

The script takes the name of the FITS file as a command line argument.

`$ python target_acquisition.py your_fits_file_rawacq.fits`

To run the script on all the files in a folder, use the following shell script inside that folder

`$ for f in *; do python target_acquisition.py $f; done`

Or you can use "target_acquisition_itr.py" to run plots the fits files in a directory. It takes the Directory name as a command line argument and outputs the plots as the location same as the python script

`$ python target_acquisition_itr.py your_dir_name`

## Example files
There are 4 combinations of the acquisition imaging modes. Those can be determined using the header keywords “EXPTYPE”, “APERTURE”, and “OPT_ELEM”. Example files for each of these modes are:

(exptype) (aperture) (opt_elem) : (filename)

ACQ/IMAGE PSA MIRRORA: ldqhpbhwq_rawacq.fits

ACQ/IMAGE PSA MIRRORB: ldvsbaymq_rawacq.fits

ACQ/IMAGE BOA MIRRORA: ldcv22wnq_rawacq.fits

ACQ/IMAGE BOA MIRRORB: ldcv03fyq_rawacq.fits
 
## SASP'19
This is part of my summer project the Space Telescope Science Institute (STScI), Baltimore as a SASP'19 intern. STScI is the science operations center for the Hubble Space Telescope (HST) and for the James Webb Space Telescope (JWST). It is operated for NASA by AURA.
