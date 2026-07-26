import requests as req

playbill_url = 'https://kinokassa.kinoplan24.ru/api/v2/release/playbill?city_id=173&date=2026-07-27'
headlines_dict = {'x-application-token':'lHwxOYbbKyDx0qFPo6D7mCRBM6slPcDV', 'x-platform':'widget', 'x-preferred-language':'ru'}

response = req.get(playbill_url, headers=headlines_dict)
data = response.json()


# print(response.status_code)
# print(data)
# print(data['releases'])

print('==='*50)
for release in data['releases']:
    if release['seances'] == []:
        print('Сеансов нет')
    else:
        for seance in release['seances']:
            print(f'Фильм: {release["title"]}, время: {seance["start_date_time"][11:16]}')



