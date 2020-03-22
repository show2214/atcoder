def LI(): return list(map(int, input().split()))

def calc(cards, alice, bob, is_alice):
    card = max(cards)
    if is_alice:
        alice += card
    else:
        bob += card
    cards.remove(card)
    if len(cards) != 0:
        return calc(cards, alice, bob, not is_alice)
    return alice - bob

if __name__ == "__main__":
    input()
    cards = LI()
    print(calc(cards, 0, 0, True))