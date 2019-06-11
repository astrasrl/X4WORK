# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: entries.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Custom source
import images

from awc.controls.textctrl import TextCtrl, TextCtrl_LC
from awc.controls.button import FlatBitmapButton

class HttpTextCtrl(TextCtrl_LC):
    def _OnFocusLost(self, event):
        TextCtrl_LC._OnFocusLost(self, event)
        v = self.GetValue() or ''
        if v:
            p = 'http://'
            if not v.lower().startswith(p):
                self.SetValue(p+v)


class SquaredFlatBitmapButton(FlatBitmapButton):
    
    def __init__(self, parent, id, bitmap):
        address_size = parent.FindWindowById(ID_ADDRESS).GetSize()
        size = (address_size[1], address_size[1])
        FlatBitmapButton.__init__(self, parent, id, bitmap, size=size)

# Window functions

ID_ADDRESS = 30000
ID_ACTION = 30001

def PhoneEntryFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item1 = TextCtrl_LC( parent, ID_ADDRESS, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_TAB )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2 = SquaredFlatBitmapButton(parent, ID_ACTION, images.getPhone20Bitmap())
    item0.Add( item2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def MailEntryFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item1 = TextCtrl_LC( parent, ID_ADDRESS, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_TAB )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2 = SquaredFlatBitmapButton(parent, ID_ACTION, images.getMail20Bitmap())
    item0.Add( item2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def FolderEntryFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item1 = TextCtrl_LC( parent, ID_ADDRESS, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_TAB )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2 = SquaredFlatBitmapButton(parent, ID_ACTION, images.getFolder20Bitmap())
    item0.Add( item2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def FileEntryFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item1 = TextCtrl_LC( parent, ID_ADDRESS, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_TAB )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2 = SquaredFlatBitmapButton(parent, ID_ACTION, images.getFolder20Bitmap())
    item0.Add( item2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def PartitaIvaEntryFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item1 = TextCtrl( parent, ID_ADDRESS, "", wx.DefaultPosition, [130,-1], wx.TE_PROCESS_TAB )
    item1.SetFont( wx.Font( 10, wx.MODERN, wx.NORMAL, wx.NORMAL ) )
    item1.SetName( "_piva" )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2 = SquaredFlatBitmapButton(parent, ID_ACTION, images.getEarth20Bitmap()); item2.SetToolTipString("Controllo online delle date\ndi inizio e fine attività")
    item0.Add( item2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_TEXT = 30002
ID_LINE = 30003
ID_BTNWEB = 30004
ID_BTNQUIT = 30005

def PartitaIvaAgEntrDateFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TEXT, " Verifica online della Partita IVA", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetForegroundColour( wx.BLUE )
    item1.SetBackgroundColour( wx.LIGHT_GREY )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item3 = wx.StaticText( parent, ID_TEXT, "Operatore IVA:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item3, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item4 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, [80,-1], wx.ST_NO_AUTORESIZE )
    item4.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item4.SetName( "operat" )
    item2.Add( item4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = wx.StaticText( parent, ID_TEXT, "Data inizio attività:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, [80,-1], wx.ST_NO_AUTORESIZE )
    item6.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item6.SetName( "datini" )
    item2.Add( item6, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Data fine attività:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item7, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item8 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, [80,-1], wx.ST_NO_AUTORESIZE )
    item8.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item8.SetName( "datend" )
    item2.Add( item8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item9 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item10 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item11 = wx.Button( parent, ID_BTNWEB, "Apri pagina WEB", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
    item11.SetName( "btnweb" )
    item10.Add( item11, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item12 = wx.Button( parent, ID_BTNQUIT, "Chiudi", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.SetName( "btnquit" )
    item10.Add( item12, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item10.AddGrowableCol( 1 )

    item0.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def CodiceFiscaleEntryFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item1 = TextCtrl( parent, ID_ADDRESS, "", wx.DefaultPosition, [140,-1], wx.TE_PROCESS_TAB )
    item1.SetFont( wx.Font( 10, wx.MODERN, wx.NORMAL, wx.NORMAL ) )
    item1.SetName( "_codfisc" )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def HttpEntryFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item1 = HttpTextCtrl( parent, ID_ADDRESS, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_TAB )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2 = SquaredFlatBitmapButton(parent, ID_ACTION, images.getWeb20Bitmap())
    item0.Add( item2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def XmppEntryFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 1, 0, 0, 0 )
    
    item1 = TextCtrl_LC( parent, ID_ADDRESS, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_TAB )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2 = SquaredFlatBitmapButton(parent, ID_ACTION, images.getJabber20Bitmap())
    item0.Add( item2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableCol( 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0


def CheckViesFunc( parent, call_fit = True, set_sizer = True ):
    item0 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item1 = wx.StaticText( parent, ID_TEXT, " Verifica online della Partita IVA", wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetForegroundColour( wx.BLUE )
    item1.SetBackgroundColour( wx.LIGHT_GREY )
    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item2 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item3 = wx.StaticText( parent, ID_TEXT, "Operatore IVA:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item3, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item4 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, [120,-1], wx.ST_NO_AUTORESIZE )
    item4.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.BOLD ) )
    item4.SetName( "operat" )
    item2.Add( item4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = wx.StaticText( parent, ID_TEXT, "Denominazione:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item6 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, [300,-1], 0 )
    item6.SetName( "rs" )
    item2.Add( item6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Indirizzo:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item2.Add( item7, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item8 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, [300,40], 0 )
    item8.SetName( "addr" )
    item2.Add( item8, 0, wx.GROW|wx.ALL, 5 )

    item2.AddGrowableRow( 3 )

    item0.Add( item2, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item9 = wx.StaticLine( parent, ID_LINE, wx.DefaultPosition, [20,-1], wx.LI_HORIZONTAL )
    item0.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item10 = wx.FlexGridSizer( 0, 2, 0, 0 )
    
    item11 = wx.Button( parent, ID_BTNWEB, "Apri pagina WEB", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
    item11.SetName( "btnweb" )
    item10.Add( item11, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM, 5 )

    item12 = wx.Button( parent, ID_BTNQUIT, "Chiudi", wx.DefaultPosition, wx.DefaultSize, 0 )
    item12.SetName( "btnquit" )
    item10.Add( item12, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.BOTTOM, 5 )

    item10.AddGrowableCol( 1 )

    item0.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item0.AddGrowableRow( 1 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

# Toolbar functions

# Bitmap functions


# End of generated file
