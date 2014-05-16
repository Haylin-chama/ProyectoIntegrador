#Boa:Frame:MTransportes

import wx
import wx.lib.masked.timectrl
import wx.lib.masked.textctrl
from wx.lib.anchors import LayoutAnchors

def create(parent):
    return MTransportes(parent)

[wxID_MTRANSPORTES, wxID_MTRANSPORTESBTBICI, wxID_MTRANSPORTESBTCAMINAR, 
 wxID_MTRANSPORTESBTCOLETO, wxID_MTRANSPORTESBTENVIAR, wxID_MTRANSPORTESBTMS, 
 wxID_MTRANSPORTESBTNINGUNO, wxID_MTRANSPORTESBTPCOLETO, 
 wxID_MTRANSPORTESBTPMS, wxID_MTRANSPORTESBTPTAXI, wxID_MTRANSPORTESBTPTS, 
 wxID_MTRANSPORTESBTR, wxID_MTRANSPORTESBTSALIR, wxID_MTRANSPORTESBTTAXI, 
 wxID_MTRANSPORTESBTTS, wxID_MTRANSPORTESBTVP, wxID_MTRANSPORTESPAGUNO, 
 wxID_MTRANSPORTESPANEL1, wxID_MTRANSPORTESPANEL2, wxID_MTRANSPORTESPANEL3, 
 wxID_MTRANSPORTESSTMT, wxID_MTRANSPORTESSTMTRANSPORTES, wxID_MTRANSPORTESSTP, 
 wxID_MTRANSPORTESSTTV, wxID_MTRANSPORTESTIMECTRL1, 
] = [wx.NewId() for _init_ctrls in range(25)]

class MTransportes(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MTRANSPORTES, name=u'MTransportes',
              parent=prnt, pos=wx.Point(668, 25), size=wx.Size(400, 700),
              style=wx.TRANSPARENT_WINDOW | wx.DEFAULT_FRAME_STYLE,
              title=u'Medios de Transportes')
        self.SetClientSize(wx.Size(392, 669))
        self.SetBackgroundColour(wx.Colour(213, 255, 213))
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Center(wx.HORIZONTAL)
        self.SetCursor(wx.CROSS_CURSOR)
        self.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Palatino Linotype'))
        self.SetForegroundColour(wx.Colour(0, 128, 0))
        self.SetHelpText(u'Programa para ingresar datos previamente recopilados.')
        self.SetToolTipString(u'Frame1')

        self.btSalir = wx.Button(id=wxID_MTRANSPORTESBTSALIR, label=u'Salir',
              name=u'btSalir', parent=self, pos=wx.Point(296, 632),
              size=wx.Size(75, 28), style=0)
        self.btSalir.Bind(wx.EVT_BUTTON, self.OnBtSalirButton,
              id=wxID_MTRANSPORTESBTSALIR)

        self.PagUno = wx.Panel(id=wxID_MTRANSPORTESPAGUNO, name=u'PagUno',
              parent=self, pos=wx.Point(21, 15), size=wx.Size(350, 607),
              style=wx.TAB_TRAVERSAL)
        self.PagUno.Center(wx.HORIZONTAL)

        self.btR = wx.Button(id=wxID_MTRANSPORTESBTR, label=u'Reiniciar',
              name=u'btR', parent=self, pos=wx.Point(24, 632), size=wx.Size(75,
              28), style=0)
        self.btR.Bind(wx.EVT_BUTTON, self.OnBtRButton, id=wxID_MTRANSPORTESBTR)

        self.stMTransportes = wx.StaticText(id=wxID_MTRANSPORTESSTMTRANSPORTES,
              label=u'Medios de Transporte', name=u'stMTransportes',
              parent=self.PagUno, pos=wx.Point(48, 8), size=wx.Size(252, 36),
              style=0)
        self.stMTransportes.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Palatino Linotype'))
        self.stMTransportes.SetForegroundColour(wx.Colour(0, 128, 255))

        self.panel1 = wx.Panel(id=wxID_MTRANSPORTESPANEL1, name='panel1',
              parent=self.PagUno, pos=wx.Point(8, 48), size=wx.Size(328, 200),
              style=wx.TAB_TRAVERSAL)

        self.stMT = wx.StaticText(id=wxID_MTRANSPORTESSTMT,
              label=u'1. \xbfQue medio de transporte usa?', name=u'stMT',
              parent=self.panel1, pos=wx.Point(24, 8), size=wx.Size(195, 18),
              style=0)

        self.btTS = wx.RadioButton(id=wxID_MTRANSPORTESBTTS,
              label=u'TranSantiago', name=u'btTS', parent=self.panel1,
              pos=wx.Point(40, 32), size=wx.Size(100, 18), style=0)
        self.btTS.SetValue(True)
        self.btTS.Bind(wx.EVT_RADIOBUTTON, self.OnRadioButton1Radiobutton,
              id=wxID_MTRANSPORTESBTTS)

        self.btMS = wx.RadioButton(id=wxID_MTRANSPORTESBTMS,
              label=u'Metro de Santiago', name=u'btMS', parent=self.panel1,
              pos=wx.Point(40, 56), size=wx.Size(128, 18), style=0)
        self.btMS.SetValue(True)

        self.btColeto = wx.RadioButton(id=wxID_MTRANSPORTESBTCOLETO,
              label=u'Colectivo', name=u'btColeto', parent=self.panel1,
              pos=wx.Point(40, 80), size=wx.Size(100, 18), style=0)
        self.btColeto.SetValue(True)

        self.btTaxi = wx.RadioButton(id=wxID_MTRANSPORTESBTTAXI, label=u'Taxi',
              name=u'btTaxi', parent=self.panel1, pos=wx.Point(40, 104),
              size=wx.Size(100, 18), style=0)
        self.btTaxi.SetValue(True)

        self.btVP = wx.RadioButton(id=wxID_MTRANSPORTESBTVP,
              label=u'Vehiculo Particular', name=u'btVP', parent=self.panel1,
              pos=wx.Point(40, 128), size=wx.Size(136, 18), style=0)
        self.btVP.SetValue(True)

        self.btBici = wx.RadioButton(id=wxID_MTRANSPORTESBTBICI,
              label=u'Bicicleta', name=u'btBici', parent=self.panel1,
              pos=wx.Point(40, 152), size=wx.Size(100, 18), style=0)
        self.btBici.SetValue(True)

        self.btCaminar = wx.RadioButton(id=wxID_MTRANSPORTESBTCAMINAR,
              label=u'Camino (No uso)', name=u'btCaminar', parent=self.panel1,
              pos=wx.Point(40, 176), size=wx.Size(128, 18), style=0)
        self.btCaminar.SetValue(True)

        self.panel2 = wx.Panel(id=wxID_MTRANSPORTESPANEL2, name='panel2',
              parent=self.PagUno, pos=wx.Point(16, 352), size=wx.Size(312, 156),
              style=wx.TAB_TRAVERSAL)

        self.stP = wx.StaticText(id=wxID_MTRANSPORTESSTP,
              label=u'3. \xbfQue medio de transporte publico prefiere?',
              name=u'stP', parent=self.panel2, pos=wx.Point(16, 16),
              size=wx.Size(268, 18), style=0)

        self.btPTS = wx.RadioButton(id=wxID_MTRANSPORTESBTPTS,
              label=u'TranSantiago', name=u'btPTS', parent=self.panel2,
              pos=wx.Point(40, 40), size=wx.Size(100, 18), style=0)
        self.btPTS.SetValue(True)

        self.btPMS = wx.RadioButton(id=wxID_MTRANSPORTESBTPMS,
              label=u'Metro de Santiago', name=u'btPMS', parent=self.panel2,
              pos=wx.Point(40, 64), size=wx.Size(100, 18), style=0)
        self.btPMS.SetValue(False)

        self.btPColeto = wx.RadioButton(id=wxID_MTRANSPORTESBTPCOLETO,
              label=u'Colectivo', name=u'btPColeto', parent=self.panel2,
              pos=wx.Point(40, 88), size=wx.Size(100, 18), style=0)
        self.btPColeto.SetValue(True)

        self.btPTaxi = wx.RadioButton(id=wxID_MTRANSPORTESBTPTAXI,
              label=u'Taxi', name=u'btPTaxi', parent=self.panel2,
              pos=wx.Point(40, 112), size=wx.Size(100, 18), style=0)
        self.btPTaxi.SetValue(True)

        self.btNinguno = wx.RadioButton(id=wxID_MTRANSPORTESBTNINGUNO,
              label=u'Ninguno', name=u'btNinguno', parent=self.panel2,
              pos=wx.Point(40, 136), size=wx.Size(100, 18), style=0)
        self.btNinguno.SetValue(False)

        self.btEnviar = wx.Button(id=wxID_MTRANSPORTESBTENVIAR,
              label=u'Enviar>>', name=u'btEnviar', parent=self.PagUno,
              pos=wx.Point(136, 568), size=wx.Size(75, 28), style=0)

        self.panel3 = wx.Panel(id=wxID_MTRANSPORTESPANEL3, name='panel3',
              parent=self.PagUno, pos=wx.Point(27, 271), size=wx.Size(200, 64),
              style=wx.TAB_TRAVERSAL)
        self.panel3.Center(wx.VERTICAL)

        self.stTV = wx.StaticText(id=wxID_MTRANSPORTESSTTV,
              label=u'2. Tiempo de Viaje', name=u'stTV', parent=self.panel3,
              pos=wx.Point(8, 8), size=wx.Size(109, 18), style=0)

        self.timeCtrl1 = wx.lib.masked.timectrl.TimeCtrl(display_seconds=True,
              fmt24hr=False, id=wxID_MTRANSPORTESTIMECTRL1, name='timeCtrl1',
              oob_color=wx.NamedColour('Yellow'), parent=self.panel3,
              pos=wx.Point(24, 32), size=wx.Size(72, 24), style=0,
              useFixedWidthFont=True, value='12:00:00 AM')

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        event.Skip()

    def OnRadioButton1Radiobutton(self, event):
        event.Skip()

    def OnBtSalirButton(self, event):
        self.Close()
        event.Skip()

    def OnBtRButton(self, event):
        #Reseteocompleto
        event.Skip()
