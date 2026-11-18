# tweet-snippets

The Python code shown in my posts on X ([@dym6100](https://x.com/dym6100)), as small scripts you can run yourself.

Needs Python 3.11 or newer and nothing else: no packages to install.

```bash
python event-loop/gather_demo.py
```

| Folder | Script | What to watch for |
|---|---|---|
| event-loop | `gather_demo.py` | B finishes before A, and the whole run takes 2 s, not 3 s |
| coroutine-await | `forgot_await.py` | `save("a")` never prints, you only get a `RuntimeWarning` |
| cancellation | `timeout_catch.py` | `except Exception` doesn't catch the cancel. Change it to `BaseException` and the timeout gets swallowed |
| blocking-call | `blocking.py`, `await_sleep.py`, `to_thread.py` | `time.sleep` stalls the heartbeat (3.0 s total). The other two keep it on time (2.0 s) |
| async-generator | `token_stream.py`, `collect_list.py` | Words appear one by one vs all at once at the end |
| context-manager | `timer.py` | The second block raises, but "took" still prints before the error |
| binary-search | `binary_search.py` | Index of 45 in a sorted list, and -1 when it's missing |
| backtracking | `four_queens.py` | A 4-Queens solution: `[1, 3, 0, 2]` |
| rng | `lcg_die.py` | A toy random generator. Rejecting `x >= 12` makes every face come up equally often |
| walrus-operator | `walrus_examples.py` | `:=` in a loop, a condition and a comprehension |
| float-assoc | `float_order.py` | The same 8 numbers summed in random orders give 258 different answers |
