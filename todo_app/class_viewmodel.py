class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def to_do_items(self):
        to_do_output = []
        for item in self._items:
            if item.status == "To Do":
                to_do_output.append(item)

        return to_do_output

    @property
    def in_progress_items(self):
        in_progress_output = []
        for item in self._items:
            if item.status == "In Progress":
                in_progress_output.append(item)

        return in_progress_output

    @property
    def done_items(self):
        done_output = []
        for item in self._items:
            if item.status == "Done":
                done_output.append(item)

        return done_output
