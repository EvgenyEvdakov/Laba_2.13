def get_extremum(type="max"):
    def get_min_or_max(collection):
        if type == "max":
            return max(collection)
        else:
            return min(collection)
    return get_min_or_max