"""Logic circuits"""


from gates import OR


def is_zero_8bit(a: str) -> bool:
    o1 = OR(a[0], a[1])
    o2 = OR(a[2], a[3])
    o3 = OR(a[4], a[5])
    o4 = OR(a[6], a[7])
    
    o5 = OR(o1, o2)
    o6 = OR(o3, o4)
    
    o7 = OR(o5, o6)
    return o7


def is_zero(a: str) -> str:
    """Return 1 if the number is zero"""
    def single_step(bits: str) -> str:
        n_out = len(bits) // 2
        ors = ["0"] * n_out
        for i in range(0, n_out, 2):
            ors[i] = OR(bits[i], bits[i - 1])
        ors = "".join(ors)
        return ors

    while len(a) > 1:
        a = single_step(a)

    return a
