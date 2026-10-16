"""Emulation of libstdc++ std::sort (introsort: median-of-3 pivot, unguarded partition, threshold 16, final insertion sort)
for Oink's step-0 reindexing (game.cpp:478-505 @ 8fbf0a7: identity if already non-decreasing, else std::sort of the index
array 0..n-1 with comparator priority(a) < priority(b)). Input construction only (TARGET step 0), not the solver.
Heap-sort fallback (depth limit 2*floor(log2 n)): std::__partial_sort(first, last, last) = make_heap + sort_heap,
emulated from libstdc++'s stl_heap.h algorithm (__adjust_heap / __push_heap / __pop_heap)."""


def oink_order(prio):
    n = len(prio)
    if all(prio[i - 1] <= prio[i] for i in range(1, n)):
        return list(range(n))
    a = list(range(n))
    lt = lambda x, y: prio[x] < prio[y]

    def median_to_first(r, x, y, z):
        if lt(a[x], a[y]):
            if lt(a[y], a[z]): a[r], a[y] = a[y], a[r]
            elif lt(a[x], a[z]): a[r], a[z] = a[z], a[r]
            else: a[r], a[x] = a[x], a[r]
        elif lt(a[x], a[z]): a[r], a[x] = a[x], a[r]
        elif lt(a[y], a[z]): a[r], a[z] = a[z], a[r]
        else: a[r], a[y] = a[y], a[r]

    def partition(f, l, piv):
        while True:
            while lt(a[f], a[piv]): f += 1
            l -= 1
            while lt(a[piv], a[l]): l -= 1
            if not f < l: return f
            a[f], a[l] = a[l], a[f]; f += 1

    def adjust_heap(f, hole, ln, value):
        top = hole; second = hole
        while second < (ln - 1) // 2:
            second = 2 * (second + 1)
            if lt(a[f + second], a[f + second - 1]):
                second -= 1
            a[f + hole] = a[f + second]; hole = second
        if (ln & 1) == 0 and second == (ln - 2) // 2:
            second = 2 * (second + 1)
            a[f + hole] = a[f + second - 1]; hole = second - 1
        parent = (hole - 1) // 2
        while hole > top and lt(a[f + parent], value):
            a[f + hole] = a[f + parent]; hole = parent; parent = (hole - 1) // 2
        a[f + hole] = value

    def heapsort(f, l):
        ln = l - f
        if ln >= 2:
            parent = (ln - 2) // 2
            while True:
                adjust_heap(f, parent, ln, a[f + parent])
                if parent == 0:
                    break
                parent -= 1
        while l - f > 1:
            l -= 1
            value = a[l]; a[l] = a[f]
            adjust_heap(f, 0, l - f, value)

    def introsort(f, l, depth):
        while l - f > 16:
            if depth == 0:
                heapsort(f, l)
                return
            depth -= 1
            mid = f + (l - f) // 2
            median_to_first(f, f + 1, mid, l - 1)
            cut = partition(f + 1, l, f)
            introsort(cut, l, depth)
            l = cut

    def linear_insert(i):
        val = a[i]; j = i - 1
        while lt(val, a[j]):
            a[i] = a[j]; i = j; j -= 1
        a[i] = val

    def insertion_sort(f, l):
        for i in range(f + 1, l):
            if lt(a[i], a[f]):
                val = a[i]; a[f + 1:i + 1] = a[f:i]; a[f] = val
            else:
                linear_insert(i)

    introsort(0, n, 2 * (n.bit_length() - 1))
    if n > 16:
        insertion_sort(0, 16)
        for i in range(16, n): linear_insert(i)
    else:
        insertion_sort(0, n)
    return a
