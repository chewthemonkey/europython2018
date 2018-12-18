def perform(xs):
    for group in deprecated_fn(*xs):
        for item in group:
            yield f(item)