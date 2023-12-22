from itertools import combinations, permutations
import math

def shapley_value_coalitions(players, coalition_values):
    n = len(players)
    shapley_values = {player: 0 for player in players}

    for player in players:
        player_value = 0


        for r in range(n):
            for S in combinations([p for p in players if p != player], r):
                S_with_player = tuple(sorted(list(S) + [player]))
                S = tuple(sorted(S))


                player_contribution = coalition_values.get(S_with_player, 0) - coalition_values.get(S, 0)


                weight = math.factorial(len(S)) * math.factorial(n - len(S) - 1) / math.factorial(n)


                player_value += weight * player_contribution

        shapley_values[player] = player_value

    return shapley_values

# Manually specified coalition values for case a
coalition_values_a = {
    (): 0,
    ('Xavier',): 0,
    ('Yvan',): 0,
    ('Zacharie',): 0,
    ('Xavier', 'Yvan'): 500,
    ('Xavier', 'Zacharie'): 500,
    ('Yvan', 'Zacharie'): 750,
    ('Xavier', 'Yvan', 'Zacharie'): 1000
}


coalition_values_b = {
    (): 0,
    ('Xavier',): 500,
    ('Yvan',): 500,
    ('Zacharie',): 0,
    ('Xavier', 'Yvan'): 1250,
    ('Xavier', 'Zacharie'): 750,
    ('Yvan', 'Zacharie'): 750,
    ('Xavier', 'Yvan', 'Zacharie'): 1250
}


players_b = {'Xavier': 8, 'Yvan': 8, 'Zacharie': 1}


players_a = {'Xavier': 3, 'Yvan': 4, 'Zacharie': 5}

shapley_values_manual_a = shapley_value_coalitions(players_a, coalition_values_a)
shapley_values_manual_a

print(shapley_values_manual_a)

shapley_values_manual_b = shapley_value_coalitions(players_b, coalition_values_b)
shapley_values_manual_b

print(shapley_values_manual_b)