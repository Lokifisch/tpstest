let TpsTester = 0
let TPs = 0
basic.forever(function () {
    TpsTester += 1
})
basic.forever(function () {
    basic.pause(1000)
    TPs = TpsTester
    TpsTester = 0
    basic.showString("" + (TPs))
})
