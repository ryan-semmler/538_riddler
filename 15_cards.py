# https://fivethirtyeight.com/features/525600-minutes-of-math/


def game(p_hand=[], o_hand=[], deck=list(range(1, 10))):
        """
        Determines whether the next player to move will win, when both players play optimally
        Returns bool
        """

	def reaches_total(hand, n=3, total=15):
		"""return bool, whether any n cards in hand add up to exactly total"""
		if n == 1:
			return total in hand
		if len(hand) >= n:
			if len(hand) == n:
				return sum(hand) == total
			if len(hand) - 1 == n:
				return sum(hand) - total in hand
			for card in hand:
				new_hand = list(hand)
				new_hand.remove(card)
				if reaches_total(new_hand, n - 1, total - card):
					return True
		return False

	if len(deck) == 1:
		return reaches_total(p_hand + deck)
	for card in deck:
		new_hand = list(p_hand)
		new_hand.append(card)
		if reaches_total(new_hand):
			return True
	results = []
	for card in deck:
		new_deck = list(deck)
		new_deck.remove(card)
		result = game(o_hand, new_hand, new_deck)
		if result is False:
			return True
		results.append(result)
	if all(item is True for item in results):
		return False


print(game())

