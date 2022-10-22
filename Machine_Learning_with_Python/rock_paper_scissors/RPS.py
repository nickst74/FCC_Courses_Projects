from random import choice

# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

# ideal responses
response = {
        'R': 'P',
        'P': 'S',
        'S': 'R'
    }

def compareMoves(pl, opp):
    if pl == opp:
        return 0
    elif response[opp] == pl:
        return 1
    else:
        return -1

# make the most unlikely move based on your previous guess
def unpredictableMove(
    player_history,
    player_freqs = [{
        'RR': 0,
        'RP': 0,
        'RS': 0,
        'PP': 0,
        'PR': 0,
        'PS': 0,
        'SS': 0,
        'SR': 0,
        'SP': 0
    }]):
    # update frequencies based on last move that we made
    if len(player_history) > 1:
        player_freqs[0][''.join(player_history[-2::])] += 1
        # find least probable move based on my past moves
        pref = player_history[-1]
        probs = []
        for next in response.keys():
            probs.append((player_freqs[0][pref + next], next))
        probs.sort()
        return response[response[probs[-1][1]]]
    elif len(player_history) == 0:
        for key in player_freqs[0].keys():
            player_freqs[0][key] = 0
    return choice(list(response.keys()))


# counter the most probable opponent move based on his two previous moves
def guessBasedOnOppSequence(
    opponent_history,
    opp_freqs = [{
        'RRR': 0,
        'PPP': 0,
        'SSS': 0,
        'RRP': 0,
        'RPR': 0,
        'PRR': 0,
        'RPP': 0,
        'PRP': 0,
        'PPR': 0,
        'RRS': 0,
        'RSR': 0,
        'SRR': 0,
        'RSS': 0,
        'SRS': 0,
        'SSR': 0,
        'PPS': 0,
        'PSP': 0,
        'SPP': 0,
        'PSS': 0,
        'SPS': 0,
        'SSP': 0,
        'RPS': 0,
        'RSP': 0,
        'PRS': 0,
        'PSR': 0,
        'SRP': 0,
        'SPR': 0
    }]):
    # update frequencies based on last move the opponent made
    if len(opponent_history) > 2:
        opp_freqs[0][''.join(opponent_history[-3::])] += 1
        
        pref = ''.join(opponent_history[-2::])
        probs = []
        for next in response.keys():
            probs.append((opp_freqs[0][pref + next], next))
        probs.sort()
        return response[probs[-1][1]]
    elif len(opponent_history) == 0:
        for key in opp_freqs[0].keys():
            opp_freqs[0][key] = 0
    return choice(list(response.keys()))


# cycle through choises with step of 2
# next guess wins the move that would beat your previous guess 
def cycleStep2(prev='R'):
    return response[response[prev]]


def player(prev_play,
            opponent_history=[],
            player_history=[],
            nums = [[0.1, 0.1, 0.1]],
            denums = [[0.1, 0.1, 0.1]],
            prev_guesses = [['S', 'S', 'S']]):
    # store previous opponent move
    if prev_play != '':
        opponent_history.append(prev_play)
    else:
        # if no previous move, reset states just in case
        opponent_history = []
        player_history = []
        nums[0] = [0.1, 0.1, 0.1]
        denums[0] = [0.1, 0.1, 0.1]
        prev_guesses[0] = ['S', 'S', 'S']
        prev_play = 'S'
    
    # calculate scores
    j_square = (len(opponent_history) + 1) ** 2
    nums[0] = [num + compareMoves(prev_guesses[0][idx], prev_play) * j_square for idx, num in enumerate(nums[0])]
    denums[0] = [denum + j_square for denum in denums[0]]
    scores = [num / denum for num, denum in zip(nums[0], denums[0])]

    # find new guesses (could add more strategies but these seem to work just fine for said opponents)
    prev_guesses[0][0] = cycleStep2('S' if player_history == [] else player_history[-1])
    prev_guesses[0][1] = guessBasedOnOppSequence(opponent_history)
    prev_guesses[0][2] = unpredictableMove(player_history)

    # pick best strategy based on scores
    guess = sorted(zip(scores, prev_guesses[0]))[-1][1]

    player_history.append(guess)
    return guess
