DATA_PATH = 'data'
MODEL_PATH = 'all_models'
MODEL_VERSION = 'v_best'

# Целевые переменные
targets = ['Артериальная гипертензия', 'ОНМК',
       'Стенокардия, ИБС, инфаркт миокарда', 'Сердечная недостаточность',
       'Прочие заболевания сердца']

# Список отобранных важных переменных
selected_feats = {
    targets[0]: ['is_pensia', 'diabet', 'lekarstva', 'perelomy', 'education'],
    targets[1]: ['is_work', 'is_pensia', 'stop_illness_work', 'lekarstva', 'perelomy', 'stag_kur', 
                 'sigaret_chastot', 'Возраст алког', 'sex', 'is_religia', 'education', 'is_kurit',
                  'is_kuril', 'is_pil', 'is_pil_ranshe', 'how_many_kurit_passive', 'hour_son', 'dlina_sna', 'nizk'],
    targets[2]: ['is_work', 'is_pensia', 'diabet', 'lekarstva', 'sigaret_chastot', 'education', 'is_kurit',
                 'is_not_pyet', 'is_pil_ranshe', 'how_many_kurit_passive', 'dlina_sna'],
    targets[3]: ['is_work', 'is_pensia', 'lekarstva', 'stag_kur', 'sigaret_chastot', 'Возраст алког', 
                 'was_zamug', 'education', 'is_pyet', 'is_not_pyet', 'how_many_kurit_passive', 'hour_son', 'dlina_sna'],
    targets[4]: ['lekarstva', 'sigaret_chastot', 'passive', 'Возраст алког', 'dlina_sna']
}
