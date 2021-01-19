# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    oauth = OAuth2(None, None, from_file='./secrets/private.json')
    gm = yfa.Game(oauth, 'nfl')
    gm.league_ids(2020)