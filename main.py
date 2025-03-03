TpsTester = 0
TPs = 0

def on_forever():
    global TpsTester
    TpsTester += 1
basic.forever(on_forever)

def on_forever2():
    global TPs, TpsTester
    basic.pause(1000)
    TPs = TpsTester
    TpsTester = 0
    basic.show_string("" + str((TPs)))
basic.forever(on_forever2)
