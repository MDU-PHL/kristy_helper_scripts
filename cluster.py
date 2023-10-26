from sklearn.cluster import AgglomerativeClustering
import pandas,numpy,sys

mat = []
isos = []
st = sys.argv[1]
with open(f"ST{st}/report/distances.tab", 'r') as f:

    lines = f.read().strip().split('\n')
    for line in lines[1:]:
        row = line.split('\t')[1:]
        isos.append(line.split('\t')[0])
        mat.append(row)

print(isos)
print(mat)
result = pandas.DataFrame()
X = numpy.array(mat,dtype=object)
for n in [1,2,5,10,20]:
    clustering = AgglomerativeClustering(n_clusters = None, affinity = 'precomputed',linkage = 'single', distance_threshold =n).fit(X)

    df = pandas.DataFrame(data = {'Seq_ID': isos, f'Tx:{n}': clustering.labels_})
    if result.empty:
        result = df
    else:
        result = result.merge(df)

print(result)

result.to_csv(f'snp_clusters_at_{st}.csv', index = False)


