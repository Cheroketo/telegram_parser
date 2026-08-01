import requests as req
headlines_dict = {'x-application-token':'lHwxOYbbKyDx0qFPo6D7mCRBM6slPcDV', 'x-platform':'widget', 'x-preferred-language':'ru'}



def get_playbill(date):
    url = f'https://kinokassa.kinoplan24.ru/api/v2/release/playbill?city_id=173&date={date}'
    response = req.get(url, headers=headlines_dict)
    data = response.json()
    lines = []
    for release in data['releases']:
        if release['seances'] == []:
            lines.append(f'Фильм: {release["title"]} - Сеансов нет ')
        else:
            times = []
            for seance in release['seances']:
                times.append(seance['start_date_time'][11:16])
            lines.append(f'Фильм: {release["title"]}, время: {",".join(times)}')
    return lines

result = get_playbill('2026-08-02')
print(result)



