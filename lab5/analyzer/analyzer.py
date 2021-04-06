class Analyzer:
    '''Анализатор почты'''

    def __init__(self, data):
        # Коэффициент спамера
        self._spammers_factor = 0.5
        # Статистические данные
        self._stats_data = {}
        for author, group in data:
            stat = {
                'messages': 0,
                'xdp': 0,
                'xdc': 0
            }
            for value in group:
                stat['messages'] += 1
                stat['xdp'] += float(value['X-DSPAM-Probability'])
                stat['xdc'] += float(value['X-DSPAM-Confidence'])

            self._stats_data[author] = stat

    spammers_factor = property()

    @spammers_factor.getter
    def spammers_factor(self):
        return self._spammers_factor

    @spammers_factor.setter
    def spammers_factor(self, value):
        if float(value) > 0.0:
            self._spammers_factor = float(value)

    @property
    def info(self):
        return self._stats_data

    @property
    def spammer_list(self):
        '''Получение списка спамеров'''
        spammers = []
        for author, stat in self._stats_data.items():
            if stat['xdp'] / stat['messages'] > self._spammers_factor:
                spammers.append(author)

        return spammers
