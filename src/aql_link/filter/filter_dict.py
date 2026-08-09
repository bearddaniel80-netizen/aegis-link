class Filter:
    def __init__(self):
        self.source = []

    def from_source(self, source: []):
        self.source = source
        return self

    def first(self):
        if not self.source:
            return self

        self.source = self.source[0]
        return self

    def get_source(self):
        if not self.source:
            return ""

        if isinstance(self.source, list):
            queries = []

            for q in self.source:
                queries.append(q["query"])

            return queries

        return self.source["query"]

    def where(self, field: str, value: str):
        self.source = [ q for q in self.source if value in q[field]]
        return self

    def print_source(self):
        print([q["query"] for q in self.source])
        print("Filtered: ", len(self.source))