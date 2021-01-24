import wx
import converters as conv


class TempConverterInterface(wx.Frame):
    def __init__(self, parent, style, title):
        super().__init__(parent, style=style, title=title, size=(310, 200))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)
        hbox = wx.BoxSizer(wx.VERTICAL)

        fgs = wx.FlexGridSizer(rows=4, cols=2, vgap=10, hgap=15)

        temp_value = wx.StaticText(panel, label="Temperature Value: ")
        temp_value.SetFont(font)
        from_temp = wx.StaticText(panel, label="From: ")
        from_temp.SetFont(font)
        to_temp = wx.StaticText(panel, label="To: ")
        to_temp.SetFont(font)
        calc_button = wx.Button(panel, label="Calculate")
        calc_button.Bind(wx.EVT_BUTTON, self.on_press_calculate)
        self.result = wx.StaticText(panel, label='', pos=(10, 10))
        font.SetPointSize(14)
        self.result.SetFont(font)

        self.tc1 = wx.TextCtrl(panel)
        self.tc2_combo = wx.ComboBox(
            panel, choices=["°C", "°F", "K"], style=wx.CB_READONLY)
        self.tc3_combo = wx.ComboBox(
            panel, choices=["°C", "°F", "K"], style=wx.CB_READONLY)

        fgs.AddMany([(temp_value), (self.tc1, 1, wx.EXPAND), (from_temp),
                     (self.tc2_combo, 1, wx.EXPAND), (to_temp, 1,
                                                      wx.EXPAND), (self.tc3_combo, 1, wx.EXPAND), (calc_button),
                     (self.result, 1, wx.RIGHT)])

        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)

        panel.SetSizer(hbox)

    def ShowValueErrorMessage(self):
        wx.MessageBox('You entered an invalid value.', 'Value Error',
                      style=wx.OK | wx.ICON_ERROR)

    def ShowTypeErrorMessage(self):
        wx.MessageBox('Origin and final temperature units must be different.', 'Unit Type Error',
                      style=wx.OK | wx.ICON_ERROR)

    def on_press_calculate(self, event):
        try:
            self.result.Label = conv.temperature_converter(value=float(self.tc1.GetValue()),
                                                           convert_from=self.tc2_combo.GetValue(),
                                                           convert_to=self.tc3_combo.GetValue())
        except ValueError:
            self.ShowValueErrorMessage()
        except TypeError:
            self.ShowTypeErrorMessage()


def main():

    app = wx.App()
    frame = TempConverterInterface(None, style=wx.MINIMIZE_BOX |
                                   wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, title='Temperature Converter')
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
