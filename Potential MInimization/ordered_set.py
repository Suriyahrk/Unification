class OrderedSet:
    def __init__(self):
        self.elements = []
        self.element_set = set()

    def add(self, element):
        if element not in self.element_set:
            self.elements.append(element)
            self.element_set.add(element)

    def discard(self, element):
        if element in self.element_set:
            self.elements.remove(element)
            self.element_set.remove(element)

    def __contains__(self, element):
        return element in self.element_set

    def __iter__(self):
        return iter(self.elements)

    def __len__(self):
        return len(self.elements)

    def __repr__(self):
        return repr(self.elements)

    def clear(self):
        self.elements.clear()
        self.element_set.clear()