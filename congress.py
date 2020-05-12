import csv
from collections import defaultdict,Counter                         # accumulating voting record
import glob
from pprint import pprint
from typing import NamedTuple, DefaultDict,List,Dict,Tuple

# OUR CUSTOM MODULE
from kmeans import k_means,assign_data

Senator = NamedTuple('Senator', [('name',str),('party',str),('state',str)])
VoteValue = int
VoteHistory = Tuple[VoteValue, ...]
NUM_SENATORS = 100

accumulated_record = defaultdict(list)                              #type: DefaultDict[Senator, List[VoteValue]]
vote_value = {'Yea':1, 'Nay':-1, "Not Voting":0}                    #type: Dict[str, VoteValue]
for file in glob.glob('congress_data/*.csv'):
    with open(file, encoding='utf-8') as f:       
        reader = csv.reader(f)      #iterator object
        vote_topic = next(reader)   #acc. to csv data
        headers = next(reader)      #acc. to csv data
        for person,state,district,vote,name,party in reader:
            senator = Senator(name,party,state)                                 
            accumulated_record[senator].append(vote_value[vote])
pprint(accumulated_record, width=500)

record = {senator:tuple(votes) for senator,votes in accumulated_record.items()}      #type: Dict[Senator,VoteHistory]
pprint(record, width=500)


#use kmeans to locate the cluster centroids from patterns of votes, assign each senetor to the nearest cluster
centroids = k_means(data=record.values(), num_centroids=3)
clustered_votes = assign_data(centroids=centroids, data=record.values())
pprint(clustered_votes)

#build a reverse mapping from a vote history to a list of senators that voted that way
votes_to_senators = defaultdict(list)                                                #type: DefaultDict[VoteHistory, List[Senator]]
for senator,vote_history in record.items():
    votes_to_senators[vote_history].append(senator)

#we know that come senators might have the same voting history,
#also check if all 100 are present even after rearranging by using assertion
assert sum([len(cluster) for cluster in votes_to_senators.values()]) == NUM_SENATORS

#display clusters and members of each clusters
for i,votes_in_clusters in enumerate(clustered_votes.values(),start=1):
    
    print(f'-------------- CLUSTER {i} --------------')
    party_totals = Counter()
    for votes_his in set(votes_in_clusters):
        for senator in votes_to_senators[votes_his]:
            party_totals[senator.party]+=1
            print(senator)
    print(party_totals)
