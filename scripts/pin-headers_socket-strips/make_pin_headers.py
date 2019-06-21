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
    # from http://katalog.we-online.de/em/datasheet/6130xx11121.pdf
    # and  http://katalog.we-online.de/em/datasheet/6130xx21121.pdf
    # and  http://katalog.we-online.de/em/datasheet/6130xx11021.pdf
    # and  http://katalog.we-online.de/em/datasheet/6130xx21021.pdf
    # and  https://cdn.harwin.com/pdfs/M20-877.pdf
    # and  https://cdn.harwin.com/pdfs/M20-876.pdf

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

    for cols in [1,2]:
        for rows in range(1,41):
            makePinHeadStraight(rows, cols, rm, rm, cols * singlecol_packwidth + singlecol_packoffset,
                                singlecol_packwidth / 2 + singlecol_packoffset,
                                singlecol_packwidth / 2 + singlecol_packoffset, ddrill, pad, [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header",
                                [0, 0, 0], [1, 1, 1], [0, 0, 0])
            makeBoxHeadStraight(rows, cols, rm, rm, cols * singlecol_packwidth + singlecol_packoffset,
                                singlecol_packwidth / 2 + singlecol_packoffset,
                                singlecol_packwidth / 2 + singlecol_packoffset, ddrill, pad, [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header",
                                [0, 0, 0], [1, 1, 1], [0, 0, 0])
            makePinHeadAngled(rows, cols, rm, rm, angled_pack_width, angled_pack_offset, angled_pin_length, angled_pin_width, ddrill, pad,
                              [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header", [0, 0, 0], [1, 1, 1], [0, 0, 0])
            if rows != 1 or cols == 2:
              if cols == 2:
                  makePinHeadStraightSMD(rows, cols, rm, rm, rmx_pad_offset[cols-1], rmx_pin_length[cols-1], pin_width, cols * singlecol_packwidth + singlecol_packoffset,
                                      singlecol_packwidth / 2 + singlecol_packoffset,
                                      singlecol_packwidth / 2 + singlecol_packoffset, dual_pad_smd,
                                         True, [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header",
                                         [0, 0, 0], [1, 1, 1], [0, 0, 0])
              if cols==1:
                  makePinHeadStraightSMD(rows, cols, rm, rm, rmx_pad_offset[cols-1], rmx_pin_length[cols-1], pin_width,
                                     cols * singlecol_packwidth + singlecol_packoffset,
                                     singlecol_packwidth / 2 + singlecol_packoffset,
                                     singlecol_packwidth / 2 + singlecol_packoffset, single_pad_smd,
                                     True, [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header",
                                     [0, 0, 0], [1, 1, 1], [0, 0, 0])
                  makePinHeadStraightSMD(rows, cols, rm, rm, rmx_pad_offset[cols-1], rmx_pin_length[cols-1], pin_width,
                                     cols * singlecol_packwidth + singlecol_packoffset,
                                     singlecol_packwidth / 2 + singlecol_packoffset,
                                     singlecol_packwidth / 2 + singlecol_packoffset, single_pad_smd,
                                     False, [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header",
                                     [0, 0, 0], [1, 1, 1], [0, 0, 0])

        # common settings
    # from http://multimedia.3m.com/mws/media/22448O/3m-four-wall-header-3000-series-100-x-100-ts-0772.pdf
    # and  http://www.selecom.it/pdf/06din416.pdf
    # and  https://www.reboul.fr/storage/00003af6.pdf
    # and  http://www.oupiin.com/product_iii.html?c1=10&c2=54
    # and  http://www.assmann-wsw.com/fileadmin/catalogue/04_Multiflex_rev4-0.pdf
    # and  https://docs.google.com/spreadsheets/d/16SsEcesNF15N3Lb4niX7dcUr-NY5_MFPQhobNuNppn4/edit#gid=0
    
    orientation='Vertical'
    latching = True
    body_width=8.8
    body_overlen=10.97
    body_offset=0
    mating_overlen=3.92
    wall_thickness=1.2
    notch_width=4.1
    latch_lengths = [0,6.5,9.5,12] # these values roughly represent the referenced parts with the latch open
    latch_width=4.4 # large enough to handle all referenced parts and measured empirically
    mh_ddrill=2.69
    mh_pad=[8,8] # 3M datasheet says 5/16" head
    mh_overlen=8.94
    mh_offset=1.02
    mh_number='' # can be 'MP' to have connected mounting holes

    cols = 2
    for rows in [5,6,7,8,10,12,13,15,17,20,25,30,32]:
        for latch_len in latch_lengths:
            for mh_ddrill, mh_pad, mh_overlen in zip([0, mh_ddrill], [[0,0], mh_pad], [0, mh_overlen]):
                makeIdcHeader(rows, cols, rm, rm, body_width,
                                    body_overlen, body_overlen, body_offset,
                                    ddrill, pad,
                                    mating_overlen, wall_thickness, notch_width,
                                    orientation, latching,
                                    latch_len, latch_width,
                                    mh_ddrill, mh_pad, mh_overlen, mh_offset, mh_number,
                                    [], "${KISYS3DMOD}/Connector_IDC", "IDC-Header", "IDC header",
                                    [0, 0, 0], [1, 1, 1], [0, 0, 0])
    
    # the above datasheets cover both horizontal and vertical
    # latches are assumed to hang off the PCB so they aren't included here
    # for this footprint the body outline is hard-coded into the script
    orientation='Horizontal'
    body_width=1.27+15.88 # 1.24 and 15.53 here and -1.24 below for simplified 3M 3000 outline
    body_offset=-1.27
    latch_len=0
    mh_overlen=5.905
    mh_offset=1.8
    
    for rows in [5,6,7,8,10,12,13,15,17,20,25,30,32]:
        for mh_ddrill, mh_pad, mh_overlen in zip([0, mh_ddrill], [[0,0], mh_pad], [0, mh_overlen]):
            makeIdcHeader(rows, cols, rm, rm, body_width,
                                body_overlen, body_overlen, body_offset,
                                ddrill, pad,
                                mating_overlen, wall_thickness, notch_width,
                                orientation, latching,
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
    latching = False
    has_latch=False
    body_width=8.9
    body_overlen=5.1
    body_offset=0
    mating_overlen=3.91
    
    for rows in [3,4,5,6,7,8,10,12,13,15,17,20,25,30,32]:
        makeIdcHeader(rows, cols, rm, rm, body_width,
                            body_overlen, body_overlen, body_offset,
                            ddrill, pad,
                            mating_overlen, wall_thickness, notch_width,
                            orientation, latching,
                            0, 0,
                            0, [0,0], 0, 0, 0,
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
                            orientation, latching,
                            0, 0,
                            0, [0,0], 0, 0, 0,
                            [], "${KISYS3DMOD}/Connector_IDC", "IDC-Header", "IDC box header",
                            [0, 0, 0], [1, 1, 1], [0, 0, 0])

    # From http://katalog.we-online.de/em/datasheet/6200xx11121.pdf
    # and  http://katalog.we-online.de/em/datasheet/6200xx21121.pdf
    # and  http://www.mouser.com/ds/2/4/page_280-282-24683.pdf
    # and  https://cdn.harwin.com/pdfs/M22-273.pdf
    # and  https://cdn.harwin.com/pdfs/M22-552.pdf

    rm=2.00
    ddrill=0.8
    pad=[1.35, 1.35]
    singlecol_packwidth=2.0
    singlecol_packoffset=0
    angled_pack_width=1.5
    angled_pack_offset=3-1.5
    angled_pin_length=4.2
    angled_pin_width=0.5
    rmx_pad_offset=[1.175,2.085]
    rmx_pin_length=[2.1,2.875]
    pin_width=0.5
    single_pad_smd=[2.35,0.85]
    dual_pad_smd=[2.58,1.0]
    for cols in [1, 2]:
        for rows in range(1, 41):
            makePinHeadStraight(rows, cols, rm, rm, cols * singlecol_packwidth + singlecol_packoffset,
                                singlecol_packwidth / 2 + singlecol_packoffset,
                                singlecol_packwidth / 2 + singlecol_packoffset, ddrill, pad, [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header",
                                [0, 0, 0], [1, 1, 1], [0, 0, 0])
            makePinHeadAngled(rows, cols, rm, rm, angled_pack_width, angled_pack_offset, angled_pin_length,
                              angled_pin_width, ddrill, pad,
                              [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header", [0, 0, 0], [1, 1, 1], [0, 0, 0])
            if rows != 1 or cols == 2:
              if cols == 2:
                  makePinHeadStraightSMD(rows, cols, rm, rm, rmx_pad_offset[cols-1], rmx_pin_length[cols-1], pin_width,
                                         cols * singlecol_packwidth + singlecol_packoffset,
                                         singlecol_packwidth / 2 + singlecol_packoffset,
                                         singlecol_packwidth / 2 + singlecol_packoffset, dual_pad_smd,
                                         True, [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header",
                                         [0, 0, 0], [1, 1, 1], [0, 0, 0])
              if cols == 1:
                  makePinHeadStraightSMD(rows, cols, rm, rm, rmx_pad_offset[cols-1], rmx_pin_length[cols-1], pin_width,
                                         cols * singlecol_packwidth + singlecol_packoffset,
                                         singlecol_packwidth / 2 + singlecol_packoffset,
                                         singlecol_packwidth / 2 + singlecol_packoffset, single_pad_smd,
                                         True, [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header",
                                         [0, 0, 0], [1, 1, 1], [0, 0, 0])
                  makePinHeadStraightSMD(rows, cols, rm, rm, rmx_pad_offset[cols-1], rmx_pin_length[cols-1], pin_width,
                                         cols * singlecol_packwidth + singlecol_packoffset,
                                         singlecol_packwidth / 2 + singlecol_packoffset,
                                         singlecol_packwidth / 2 + singlecol_packoffset, single_pad_smd,
                                         False, [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header",
                                         [0, 0, 0], [1, 1, 1], [0, 0, 0])

    # From https://cdn.harwin.com/pdfs/M50-393.pdf
    # https://cdn.harwin.com/pdfs/M50-363.pdf
    # https://cdn.harwin.com/pdfs/M50-353.pdf
    # https://cdn.harwin.com/pdfs/M50-360.pdf
    # and http://www.mouser.com/ds/2/181/M50-360R-1064294.pdfs
    rm = 1.27
    ddrill = 0.65
    pad = [1.0, 1.0]
    package_width=[2.1,3.41]
    singlecol_packwidth = 1.27
    angled_pack_width=1.0
    angled_pack_offset=0.5
    angled_pin_length=4.0
    angled_pin_width=0.4
    rmx_pad_offset=[1.5,1.95]
    rmx_pin_length=[2.5, 2.75]
    pin_width=0.4
    single_pad_smd=[3.0,0.65]
    dual_pad_smd=[2.4,0.74]
    for cols in [1, 2]:
        for rows in range(1, 41):
            makePinHeadStraight(rows, cols, rm, rm, package_width[cols-1],
                                singlecol_packwidth / 2 ,
                                singlecol_packwidth / 2 , ddrill, pad, [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header",
                                [0, 0, 0], [1, 1, 1], [0, 0, 0])
            makePinHeadAngled(rows, cols, rm, rm, angled_pack_width, angled_pack_offset, angled_pin_length,
                              angled_pin_width, ddrill, pad,
                              [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header", [0, 0, 0], [1, 1, 1], [0, 0, 0])
            if rows != 1 or cols == 2:
                if cols == 2:
                    makePinHeadStraightSMD(rows, cols, rm, rm, rmx_pad_offset[cols-1], rmx_pin_length[cols-1], pin_width,
                                           package_width[cols-1],
                                           singlecol_packwidth / 2 + singlecol_packoffset,
                                           singlecol_packwidth / 2 + singlecol_packoffset, dual_pad_smd,
                                           True, [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header",
                                           [0, 0, 0], [1, 1, 1], [0, 0, 0])
                if cols == 1:
                    makePinHeadStraightSMD(rows, cols, rm, rm, rmx_pad_offset[cols-1], rmx_pin_length[cols-1], pin_width,
                                           package_width[cols-1],
                                           singlecol_packwidth / 2 + singlecol_packoffset,
                                           singlecol_packwidth / 2 + singlecol_packoffset, single_pad_smd,
                                           True, [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header",
                                           [0, 0, 0], [1, 1, 1], [0, 0, 0])
                    makePinHeadStraightSMD(rows, cols, rm, rm, rmx_pad_offset[cols-1], rmx_pin_length[cols-1], pin_width,
                                           package_width[cols-1],
                                           singlecol_packwidth / 2 + singlecol_packoffset,
                                           singlecol_packwidth / 2 + singlecol_packoffset, single_pad_smd,
                                           False, [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header",
                                           [0, 0, 0], [1, 1, 1], [0, 0, 0])
    #single row THT Straight headers https://gct.co/pdfjs/web/viewer.html?file=/Files/Drawings/BC020.pdf&t=1502019369628
    #dual row THT Straight headers https://gct.co/files/drawings/bc035.pdf
    #single row THT Angled headers https://gct.co/pdfjs/web/viewer.html?file=/Files/Drawings/BC030.pdf&t=1502031327147
    #dual row THT Angled headers https://gct.co/files/drawings/bc045.pdf
    #single row SMD Straight headers http://www.farnell.com/datasheets/1912818.pdf?_ga=2.101918145.1303212991.1501602361-984110936.1498471838
    #dual row SMD Straight headers https://gct.co/files/drawings/bc050.pdf
    rm = 1.0
    ddrill = 0.5
    pad = [0.85, 0.85]
    package_width=[1.27,2.3]
    singlecol_packwidth = 1.00
    angled_pack_width=[1.0, 1.2]
    angled_pack_offset= [0.25, 0.9]
    angled_pin_length=2.0
    angled_pin_width=0.3
    rmx_pad_offset=[0.875, 1.65]
    rmx_pin_length=[1.25, 2.4]
    pin_width=0.3
    single_pad_smd=[1.75,0.6]
    dual_pad_smd=[2.0,0.5]
    for cols in [1, 2]:
        for rows in range(1, 41):
            makePinHeadStraight(rows, cols, rm, rm, package_width[cols-1],
                                singlecol_packwidth / 2 ,
                                singlecol_packwidth / 2 , ddrill, pad, [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header",
                                [0, 0, 0], [1, 1, 1], [0, 0, 0])
            makePinHeadAngled(rows, cols, rm, rm, angled_pack_width[cols-1], angled_pack_offset[cols-1], angled_pin_length,
                              angled_pin_width, ddrill, pad,
                              [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header", [0, 0, 0], [1, 1, 1], [0, 0, 0])
            
            if rows != 1 or cols == 2:
                if cols == 2:
                    makePinHeadStraightSMD(rows, cols, rm, rm, rmx_pad_offset[cols-1], rmx_pin_length[cols-1], pin_width,
                                           package_width[cols-1],
                                           singlecol_packwidth / 2 + singlecol_packoffset,
                                           singlecol_packwidth / 2 + singlecol_packoffset, dual_pad_smd,
                                           True, [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header",
                                           [0, 0, 0], [1, 1, 1], [0, 0, 0])
                
                if cols == 1:
                    makePinHeadStraightSMD(rows, cols, rm, rm, rmx_pad_offset[cols-1], rmx_pin_length[cols-1], pin_width,
                                           package_width[cols-1],
                                           singlecol_packwidth / 2 + singlecol_packoffset,
                                           singlecol_packwidth / 2 + singlecol_packoffset, single_pad_smd,
                                           True, [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header",
                                           [0, 0, 0], [1, 1, 1], [0, 0, 0])
                    makePinHeadStraightSMD(rows, cols, rm, rm, rmx_pad_offset[cols-1], rmx_pin_length[cols-1], pin_width,
                                           package_width[cols-1],
                                           singlecol_packwidth / 2 + singlecol_packoffset,
                                           singlecol_packwidth / 2 + singlecol_packoffset, single_pad_smd,
                                           False, [], "${KISYS3DMOD}/Pin_Headers", "Pin_Header", "pin header",
                                           [0, 0, 0], [1, 1, 1], [0, 0, 0])
