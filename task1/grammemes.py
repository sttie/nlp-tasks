class Grammeme:
    def __init__(self, _id, name, brief_description, full_description, parent_name):
        self._id = _id
        self.name = name
        self.brief_description = brief_description
        self.full_description = full_description
        self.parent_name = parent_name

    def __repr__(self):
        return f"{self._id}\t{self.name}\t{self.brief_description}\t{self.full_description}\t{self.parent_name}"

def parse_grammemes(filepath):
    grammemes = {}
 
    with open(filepath, "r", encoding="utf-8") as grammemes_file:
        lines = grammemes_file.read().split("\n")
        for line in lines:
            _id, name, brief_description, full_description, parent_name = line.split("\t")
            grammemes[name] = Grammeme(_id, name, brief_description, full_description, parent_name)

    return grammemes
