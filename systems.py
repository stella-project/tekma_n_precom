import pandas as pd
import tarfile
import jsonlines


class Ranker(object):

    def __init__(self):
        self.idx = None
        with jsonlines.open('resources/livivo/livivo_hq_1000.jsonl') as q_in:
            self.q_translate = {q.get('qstr'): q.get('qid') for q in q_in}

    def index(self):
        try:
            with tarfile.open('precom/rank/run.tar.gz') as run_tar:
                run_tar.extract('run.txt', 'precom/rank')
            self.idx = pd.read_csv('precom/rank/run.txt', sep=' ', names=['num', 'Q0', 'docid', 'rank', 'score', 'runid'])
        except:
            pass

    def rank_publications(self, query, page, rpp):

        qid = self.q_translate.get(query)

        if self.idx is not None and qid:
            ranking = self.idx[self.idx['num'] == qid]
            itemlist = list(ranking['docid'][page * rpp:(page + 1) * rpp])
        else:
            ranking = []
            itemlist = []

        return {
            'page': page,
            'rpp': rpp,
            'query': query,
            'itemlist': itemlist,
            'num_found': len(ranking)
        }


class Recommender(object):

    def __init__(self):
        self.idx_datasets = None
        self.idx_publications = None

    def index(self):
        try:
            with tarfile.open('precom/rec/datasets/run.tar.gz') as run_tar:
                run_tar.extract('run.txt', 'precom/rec/datasets')
                self.idx_datasets = pd.read_csv('precom/rec/datasets/run.txt', sep=' ', names=['num', 'Q0', 'docid', 'rank', 'score', 'runid'])
        except:
            pass

        try:
            with tarfile.open('precom/rec/publications/run.tar.gz') as run_tar:
                run_tar.extract('run.txt', 'precom/rec/publications')
            self.idx_publications = pd.read_csv('precom/rec/publications/run.txt', sep=' ', names=['num', 'Q0', 'docid', 'rank', 'score', 'runid'])
        except:
            pass

    def recommend_datasets(self, item_id, page, rpp):

        if self.idx_datasets is not None:
            recommendation = self.idx_datasets[self.idx_datasets['num'] == item_id]
            itemlist = list(recommendation['docid'][page * rpp:(page + 1) * rpp + 1])
        else:
            recommendation = []
            itemlist = []

        return {
            'page': page,
            'rpp': rpp,
            'item_id': item_id,
            'itemlist': itemlist,
            'num_found': len(recommendation)
        }

    def recommend_publications(self, item_id, page, rpp):

        if self.idx_publications is not None:
            recommendation = self.idx_publications[self.idx_publications['num'] == item_id]
            itemlist = list(recommendation['docid'][page * rpp:(page + 1) * rpp])
        else:
            recommendation = []
            itemlist = []


        return {
            'page': page,
            'rpp': rpp,
            'item_id': item_id,
            'itemlist': itemlist,
            'num_found': len(recommendation)
        }
