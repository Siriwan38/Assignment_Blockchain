import json
import os
import hashlib

BLOCKCHAIN_DIR = 'blockchain/'

def get_hash(prev_block):
    with open(BLOCKCHAIN_DIR + prev_block, 'rb') as f:
        content = f.read()
    return hashlib.md5(content).hexdigest()

def check_integrity():
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))
    
    results = []
    
    for file in files[1:]:
        with open(BLOCKCHAIN_DIR + file) as f:
            block = json.load(f)
        
        prev_hash = block.get('prev_block').get('hash')
        prev_filename = block.get('prev_block').get('filename')
        
        actual_hash = get_hash(prev_filename)
        if prev_hash == actual_hash:
            res = 'OK'
        else:
            res = 'Was Changed'

        print(f'Block {prev_filename} : {res}')
        results.append({'block' : prev_filename, 'results' : res})
    return results




def write_block(T1, T2, About):
    
    blocks_count = len(os.listdir(BLOCKCHAIN_DIR))
    prev_block = str(blocks_count)
    

    data = {
        "Team1": T1,
        "Team2": T2,
        "About": About,
        "prev_block": {
            "hash": get_hash(prev_block),
            "filename": prev_block
        }
    }

    current_block = BLOCKCHAIN_DIR + str(blocks_count+1)

    with open(current_block, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.write('\n')


def show_data():
    files = sorted(os.listdir(BLOCKCHAIN_DIR), key=lambda x: int(x))
    data = []
    for file in files[1:]:
        with open(BLOCKCHAIN_DIR + file) as f:
            block = json.load(f)
        
        prev_filename = block.get('prev_block').get('filename')
        T1 = block.get('Team1')
        T2 = block.get('Team2')
        About =  block.get('About')
        actual_hash = get_hash(prev_filename)

        data.append({'block' : prev_filename, 'Team1' : T1, 'Team2' : T2, 'About' : About})
    return data


def main():
    write_block(T1 = 'MAMA', T2 = 'LOOKOM',About = '16/02/2022 09:00')
    write_block(T1 = 'Alpha Red.', T2 = 'EVOS Debut',About = '17/02/2021 09:00')
    write_block(T1 = 'BAZAAR Gaming', T2 = 'IT.City Bacon',About = '18/02/2021 09:00')
    write_block(T1 = 'Buriram Arctic Wolf.', T2 = 'RRQ.',About = '19/02/2021 09:00')
    write_block(T1 = 'Diamond Cobra', T2 = 'Valencia CF',About = '20/02/2021 09:00')
    write_block(T1 = 'eArena', T2 = 'King of Gamers Club',About = '21/02/2021 09:00')
    write_block(T1 = 'PSG Esports', T2 = 'GOLDCITY Esports',About = '22/02/2021 09:00')
    write_block(T1 = 'Dtac x Talon', T2 = 'Team Olympus',About = '23/02/2021 09:00')
    write_block(T1 = 'UndeRank', T2 = 'X eSports',About = '24/02/2021 09:00')
    write_block(T1 = 'Hongkong Attitude', T2 = 'PPR.QC',About = '25/02/2021 09:00')
    check_integrity()
    

if __name__ == '__main__':
    main()