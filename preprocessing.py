import pandas as pd


## Генерация и препроцессинг фичей
def prep(train_df):
    train_df['is_zamug'] = train_df['Семья'].isin([
        'в браке в настоящее время', 'гражданский брак / проживание с партнером', 
        'раздельное проживание (официально не разведены)'
    ])

    train_df['was_zamug'] = train_df['Семья'].isin([
        'вдовец / вдова', 
        'в разводе'
    ])

    train_df['sex'] = (train_df['Пол'] == 'М').astype(int)
    train_df.rename(columns={'Семья':'family'}, inplace=True)
    train_df['is_europe'] = (train_df['Этнос'] == 'европейская').astype(int)
    train_df['is_rus'] = (train_df['Национальность'] == 'Русские').astype(int)
    train_df['is_religia'] = (train_df['Религия'].isin(['Ислам', 'Христианство'])).astype(int)
    train_df.rename(columns={'Религия':'religia'}, inplace=True)
    train_df['education'] = train_df['Образование'].apply(lambda x: int(x[0]))
    train_df['is_kurit'] = (train_df['Статус Курения'] == 'Курит').astype(int)
    train_df['is_not_kurit'] = (train_df['Статус Курения'] != 'Курит').astype(int)
    train_df['is_kuril'] = (train_df['Статус Курения'] != 'Никогда не курил(а)').astype(int)
    train_df['is_kuril_ranshe'] = (train_df['Статус Курения'] == 'Бросил(а)').astype(int)

    train_df['is_pyet'] = (train_df['Алкоголь'] == 'употребляю в настоящее время').astype(int)
    train_df['is_not_pyet'] = (train_df['Алкоголь'] != 'употребляю в настоящее время').astype(int)
    train_df['is_pil'] = (train_df['Алкоголь'] != 'никогда не употреблял').astype(int)
    train_df['is_pil_ranshe'] = (train_df['Алкоголь'] == 'ранее употреблял').astype(int)

    train_df['Возраст курения'].fillna(0, inplace=True)
    train_df['Сигарет в день'].fillna(0, inplace=True)
    train_df['Частота пасс кур'].fillna(0, inplace=True)
    train_df['how_many_kurit_passive'] = train_df['Частота пасс кур'].replace(
        {
            '1-2 раза в неделю': 1.5/7,
            '4 и более раз в день': 5,
            '2-3 раза в день':2.5,
            'не менее 1 раза в день':1,
            '3-6 раз в неделю': 4.5/7  
        }
    )
    train_df['Возраст алког'].fillna(0, inplace=True)
    train_df['hour_son'] = train_df['Время засыпания'].apply(lambda x: float(x.split(':')[0]))
    train_df['dlina_sna'] = train_df.apply(lambda x: (pd.to_datetime(x['Время пробуждения']) - 
                                                      pd.to_datetime(x['Время засыпания'])).seconds/3600, axis=1)

    train_df.rename(columns={'Профессия':'professia', 'Вы работаете?': 'is_work',
                             'Выход на пенсию': 'is_pensia',
                             'Прекращение работы по болезни': 'stop_illness_work',
                             'Сахарный диабет': 'diabet', 'Гепатит': 'gepatit',
                             'Онкология': 'onkology', 'Хроническое заболевание легких': 'legkie',
                             'Бронжиальная астма':'astma', 'Туберкулез легких ': 'tuberkulez',
                             'ВИЧ/СПИД':'vich', 'Регулярный прим лекарственных средств': 'lekarstva',
                             'Травмы за год': 'travmy', 'Переломы': 'perelomy',
                             'Возраст курения':'stag_kur', 'Сигарет в день': 'sigaret_chastot',
                             'Пассивное курение': 'passive', 
                             'Сон после обеда': 'son_dnem', 'Спорт, клубы':'sport', 'Религия, клубы':'clubs', 
                            }, inplace=True)
    train_df['diplom'] = (train_df['professia'] == 'дипломированные специалисты').astype(int)
    train_df['nizk'] = (train_df['professia'] == 'низкоквалифицированные работники').astype(int)
    dropcols = ['Статус Курения', 'Частота пасс кур', 'Алкоголь', 'Этнос', 'Национальность', 'Образование',
                'Время засыпания', 'Время пробуждения', 'ID_y', 'Пол', 'family', 'religia', 'professia']
    return train_df.drop(dropcols, axis=1, errors='ignore')
