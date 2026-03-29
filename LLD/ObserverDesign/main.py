from Observable.IphoneStockObservable import IphoneStockObservable
from Observer.EmailObserver import EmailObserver
from Observer.SmsObserver import SmsObserver

# Observable
iphoneObservable:IphoneStockObservable= IphoneStockObservable(0)

obsv1:EmailObserver=EmailObserver("abc@gmail.com",iphoneObservable)
obsv2:SmsObserver=SmsObserver("123456789",iphoneObservable)
iphoneObservable.addObserver(obsv1)
iphoneObservable.addObserver(obsv2)

iphoneObservable.setStockQuantity(15)