# Target interface expected by client
class PaymentGateway:
    def pay(self, amount: float) -> None:
        raise NotImplementedError

# Adaptee: legacy API we can't modify
class LegacyPayAPI:
    def make_payment(self, pennies: int) -> None:
        print(f"[LegacyPayAPI] processed {pennies} pennies")

# Adapter maps target to adaptee
class LegacyPayAdapter(PaymentGateway):
    def __init__(self, adaptee: LegacyPayAPI) -> None:
        self._adaptee = adaptee

    def pay(self, amount: float) -> None:
        pennies = int(round(amount * 100))
        self._adaptee.make_payment(pennies)

if __name__ == "__main__":
    gateway: PaymentGateway = LegacyPayAdapter(LegacyPayAPI())
    gateway.pay(12.34)
