# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: aliqiva.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
from awc.controls.radiobox import RadioBox
from awc.controls.numctrl import NumCtrl

from anag.basetab import AnagCardPanel, WorkZoneNotebook, UnoZeroCheckBox


class ModoIvaRadioBox(RadioBox):

    def __init__(self, *args, **kwargs):
        RadioBox.__init__(self, *args, **kwargs)
        self.SetDataLink(values=["I", "N", "E", "F"])




# Window functions

ID_ANAGMAIN = 16000
ID_DATIALLEG = 16001

def AliqIvaCardFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = AnagCardPanel(parent)
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = WorkZoneNotebook( parent, ID_DATIALLEG, wx.DefaultPosition, [200,160], 0 )
    item2 = item3
    
    item4 = wx.Panel( item3, -1 )
    AliqIvaCardDatiFunc(item4, False)
    item3.AddPage( item4, "Dati" )

    item5 = wx.Panel( item3, -1 )
    AliqIvaCardAllegFunc(item5, False)
    item3.AddPage( item5, "Allegati" )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_TEXT = 16002
ID_PERCIVA = 16003
ID_PERCIND = 16004
ID_TIPO = 16005
ID_MODO = 16006
ID_SM11_NO = 16007

def AliqIvaCardDatiFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item2 = wx.StaticBox( parent, -1, "Percentuali di calcolo" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.FlexGridSizer( 0, 4, 0, 0 )
    
    item4 = wx.StaticText( parent, ID_TEXT, "Aliquota %:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item5 = NumCtrl( parent, integerWidth=3, fractionWidth=2, allowNegative=False, groupDigits=False); item5.SetName("perciva")
    item3.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "Indeducibilità %:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item7 = NumCtrl( parent, integerWidth=3, fractionWidth=2, allowNegative=False, groupDigits=False); item7.SetName("percind")
    item3.Add( item7, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item8 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item9 = RadioBox( parent, ID_TIPO, "Tipologia", wx.DefaultPosition, wx.DefaultSize, 
        ["Acquisti/Vendite","Acquisti CEE","Vendite in sospensione"] , 1, wx.RA_SPECIFY_COLS )
    item9.SetName( "tipo" )
    item8.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item10 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item11 = ModoIvaRadioBox( parent, ID_MODO, "L'importo assogettato a questa aliquota è:", wx.DefaultPosition, wx.DefaultSize, 
        ["Imponibile","Non Imponibile","Esente","Fuori Campo"] , 1, wx.RA_SPECIFY_COLS )
    item11.SetName( "modo" )
    item10.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item13 = wx.StaticBox( parent, -1, "Spesometro 2011" )
    item12 = wx.StaticBoxSizer( item13, wx.VERTICAL )
    
    item14 = UnoZeroCheckBox( parent, ID_SM11_NO, "Escludi dalla compilazione dello spesometro", wx.DefaultPosition, wx.DefaultSize, 0 )
    item14.SetName( "sm11_no" )
    item12.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item10.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item10.AddGrowableCol( 0 )

    item8.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item8.AddGrowableCol( 0 )

    item8.AddGrowableCol( 1 )

    item0.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_RADIOBOX = 16008

def AliqIvaCardAllegFunc( parent, call_fit = True, set_sizer = True ):
    item1 = wx.StaticBox( parent, -1, "Progressivi allegati clienti/fornitori" )
    item0 = wx.StaticBoxSizer( item1, wx.VERTICAL )
    
    item2 = wx.FlexGridSizer( 0, 5, 0, 0 )
    
    item3 = wx.StaticText( parent, ID_TEXT, "Clienti", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item3, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item4 = RadioBox( parent, ID_RADIOBOX, "Colonna 1", wx.DefaultPosition, wx.DefaultSize, 
        ["Nulla","Imponibile","Imposta"] , 1, wx.RA_SPECIFY_COLS )
    item4.SetName( "pralcc1" )
    item2.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = RadioBox( parent, ID_RADIOBOX, "Colonna 2", wx.DefaultPosition, wx.DefaultSize, 
        ["Nulla","Imponibile","Imposta"] , 1, wx.RA_SPECIFY_COLS )
    item5.SetName( "pralcc2" )
    item2.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item6 = RadioBox( parent, ID_RADIOBOX, "Colonna 3", wx.DefaultPosition, wx.DefaultSize, 
        ["Nulla","Imponibile","Imposta"] , 1, wx.RA_SPECIFY_COLS )
    item6.SetName( "pralcc3" )
    item2.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item7 = RadioBox( parent, ID_RADIOBOX, "Colonna 4", wx.DefaultPosition, wx.DefaultSize, 
        ["Nulla","Imponibile","Imposta"] , 1, wx.RA_SPECIFY_COLS )
    item7.SetName( "pralcc4" )
    item2.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item8 = wx.StaticText( parent, ID_TEXT, "Fornitori", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item8, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item9 = RadioBox( parent, ID_RADIOBOX, "Colonna 1", wx.DefaultPosition, wx.DefaultSize, 
        ["Nulla","Imponibile","Imposta"] , 1, wx.RA_SPECIFY_COLS )
    item9.SetName( "pralfc1" )
    item2.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item10 = RadioBox( parent, ID_RADIOBOX, "Colonna 2", wx.DefaultPosition, wx.DefaultSize, 
        ["Nulla","Imponibile","Imposta"] , 1, wx.RA_SPECIFY_COLS )
    item10.SetName( "pralfc2" )
    item2.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item11 = RadioBox( parent, ID_RADIOBOX, "Colonna 3", wx.DefaultPosition, wx.DefaultSize, 
        ["Nulla","Imponibile","Imposta"] , 1, wx.RA_SPECIFY_COLS )
    item11.SetName( "pralfc3" )
    item2.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item12 = RadioBox( parent, ID_RADIOBOX, "Colonna 4", wx.DefaultPosition, wx.DefaultSize, 
        ["Nulla","Imponibile","Imposta"] , 1, wx.RA_SPECIFY_COLS )
    item12.SetName( "pralfc4" )
    item2.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item2.AddGrowableCol( 1 )

    item2.AddGrowableCol( 2 )

    item2.AddGrowableCol( 3 )

    item2.AddGrowableCol( 4 )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
