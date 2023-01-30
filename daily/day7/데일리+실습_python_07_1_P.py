class Nationality:
    def __init__(self, nation):
        self.nation = nation


korea_nationality = Nationality("대한민국")
print(f'나의 국적은 {korea_nationality.nation}') # 나의 국적은 대한민국