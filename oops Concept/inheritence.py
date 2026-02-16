from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self,amount : float):
        pass

class CreditCardPayment(Payment):
    def __init__(self,amount) -> None:
        self.amount = amount
    def pay(self,amount:float):
        print(f"Paying {amount} using credit card")

class PayPalPayment(Payment):
    def __init__(self,amount) -> None:
        self.amount = amount
    def pay(self,amount:float):
        print(f"Paying {amount} using Paypal ")   


def checkout(payment_obj: Payment amount: float):
    return payment_obj.pay(amount)
    
