from __future__ import absolute_import
from getcpus import getcpus

option_list = ( ( 'machine', 'NCPU', int, getcpus() ),
                ( 'image', 'pbimage', str, 'image_full_ampphase_di_m.NS_shift.int.facetRestored.fits', 'PB-corrected image to use for source finding' ),
                ( 'image', 'nonpbimage', str, 'image_full_ampphase_di_m.NS_shift.app.facetRestored.fits', 'PB-uncorrected image to use for source finding' ),
                ( 'image', 'catprefix', str, 'image_full_ampphase_di_m.NS', 'Prefix to use for output catalogues' ),
                ( 'control', 'sfind_pixel_fraction', float, 1.0, 'Source find over what fraction of the image?' ),
                ( 'control', 'fit_sourcecounts', bool, True),
                ( 'control', 'quiet', bool, False ),
                ( 'control', 'logging', str, 'logs' ),
                ( 'control', 'dryrun', bool, False ),
                ( 'control', 'restart', bool, True ),
                ( 'pybdsm', 'atrous', bool, True ),
                ( 'comparison_cats', 'dir', str, '.' ),
                ( 'comparison_cats', 'list', list, None ),
                ( 'comparison_cats', 'filenames', list, None),
                ( 'comparison_cats', 'radii', list, None),
                ( 'comparison_cats', 'fluxfactor', list, None),
                ( 'comparison_cats', 'TGSS', str, None ),
                ( 'comparison_cats', 'TGSS_matchrad', float, 10.0 ),
                ( 'comparison_cats', 'TGSS_match_majkey1', float, 'Maj_1' ),
                ( 'comparison_cats', 'TGSS_match_majkey2', float, 'Maj_2' ),
                ( 'comparison_cats', 'TGSS_filtersize', float, 40.0 ),
                ( 'comparison_cats', 'TGSS_fluxfactor', float, 1000.0 ),
                ( 'comparison_cats', 'FIRST', str, None ),
                ( 'comparison_cats', 'FIRST_matchrad', float, 10.0 ),
                ( 'comparison_cats', 'FIRST_match_majkey1', float, 'Maj' ),
                ( 'comparison_cats', 'FIRST_match_majkey2', float, 'MAJOR' ),
                ( 'comparison_cats', 'FIRST_filtersize', float, 10.0 ),
                ( 'comparison_cats', 'FIRST_fluxfactor', float, 1.0 ) )
