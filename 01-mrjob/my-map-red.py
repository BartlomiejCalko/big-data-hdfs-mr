from mrjob.job import MRJob
from mrjob.step import MRStep

class MapRedWordCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

    def mapper(self, _, value):
        yield 'lines ', 1
        yield 'all words ', len(value.split())
        yield 'characters ', len(value)

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MapRedWordCount.run()