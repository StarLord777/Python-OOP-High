import win32com.client

speek = win32com.client.Dispatch('SAPI.SPVOICE')
for i in range(1000):
    speek.Speak('good good study')
    speek.Speak('day day up')
