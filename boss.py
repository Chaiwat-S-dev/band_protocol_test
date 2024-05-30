'''
Problem 1: Boss Baby's Revenge
Description:
Boss Baby, known for his cool and clever ways, deals with teasing from the neighborhood kids who shoot
water guns at his house. In response, Boss Baby seeks revenge by shooting at least one shot back, but only
if the kids have already shot at him first. As Boss Baby's assistant, your task is to check if Boss Baby has
sought revenge for every shot aimed at him at least once and hasn't initiated any shooting himself.
Input:
A string (S, 1 <= len(S) <= 1,000,000) containing characters 'S' and 'R', where 'S' represents a shot and 'R'
represents revenge. The string represents the sequence of events for one day.
Output:
Return "Good boy" if all shots have been revenged at least once and Boss Baby doesn't initiate any shots at
the neighborhood kids first. Return "Bad boy" if these conditions are not satisfied.
Note:
- Boss Baby doesn't need to shoot back before the next shots of the kids. He can shoot back whenever
he wants as long as he doesn't shoot first.
'''


def evaluate(count_hash: dict) -> bool:
    if count_hash["R"] and count_hash["S"]:
        count_hash["R"], count_hash["S"] = 0, 0
        return True
    else:
        count_hash["R"], count_hash["S"] = 0, 0
        return False

def main(text: str) -> str:
    count_hash = {
        "R": 0,
        "S": 0
    }
    initial = text[0]
    for idx, c in enumerate(text):
        if idx == 0 and c == "R":
            return "Bad boy"
        
        count_hash[c] += 1
        if c != initial and idx+1 < len(text) and text[idx+1] == initial:
            if evaluate(count_hash):
                initial = text[idx+1]
                continue
            else:
                return "Bad boy"

    if evaluate(count_hash):
        return "Good boy"
    else:
        return "Bad boy"

if __name__ == '__main__':
    print(f'Input srting which contain "R" or "S":')
    text = input().upper()
    eval_txt = True
    for char in text:
        if char not in ('R', 'S'):
            eval_txt = False
    if eval_txt:
        print(main(text))
    else:
        print(f'Message have some character not in "R", "S"')
    # print(main("SRSSRRR"))
    # print(main("RSSRR"))
    # print(main("SSSRRRRS"))
    # print(main("SRRSSR"))
    # print(main("SSRSRRR"))