#!/usr/bin/env python

import sys
import os
import math

# ensure that the kicad-footprint-generator directory is available
#sys.path.append(os.environ.get('KIFOOTPRINTGENERATOR'))  # enable package import from parent directory
#sys.path.append("D:\hardware\KiCAD\kicad-footprint-generator")  # enable package import from parent directory
sys.path.append(os.path.join(sys.path[0],"..","..","kicad_mod")) # load kicad_mod path
sys.path.append(os.path.join(sys.path[0],"..","..")) # load kicad_mod path
sys.path.append(os.path.join(sys.path[0],"..","tools")) # load kicad_mod path

from KicadModTree import *  # NOQA
from footprint_scripts_pin_headers import *  # NOQA




if __name__ == '__main__':
    # common settings
    # from https://multimedia.3m.com/mws/media/22268O/3mtm-100-in-4-wll-hdr-100x-100l-e-strt-cmpl-pin-ts0478.pdf
    # and  http://www.selecom.it/pdf/06din416.pdf
    # and  https://www.reboul.fr/storage/00003af6.pdf
    # and  http://www.oupiin.com/product_iii.html?c1=10&c2=54
    # and  http://www.assmann-wsw.com/fileadmin/catalogue/04_Multiflex_rev4-0.pdf
    # and  https://docs.google.com/spreadsheets/d/16SsEcesNF15N3Lb4niX7dcUr-NY5_MFPQhobNuNppn4/edit#gid=0

    rm=2.54
    ddrill=1
    pad=[1.7,1.7]
    singlecol_packwidth=2.54
    singlecol_packoffset=0
    angled_pack_width=2.54
    angled_pack_offset=1.5
    angled_pin_length=6
    angled_pin_width=0.64
    rmx_pad_offset=[1.655,2.525]
    rmx_pin_length=[2.54,3.6]
    pin_width=0.64
    single_pad_smd=[2.51,1.0]
    dual_pad_smd=[3.15,1.0]
    
    orientation='Vertical'
    body_width=8.8
    body_overlen=10.97
    body_offset=0
    mating_overlen=3.92
    wall_thickness=1.2
    notch_width=4.1
    latch_lengths = [0,6.5,9.5,12] # these values roughly represent the referenced parts with the latch open
    latch_width=4.4 # large enough to handle all referenced parts
    mh_ddrill=2.69
    mh_pad=[8,8] # 3M datasheet says 5/16" head
    mh_overlen=2.03
    mh_offset=rm/2
    mh_number='' # can be 'MP' to have connected mounting holes

    cols = 2
    for rows in [5,6,7,8,10,12,13,15,17,20,25,30,32]:
        for latch_len in latch_lengths:
            for mh_ddrill, mh_pad, mh_overlen in zip([0, mh_ddrill], [0, mh_pad], [0, mh_overlen]):
                makeIdcHeader(rows, cols, rm, rm, body_width,
                                    body_overlen, body_overlen, body_offset,
                                    ddrill, pad,
                                    mating_overlen, wall_thickness, notch_width,
                                    orientation,
                                    latch_len, latch_width,
                                    mh_ddrill, mh_pad, mh_overlen, mh_offset, mh_number,
                                    [], "${KISYS3DMOD}/Connector_IDC", "IDC-Header", "IDC header",
                                    [0, 0, 0], [1, 1, 1], [0, 0, 0])
    
    # common settings
    # from http://multimedia.3m.com/mws/media/330367O/3m-four-wall-header-2500-series-ts-0770.pdf
    # and  https://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=1761681&DocType=Customer+Drawing&DocLang=English
    # and  https://cdn.amphenol-icc.com/media/wysiwyg/files/drawing/75869.pdf
    # and  https://katalog.we-online.de/em/datasheet/6120xx21621.pdf
    # and  https://docs.google.com/spreadsheets/d/16SsEcesNF15N3Lb4niX7dcUr-NY5_MFPQhobNuNppn4/edit#gid=0
    
    orientation='Vertical'
    has_latch=False
    body_width=8.9
    body_overlen=5.1
    mating_overlen=3.91
    
    for rows in [3,4,5,6,7,8,10,12,13,15,17,20,25,30,32]:
        makeIdcHeader(rows, cols, rm, rm, body_width,
                            body_overlen, body_overlen, body_offset,
                            ddrill, pad,
                            mating_overlen, wall_thickness, notch_width,
                            orientation,
                            0, 0,
                            0, 0, 0, 0, 0,
                            [], "${KISYS3DMOD}/Connector_IDC", "IDC-Header", "IDC box header",
                            [0, 0, 0], [1, 1, 1], [0, 0, 0])

    # common settings
    # from http://multimedia.3m.com/mws/media/22504O/3mtm-100-in-loprof-hdr-100x-100strt-ra-4-wall-ts0818.pdf
    # and  https://b2b.harting.com/files/download/PRD/PDF_TS/09185XXX323_100154466DRW007A.pdf
    # and  http://suddendocs.samtec.com/prints/tst-1xx-xx-xx-x-xx-xx-mkt.pdf
    # and  https://katalog.we-online.de/em/datasheet/6120xx21721.pdf
    # and  https://cdn.amphenol-icc.com/media/wysiwyg/files/drawing/75867.pdf
    # and  https://docs.google.com/spreadsheets/d/16SsEcesNF15N3Lb4niX7dcUr-NY5_MFPQhobNuNppn4/edit#gid=0
    
    orientation='Horizontal'
    body_offset=4.38 # distance from pin 1 row to the closest edge of the plastic body
    
    for rows in [3,4,5,6,7,8,10,12,13,15,17,20,25,30,32]:
        makeIdcHeader(rows, cols, rm, rm, body_width,
                            body_overlen, body_overlen, body_offset,
                            ddrill, pad,
                            mating_overlen, wall_thickness, notch_width,
                            orientation,
                            0, 0,
                            0, 0, 0, 0, 0,
                            [], "${KISYS3DMOD}/Connector_IDC", "IDC-Header", "IDC box header",
                            [0, 0, 0], [1, 1, 1], [0, 0, 0])
