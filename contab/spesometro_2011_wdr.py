# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: spesometro_2011.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
from awc.controls.linktable import LinkTable
from awc.controls.textctrl import TextCtrl
from awc.controls.datectrl import DateCtrl
from awc.controls.numctrl import NumCtrl
from awc.controls.checkbox import CheckBox, RCheckBox
from awc.controls.radiobox import RadioBox

import anag.lib as alib

from Env import Azienda
bt = Azienda.BaseTab

class AcquistiVenditeCorrispettiviRadioBox(RadioBox):
    def __init__(self, *args, **kwargs):
        RadioBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values=["A", "V", "C", "T"])



# Window functions

ID_ACQVENCOR = 10000
ID_TEXT = 10001
ID_ANNO = 10002
ID_DATA1 = 10003
ID_DATA2 = 10004
ID_SOLO_ALL = 10005
ID_LINE = 10006
ID_ESCLUDI_BLA = 10007
ID_ESCLUDI_BLS = 10008
ID_BUTUPDATE = 10009
ID_REGSPY = 10010
ID_GRIDPANEL = 10011
ID_TOTANADES = 10012
ID_TOTANAIMP = 10013
ID_TOTANAIVA = 10014
ID_TOTANATOT = 10015
ID_WARNING = 10016
ID_BUTESTRAI = 10017
ID_BUTGENERA = 10018

def SpesometroPanelFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item2 = AcquistiVenditeCorrispettiviRadioBox( parent, ID_ACQVENCOR, "Tipo", wx.DefaultPosition, wx.DefaultSize, 
        ["Acquisti","Vendite","Corrisp.","TUTTO"] , 1, wx.RA_SPECIFY_ROWS )
    item2.SetName( "acqvencor" )
    item1.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

    item4 = wx.StaticBox( parent, -1, "Periodo" )
    item3 = wx.StaticBoxSizer( item4, wx.VERTICAL )
    
    item5 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item6 = wx.StaticText( parent, ID_TEXT, "Anno:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item6, 0, wx.ALIGN_CENTER|wx.LEFT|wx.BOTTOM, 5 )

    item7 = NumCtrl(parent, ID_ANNO, integerWidth=4, fractionWidth=0, groupDigits=False); item7.SetName('anno')
    item5.Add( item7, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item8 = wx.StaticText( parent, ID_TEXT, "Registrazioni dal:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item8, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item9 = DateCtrl( parent, ID_DATA1, "", wx.DefaultPosition, [80,-1], 0 )
    item9.SetName( "data1" )
    item5.Add( item9, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item10 = wx.StaticText( parent, ID_TEXT, "al:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item10, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item11 = DateCtrl( parent, ID_DATA2, "", wx.DefaultPosition, [80,-1], 0 )
    item11.SetName( "data2" )
    item5.Add( item11, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item5.AddGrowableCol( 5 )

    item3.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item13 = wx.StaticBox( parent, -1, "Anagrafiche" )
    item12 = wx.StaticBoxSizer( item13, wx.VERTICAL )
    
    item14 = wx.CheckBox( parent, ID_SOLO_ALL, "Solo in allegato", wx.DefaultPosition, wx.DefaultSize, 0 )
    item14.SetValue( True )
    item14.SetName( "solo_all" )
    item12.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item15 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item12.Add( item15, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item16 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item17 = wx.StaticText( parent, ID_TEXT, "Escludi blacklist:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item16.Add( item17, 0, wx.ALIGN_CENTER|wx.RIGHT, 5 )

    item18 = wx.CheckBox( parent, ID_ESCLUDI_BLA, "Anagr.", wx.DefaultPosition, wx.DefaultSize, 0 )
    item18.SetValue( True )
    item18.SetName( "escludi_bla" )
    item16.Add( item18, 0, wx.ALIGN_CENTER, 5 )

    item19 = wx.CheckBox( parent, ID_ESCLUDI_BLS, "Stato", wx.DefaultPosition, wx.DefaultSize, 0 )
    item19.SetValue( True )
    item19.SetName( "escludi_bls" )
    item16.Add( item19, 0, wx.ALIGN_CENTER, 5 )

    item12.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item20 = wx.Button( parent, ID_BUTUPDATE, "Aggiorna", wx.DefaultPosition, wx.DefaultSize, 0 )
    item20.SetDefault()
    item20.SetName( "butupdate" )
    item1.Add( item20, 0, wx.ALIGN_RIGHT|wx.ALIGN_BOTTOM|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item21 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item22 = wx.StaticText( parent, ID_TEXT, "Elenco transazioni", wx.DefaultPosition, wx.DefaultSize, 0 )
    item22.SetForegroundColour( wx.BLUE )
    item22.SetName( "gridtitle" )
    item21.Add( item22, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item23 = RCheckBox( parent, ID_REGSPY, "Reg.Spy", wx.DefaultPosition, wx.DefaultSize, 0 )
    item23.SetName( "regspy" )
    item21.Add( item23, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item21.AddGrowableCol( 0 )

    item0.Add( item21, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item24 = wx.Panel( parent, ID_GRIDPANEL, wx.DefaultPosition, [900,300], wx.SUNKEN_BORDER )
    item24.SetName( "gridpanel" )
    item0.Add( item24, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item25 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item26 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item27 = wx.FlexGridSizer( 0, 4, 0, 0 )
    
    item28 = wx.StaticText( parent, ID_TEXT, "Anagrafica", wx.DefaultPosition, [400,-1], wx.ST_NO_AUTORESIZE )
    item27.Add( item28, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item29 = wx.StaticText( parent, ID_TEXT, "Tot.Operazioni", wx.DefaultPosition, [100,-1], wx.ST_NO_AUTORESIZE|wx.ALIGN_RIGHT )
    item27.Add( item29, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item30 = wx.StaticText( parent, ID_TEXT, "Tot.Imposta", wx.DefaultPosition, [100,-1], wx.ST_NO_AUTORESIZE|wx.ALIGN_RIGHT )
    item27.Add( item30, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item31 = wx.StaticText( parent, ID_TEXT, "Tot.Op.+IVA", wx.DefaultPosition, [100,-1], wx.ST_NO_AUTORESIZE|wx.ALIGN_RIGHT )
    item27.Add( item31, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item32 = wx.StaticText( parent, ID_TOTANADES, "-", wx.DefaultPosition, wx.DefaultSize, 0 )
    item32.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item32.SetName( "totanades" )
    item27.Add( item32, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item33 = wx.StaticText( parent, ID_TOTANAIMP, "0", wx.DefaultPosition, [100,-1], wx.ST_NO_AUTORESIZE|wx.ALIGN_RIGHT )
    item33.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item33.SetName( "totanaimp" )
    item27.Add( item33, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item34 = wx.StaticText( parent, ID_TOTANAIVA, "0", wx.DefaultPosition, [100,-1], wx.ST_NO_AUTORESIZE|wx.ALIGN_RIGHT )
    item34.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item34.SetName( "totanaiva" )
    item27.Add( item34, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item35 = wx.StaticText( parent, ID_TOTANATOT, "0", wx.DefaultPosition, [100,-1], wx.ST_NO_AUTORESIZE|wx.ALIGN_RIGHT )
    item35.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item35.SetName( "totanatot" )
    item27.Add( item35, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item26.Add( item27, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item36 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item26.Add( item36, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

    item37 = wx.StaticText( parent, ID_WARNING, "-", wx.DefaultPosition, wx.DefaultSize, 0 )
    item37.SetForegroundColour( wx.RED )
    item37.SetFont( wx.Font( 12, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item37.SetName( "warning" )
    item26.Add( item37, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item26.AddGrowableCol( 0 )

    item25.Add( item26, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item38 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item39 = wx.Button( parent, ID_BUTESTRAI, "&Estrai", wx.DefaultPosition, wx.DefaultSize, 0 )
    item39.SetName( "butestrai" )
    item39.Enable(False)
    item38.Add( item39, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item40 = wx.Button( parent, ID_BUTGENERA, "Genera file", wx.DefaultPosition, wx.DefaultSize, 0 )
    item40.SetName( "butgenera" )
    item38.Add( item40, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item25.Add( item38, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

    item25.AddGrowableCol( 0 )

    item0.Add( item25, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 2 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_CAUSALE = 10019
ID_DATREG = 10020
ID_NUMDOC = 10021
ID_DATDOC = 10022
ID_PANGRIDBODY = 10023

def RegSpyPanelFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item2 = wx.StaticText( parent, ID_TEXT, "Causale:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item2, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item3 = alib.LinkTableCauContab(parent, ID_CAUSALE, 'id_caus'); item3.Disable()
    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = wx.StaticText( parent, ID_TEXT, "Registrazione del:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item4, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item5 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item6 = DateCtrl( parent, ID_DATREG, "", wx.DefaultPosition, [80,-1], 0 )
    item6.SetName( "datreg" )
    item6.Enable(False)
    item5.Add( item6, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Documento num.:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item7, 0, wx.ALIGN_CENTER|wx.LEFT|wx.BOTTOM, 5 )

    item8 = TextCtrl( parent, ID_NUMDOC, "", wx.DefaultPosition, [80,-1], 0 )
    item8.SetName( "numdoc" )
    item8.Enable(False)
    item5.Add( item8, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item9 = wx.StaticText( parent, ID_TEXT, "del:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item9, 0, wx.ALIGN_CENTER|wx.LEFT|wx.BOTTOM, 5 )

    item10 = DateCtrl( parent, ID_DATDOC, "", wx.DefaultPosition, [80,-1], 0 )
    item10.SetName( "datdoc" )
    item10.Enable(False)
    item5.Add( item10, 0, wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item1.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.AddGrowableCol( 1 )

    item0.Add( item1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item11 = wx.StaticText( parent, ID_TEXT, "Contenuto della registrazione:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item11.SetForegroundColour( wx.BLUE )
    item0.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.TOP, 5 )

    item12 = wx.Panel( parent, ID_PANGRIDBODY, wx.DefaultPosition, [700,160], wx.SUNKEN_BORDER )
    item12.SetName( "pangridbody" )
    item0.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.AddGrowableCol( 0 )

    item0.AddGrowableRow( 2 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_RAGSOC = 10024
ID_COMUNE = 10025
ID_PROV = 10026
ID_CODFISC = 10027
ID_PIVA = 10028
ID_BUTGEN = 10029

def GeneraFileFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item2 = wx.StaticBox( parent, -1, "Dati del soggetto obbligato alla presentazione" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.StaticText( parent, ID_TEXT, "Denominazione:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.TOP, 5 )

    item4 = TextCtrl( parent, ID_RAGSOC, "", wx.DefaultPosition, [400,-1], 0 )
    item4.SetName( "ragsoc" )
    item1.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item5 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item6 = wx.StaticText( parent, ID_TEXT, "Comune:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Prov:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item7, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

    item8 = TextCtrl( parent, ID_COMUNE, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item8.SetName( "comune" )
    item5.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.BOTTOM, 5 )

    item9 = TextCtrl( parent, ID_PROV, "", wx.DefaultPosition, [40,-1], 0 )
    item9.SetName( "prov" )
    item5.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item5.AddGrowableCol( 0 )

    item1.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item10 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item11 = wx.StaticText( parent, ID_TEXT, "Cod.Fiscale:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item10.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item12 = wx.StaticText( parent, ID_TEXT, "P.IVA:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item10.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item13 = TextCtrl( parent, ID_CODFISC, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item13.SetName( "codfisc" )
    item10.Add( item13, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item14 = TextCtrl( parent, ID_PIVA, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item14.SetName( "piva" )
    item10.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item10.AddGrowableCol( 0 )

    item10.AddGrowableCol( 1 )

    item1.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.Add( item1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item15 = wx.Button( parent, ID_BUTGEN, "Genera file", wx.DefaultPosition, wx.DefaultSize, 0 )
    item15.SetName( "butgen" )
    item0.Add( item15, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
