# PlayersStats/Normal/midfielder.py

from ..player import Player

class Midfielder(Player):
    def __init__(self):
        super().__init__('Midfielder')

    def get_stat_config(self):
        stat_config = super().get_stat_config()

        # Midfielder-specific adjustments
        stat_config['Playmaking']['Creative'] = {'mean': 65, 'std_dev': 4}
        stat_config['Playmaking']['Passing'] = {'mean': 65, 'std_dev': 4}
        stat_config['Playmaking']['Crossing'] = {'mean': 65, 'std_dev': 4}

        stat_config['Attack']['Finishing'] = {'mean': 50, 'std_dev': 4}
        stat_config['Attack']['Long Shots'] = {'mean': 60, 'std_dev': 4}
        stat_config['Attack']['Off The Ball'] = {'mean': 55, 'std_dev': 4}

        return stat_config