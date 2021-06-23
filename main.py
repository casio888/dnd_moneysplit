from moneypot import Moneypot

if __name__ == "__main__":
    m = Moneypot.from_string("100sp100cp")
    print(m.get_money(True))
