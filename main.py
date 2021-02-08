from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


'''
Questions to answer:
Best draft (actual point production for the season) - drafted team with highest point total by week 16
Best waiver wire transactions - players added outperformed players dropped
Best roster setter - plays the right players

Players who outperformed their draft position
'''

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    oauth = OAuth2(None, None, from_file='./secrets/private.json')
    gm = yfa.Game(oauth, 'nfl')
    LEAGUE_ID_2020 = gm.league_ids(2020)[0]
    lg = gm.to_league(LEAGUE_ID_2020)
    trades = lg.transactions('trade', '')
    waivers_add = lg.transactions('add','')
    waivers_drop = lg.transactions('drop','')