class Payment:
    def __init__(self, amount):
        self.amount = amount
    def total_amount(self):
        pass

class CashPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)
    def total_amount(self):
        return self.amount + self.amount * 0.10 

class CreditCardPayment(Payment):
    def __init__(self, amount):
        super().__init__(amount)
    def total_amount(self):
        return self.amount + self.amount * 0.10 + self.amount * 0.02 

cash_payment = CashPayment(1000)
credit_card_payment = CreditCardPayment(1000)

print(f"Total amount for cash payment: {cash_payment.total_amount()}")
print(f"Total amount for credit card payment: {credit_card_payment.total_amount()}")
