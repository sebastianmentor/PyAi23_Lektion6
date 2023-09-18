def boka_tid(tider):
    ledig_tid_avbildad_till_menyval = {}
    menyval = 1
    for tid, är_ledig in tider.items():
        if är_ledig:
            print(f'Välj {menyval} för tiden mellan {tid} och {tid+1}.')
            ledig_tid_avbildad_till_menyval[menyval] = tid

    önskad_tid = int(input('Skriv in önskad tid!'))

    if önskad_tid in tider:
        tider[önskad_tid] = False
        print('Tiden är bokad')
    else:
        print('Den tiden finns inte! Vi går tillbaka!')

def kolla_om_bana_är_full_bokad(tider):
    return any(ledig for ledig in tider.values())

def boka_bana(banor):
    lediga_banor = []
    for bana, tider in banor.items():
        if kolla_om_bana_är_full_bokad(tider):
            lediga_banor.append(bana)

    if len(lediga_banor) == 0:
        print('Fullbokat tyvärr!')
        return
    elif len(lediga_banor) == 1:
        boka_tid(lediga_banor[0])
    else:
        print('Lediga banor!!')
        for ledig_bana in lediga_banor:
            print(f'Bana {ledig_bana} har lediga tider')

        önskad_bana = int(input('Skriv in önskad bana!'))
        if önskad_bana in lediga_banor:
            boka_tid(banor[önskad_bana])

def boka_sport(spelhall):
    for sport in spelhall:
        print(sport)

    önska_boka_sport = input('Vad önskar du boka för sport?')
    if önska_boka_sport in spelhall.keys():
        boka_bana(spelhall[önska_boka_sport])
    else:
        print('Finns ingen sådan sport!')



def skriv_ut_allt(spelhall):
    for sport, banor in spelhall.items():
        print(f'{sport}:')
        for bana, tider in banor.items():
            print(f'\t{bana}:')
            for tid, ledig_tid in tider.items():
                print(f'\t\t{tid} är {"ledig" if ledig_tid else "bokad"}')

def huvudmeny(spelhall):
    while True:
        print('1. Boka\n2. Skriv ut bokningar\n3. Avsluta')
        val = input('Gör ett val!!!')
        if val == '1':
            boka_sport(spelhall)
        elif val == '2':
            skriv_ut_allt(spelhall)
        elif val == '3':
            break
        else:
            print('Fel val!')

def lägg_till_tider_9_till_21_till_bana():
    bana = {}
    for i in range(9,22):
        bana[i] = True
    return bana

if __name__ == '__main__':
    ANTAL_BOWLINGBANOR = 3
    ANTAL_BADMINTONBANOR = 5
    ANTAL_TENNISBANOR = 4

    idrottshallen = {
                    "bowling":{},
                    "badminton":{},
                    "tennis":{}
                    }

    for i in range(1, ANTAL_BOWLINGBANOR + 1):
        idrottshallen["bowling"][i] = lägg_till_tider_9_till_21_till_bana()

    for i in range(1, ANTAL_BADMINTONBANOR + 1):
        idrottshallen['badminton'][i] = lägg_till_tider_9_till_21_till_bana()

    for i in range(1, ANTAL_TENNISBANOR + 1):
        idrottshallen['tennis'][i] = lägg_till_tider_9_till_21_till_bana()

    huvudmeny(idrottshallen)